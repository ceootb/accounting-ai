# Model Card — Accounting AI (draft)

> Placeholder until v0.1 weights are published on Hugging Face.

- **Intended use:** accounting/bookkeeping assistance — journal entries, COA mapping, transaction categorization, bookkeeping Q&A. English & Indonesian (PSAK/PPN aware).
- **Out of scope:** legal/tax advice, audit sign-off, or any use where an error is unacceptable without human review. Always have a qualified accountant verify outputs.
- **Base model:** TBD (small, 1–3B class, permissively licensed).
- **Training data:** open datasets in `data/` (community-contributed, anonymized). See CONTRIBUTING.md.
- **Limitations:** may produce plausible-but-wrong entries; must not be trusted blindly. Double-entry outputs should be checked to balance.
- **License:** Apache-2.0.
