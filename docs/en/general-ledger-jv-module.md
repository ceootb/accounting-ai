# General Ledger Module — Journal Voucher (JV)

> The **Journal Voucher (JV)** is the **5th ledger** of the [5-Ledgers concept](how-accounting-system-works.md).
> Unlike the other four (Purchases, Sales, Cash Payments & Cash Receipts), the JV is a **manual
> journal** for things **not** covered by automatic transactions. Plain language for users; technical
> detail is kept for the software-build stage.

---

## What is the JV used for?

The JV is used for **adjustments and corrections** — journals that don't come out of the
Sales/Purchase/Cash modules. Common uses:
- **Amortizing prepaid expenses** (rent, insurance, etc.).
- **Reclassifying** accounts (wrong posting → moved).
- **Settling cash advances** given to staff.
- **Correcting** recording errors.

> **Note:** **asset depreciation is computed automatically by the Fixed Asset module**, so no manual JV is needed.

> Because it adjusts figures manually, the **JV is usually restricted to supervisors/managers** — not
> regular input staff. This is part of internal control (see access rights in the Setup module).

---

## Fields to fill

**a) Top section:**
- **Voucher No.** — voucher number (auto).
- **Date** — the journal date.
- **Description** — a note (e.g. "office rent amortization September").
- **Multi Currency** — tick if foreign currency is involved.

**b) Journal-line grid:**
- **Account No. / Account Name** — pick an account from the **COA** list. Either via the
  **search option** or simply by **typing the account name/number** (e.g. type "pet" → *Cash - Petty
  Cash* appears).
- **Debit** / **Credit** — enter the value on the correct side.
- **Memo** — a per-line note.
- **Department** — cost center (optional).
- **Subsidiary Ledger** — if the account has a sub-ledger (e.g. Receivables/Payables per
  person/vendor), pick the related sub-account so the per-party detail also updates.

**c) Bottom:** the **Debits** and **Credits** totals are shown. **The voucher can only be saved when
Debits = Credits (balanced).** It can be made **Recurring** for monthly adjustments.

---

## Example 1 — Amortizing a prepaid rent expense (as requested)

Say the company pays **one year of office rent up front, IDR 12,000,000**, in January. When paid, the
amount goes into the asset account **"Prepaid Rent"** — it isn't an expense yet.

At each month-end, **1/12 = IDR 1,000,000** is recognized as expense via a JV:
```
Dr  Office Rent Expense            1,000,000
    Cr  Prepaid Rent                   1,000,000
```
> The prepaid asset decreases each month, and expense is recognized in the right month (the
> **matching** principle). After 12 months the prepaid balance is used up. This JV is a good fit for
> **recurring** since it repeats monthly.

---

## Example 2 — Settling a staff cash advance

Say a purchasing staffer is given a **cash advance of IDR 3,200,000** for an event (when given, it's
recorded as an **Employee Advance / Receivable**). After the event, they account for it: actual
expense **IDR 2,900,000**, and **IDR 300,000** cash returned. The JV:
```
Dr  Activity Expense               2,900,000
Dr  Cash/Bank (returned balance)     300,000
    Cr  Employee Advance               3,200,000
```
> The advance is "cleared" (Cr) for the full amount originally given; the debit side details where the
> money went + the returned balance. Debits = credits. If the account has a sub-ledger (e.g. per staff
> name), pick the **Subsidiary Ledger** so the per-person detail updates too.

---

## Bottom line

> **JV = a manual journal for adjustments & corrections** not produced by the automatic modules. The
> rule is the same: **it must balance (Debits = Credits)**. Because it hits the General Ledger
> directly, access is restricted to supervisors/managers. It completes the other four automatic books
> into a full set of **5 Ledgers**.
