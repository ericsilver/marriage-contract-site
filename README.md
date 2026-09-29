# The Marriage Contract: companion site

Companion material for *The Marriage Contract*, a book by Eric Silver about the agreement every married couple already has: the default terms their state wrote for them.

This repository holds only what is meant to be public. The manuscript is not here.

## What's here

| Path | What it is |
|---|---|
| `index.html` | One page with every sample contract, a copy-to-clipboard button for each, and the list of state pages |
| `contracts/default.txt` | The default marriage contract, reconstructed from statutes and case law, with the main state variations as options |
| `contracts/generous.txt` | The Generous Contract: "what's mine is yours," in writing |
| `contracts/nosurprises.txt` | The No-Surprises Contract: built to minimize regret by replacing judicial discretion with numbers |
| `contracts/children.txt` | The Children's Contract: the children's stability comes before either spouse's share |
| `luck.html` | The Luck of the Draw Index: every state scored 0-100 on how much of the money at a divorce is left to the judge, with the statute or case behind each of five parts |
| `worksheet.html` | A printable worksheet for reading the default contract together, article by article |
| `states/_template.md` | The template every state page follows |

The `.txt` files are plain text, one paragraph per line, so they can be pasted into a chatbot ("explain Article 6 to me," "what would this do to a couple like us?") or marked up and taken to a lawyer.

Words in `[[double brackets]]` are the "luck of the draw" terms: places where the contract hands the decision to a judge or arbitrator instead of giving an answer.

## Read this first

These are starting points for a conversation, not finished legal documents, and nothing here is legal advice.

- No template is enforceable merely because both of you signed it.
- Each spouse needs an independent lawyer licensed in their own state.
- Nothing a couple signs binds a court about their children.
- Retirement plans need their own paperwork; a prenup cannot waive rights in a 401(k) or pension.
- The default contract is a reconstruction. No legislature enacted these words.
- No lawyer has reviewed the contracts or the state pages.

## State pages

Every state page carries its Luck of the Draw score, with each part checked against the statute or case it cites; a part not yet checked says so. The rest of a state page is published once its entries have been checked the same way. The pages are not reviewed by a lawyer.

## How this repository is built

The files are generated from the book's appendix sources by a build script that lives with the manuscript. Please don't edit `index.html` or `contracts/*.txt` by hand; changes will be overwritten. Corrections are welcome as issues.

## Rights

The contract texts (`contracts/*.txt` and the contracts page) are licensed under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0). You may copy, adapt, and share them for any purpose, including commercial use, if you credit *The Marriage Contract, 2027* by Eric Silver. Everything else on the site is copyright Eric Silver, all rights reserved.
