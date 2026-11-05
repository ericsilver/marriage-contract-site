# The Marriage Contract: companion site

Companion material for *The Marriage Contract, 2027*, a book by Eric Silver about the terms every married couple already has, written for them by their state.

This repository holds only what is meant to be public. The manuscript is not here.

## What's here

| Path | What it is |
|---|---|
| `index.html` | What the book is, who should and shouldn't buy it, and what's free on the site |
| `contracts.html` | The book's four contracts, with a copy button for each |
| `contracts/default.txt` | The default contract, a reconstruction from statutes and case law, with the main state variations as options |
| `contracts/generous.txt` | The Generous Contract: sharing nearly everything, in writing |
| `contracts/nosurprises.txt` | The No-Surprises Contract: numbers in place of judicial discretion |
| `contracts/children.txt` | The Children's Contract: the children's stability ahead of either spouse's share |
| `luck.html` | The Luck of the Draw Index: every state scored 0-100 on how much of the money at a divorce is left to the judge, with the statute or case behind each of five parts |
| `worksheet.html` | A printable worksheet for reading the default contract together, article by article |
| `states/_template.md` | The template every state page follows |

The `.txt` files are plain text, one paragraph per line, for pasting into a chatbot or marking up for a lawyer. Words in `[[double brackets]]` are the "luck of the draw" terms, which leave a decision to a judge or arbitrator.

The contracts are Appendices A and B of the book, as the book prints them. One sentence is corrected here until the book is: the plain-English note to Article 3 of the default contract says that only three of the nine community-property states must split property evenly at a divorce.

## Read this first

These are places to start a conversation. They aren't finished legal documents, and nothing here is legal advice.

- Signing a template doesn't make it enforceable.
- Each of you needs a separate lawyer licensed in your own state.
- No agreement between a couple binds a court on their children.
- Retirement plans need their own paperwork. A prenup can't give up rights in a 401(k) or pension.
- The default contract is a reconstruction. No legislature enacted these words.
- No lawyer has reviewed the contracts or the state pages.

## State pages

Every state page carries its Luck of the Draw score, with each part checked against the statute or case it cites; a part not yet checked says so. The rest of a state page is published once its entries have been checked the same way. The pages are not reviewed by a lawyer.

## How this repository is built

A build script that lives with the manuscript generates these files. It takes the contracts from the book's appendices; the rest of the page copy is written for the site. Please don't edit `index.html` or `contracts/*.txt` by hand; changes will be overwritten. Corrections are welcome as issues.

## Rights

The contract texts (`contracts/*.txt` and the contracts page) are licensed under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0). Copy, adapt and share them for any purpose, commercial use included, with credit to Eric Silver's *The Marriage Contract, 2027*. Everything else on the site is copyright Eric Silver, all rights reserved.
