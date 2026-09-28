"""Assemble the deployable site for marriagecontract.org, publishing articles on their dates.

  python publish.py                 build _site/ for today (America/New_York)
  python publish.py --today 2026-12-01   build as if it were that date (for previewing)

Runs in GitHub Actions every morning and on every push (.github/workflows/pages.yml), and the
workflow deploys _site/ to GitHub Pages. Only the standard library is used.

Articles arrive ready-made from the book repo's build_site.py as
_scheduled/YYYY-MM-DD--slug.html. One whose date has come is copied to articles/slug.html.
Then this script writes articles/index.html (from _scheduled/articles-index.tmpl.html), the
latest three on the front page (between <!--LATEST--> and <!--/LATEST-->), feed.xml, sitemap.xml
and robots.txt. Nothing in _scheduled/ is deployed.
"""
import datetime as dt
import html
import re
import shutil
import sys
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "_site"
BASE = "https://marriagecontract.org/"
SKIP = {".git", ".github", "_scheduled", "_site", "publish.py", "README.md", ".gitignore"}


def today():
    if "--today" in sys.argv:
        return dt.date.fromisoformat(sys.argv[sys.argv.index("--today") + 1])
    return dt.datetime.now(ZoneInfo("America/New_York")).date()


def meta(page, name):
    m = re.search(r'<meta name="%s" content="([^"]*)"' % name, page)
    return html.unescape(m.group(1)) if m else ""


def title_of(page):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", page, re.S)
    return html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else ""


def main():
    day = today()
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT, OUT, ignore=lambda d, names: [n for n in names if Path(d) == ROOT and n in SKIP])

    published, upcoming = [], []
    for f in sorted((ROOT / "_scheduled").glob("????-??-??--*.html")):
        date_s, slug = f.stem.split("--", 1)
        date = dt.date.fromisoformat(date_s)
        page = f.read_text(encoding="utf-8")
        item = dict(date=date, slug=slug, title=title_of(page), desc=meta(page, "description"), page=page)
        (published if date <= day else upcoming).append(item)
    published.sort(key=lambda a: a["date"], reverse=True)
    (OUT / "articles").mkdir(exist_ok=True)
    for a in published:
        (OUT / "articles" / f"{a['slug']}.html").write_text(a["page"], encoding="utf-8")

    def when(d):
        return f"{d:%B} {d.day}, {d.year}"

    # articles index
    tmpl = (ROOT / "_scheduled" / "articles-index.tmpl.html").read_text(encoding="utf-8")
    if published:
        items = "".join(f'<li><a href="{a["slug"]}.html"><strong>{html.escape(a["title"])}</strong></a>'
                        f'<br><span class="sans" style="font-size:.85rem;color:#5d6472">{when(a["date"])}</span>'
                        f'<br>{html.escape(a["desc"])}</li>' for a in published)
        listing = f'<ul class="articles">{items}</ul>'
    else:
        listing = "<p>Nothing yet.</p>"
    if upcoming:
        nxt = min(a["date"] for a in upcoming)
        listing += f'<p class="sans" style="font-size:.9rem;color:#5d6472">A new one every week. The next is out on {when(nxt)}.</p>'
    (OUT / "articles" / "index.html").write_text(tmpl.replace("<!--ARTICLES-->", listing), encoding="utf-8")

    # latest three on the front page
    front = (OUT / "index.html").read_text(encoding="utf-8")
    if published:
        latest = "".join(f'<li><a href="articles/{a["slug"]}.html">{html.escape(a["title"])}</a></li>' for a in published[:3])
        block = f'<h2>From the site</h2><ul>{latest}</ul><p><a href="articles/index.html">All articles</a></p>'
    else:
        block = ""
    front = re.sub(r"<!--LATEST-->.*?<!--/LATEST-->", f"<!--LATEST-->{block}<!--/LATEST-->", front, flags=re.S)
    (OUT / "index.html").write_text(front, encoding="utf-8")

    # RSS
    items = "".join(
        f"<item><title>{html.escape(a['title'])}</title><link>{BASE}articles/{a['slug']}.html</link>"
        f"<guid>{BASE}articles/{a['slug']}.html</guid>"
        f"<pubDate>{dt.datetime(a['date'].year, a['date'].month, a['date'].day, 12, 0, tzinfo=dt.timezone.utc):%a, %d %b %Y %H:%M:%S +0000}</pubDate>"
        f"<description>{html.escape(a['desc'])}</description></item>" for a in published[:20])
    (OUT / "feed.xml").write_text(
        '<?xml version="1.0" encoding="utf-8"?><rss version="2.0"><channel>'
        f"<title>The Marriage Contract</title><link>{BASE}</link>"
        "<description>Articles on the marriage contract every married couple already has.</description>"
        f"{items}</channel></rss>\n", encoding="utf-8")

    # sitemap + robots
    urls = sorted(p.relative_to(OUT).as_posix() for p in OUT.rglob("*.html"))
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="utf-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        + "".join(f"<url><loc>{BASE}{'' if u == 'index.html' else u}</loc></url>" for u in urls)
        + "</urlset>\n", encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n", encoding="utf-8")

    print(f"{day}: {len(published)} published, {len(upcoming)} scheduled; {len(urls)} pages in _site/")


if __name__ == "__main__":
    main()
