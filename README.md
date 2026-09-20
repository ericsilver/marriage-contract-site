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
- This is a working draft. Legal statements have not yet been checked against primary sources or reviewed by counsel.

## State pages

A state page is published once its entries have been checked against the statutes and cases it cites. The pages are not reviewed by a lawyer, and each one says when it was last checked. None are up yet.

## How this repository is built

The files are generated from the book's appendix sources by a build script that lives with the manuscript. Please don't edit `index.html` or `contracts/*.txt` by hand; changes will be overwritten. Corrections are welcome as issues.

## Rights

Copyright Eric Silver. All rights reserved for now; a licence for the contract texts will be chosen before publication. You are welcome to copy the contracts for your own personal use, including pasting them into a chatbot or giving them to your lawyer.
