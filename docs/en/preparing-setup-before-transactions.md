# Preparing Setup Data Before Transactions — A Simple Explanation

> For **users who don't need to be accounting experts**. The point:
> **all the basic data is prepared first**, so the moment a transaction is entered, the system
> already knows where to record it — and the financial statements form by themselves.
>
> *(The more technical, full field list is in [setup-module.md](setup-module.md), used when building
> the software.)*

---

## Why prepare it first?

Think of **cooking in a kitchen**. Before you start, the ingredients, spices, and recipe must already
be there and organized. If the salt is in its place and the recipe is clear, cooking is fast and the
result is consistent. Accounting is the same: if the **setup data is tidy up front**, then when a
transaction comes in, the system isn't confused — it immediately knows which account to record it to,
and the reports at the back end become automatic and correct.

There are **3 things to prepare** before the first transaction:

```
1. Company Info   → the company's identity & periods
2. Preferences    → the rules + the "account map" (the key to auto-journaling)
3. User Profile   → who is allowed to do what (security)
```

---

## 1. Company Info — filling in the company's identity

This is like filling in the **company's ID card**. What you enter:

- **Identity:** name, address, phone, and the main **currency** (e.g. Rupiah).
- **Bookkeeping period:** when the fiscal year starts, and the current **period**.
- **Tax data:** tax ID, taxable-company status, and related tax codes.

The period part matters as a **safeguard**: the system can give a **warning** or even **reject** an
attempt to record a transaction in a month that's already closed, or on an unreasonable date. So no
one can quietly change old-period figures.

---

## 2. Preferences — the rules and the "account map"

This is the **most decisive** part. Here we tell the system **two things**:

**a) General rules** — for example the inventory valuation method (FIFO), date format, how tax is
computed, and due-date reminders.

**b) The "account map" (default accounts)** — this is the key. Each type of transaction is **linked
in advance** to the right account. For example:

- When there's a **sale** later → record it to **Receivables** and **Revenue**.
- When there's a **purchase** → record it to **Inventory** and **Payables**.
- When there's **tax** → it goes to the **VAT** account.

Because this "map" is built up front, users later **don't have to pick accounts one by one** during
entry. They just fill in the transaction, and the system automatically records it to the correct
account. **This is what makes the journal form automatically** — and why the financial statements
come out tidy right away.

---

## 3. User Profile — who is allowed to do what

This is about **security and trust**. Each staff member gets their **own login**, and their **access
rights** are set: allowed to create, edit, delete, or only view — per area (sales, purchasing,
general ledger, and so on).

The principle: **no single person should be allowed to do everything.** Whoever inputs, whoever
approves, and whoever holds the money should be **different people**. The riskiest rights — like
**deleting data** or **changing selling prices** — are tightly restricted. This protects the company
from both mistakes and fraud.

---

## In one breath

> **All setup data — the company's identity, the rules + account map, and access rights — is prepared
> before the first transaction.** Because this preparation is tidy, when the user enters a
> transaction the system already knows where to record it. The result: automatic journals, a tidy
> general ledger, and **financial statements that form by themselves** — without the user needing to
> be an accounting expert.
