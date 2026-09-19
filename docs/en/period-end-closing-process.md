# Period-End Closing Process (Period End)

> **Period End** is the process run **when closing the books each month/period**. When run, the
> system automatically **creates the routine closing journals** — mainly **asset depreciation** and
> **foreign-exchange adjustments** — so the user does no manual math.

---

## Where & how to run it

Menu: **Activities → Periodic → Period End**. Then:
1. Pick the **Period** (month) and **Year** to close. The system shows the **Last Period End** (the
   most recently closed period) to keep things in order and prevent skipping.
2. Enter the **closing Exchange Rate** for each foreign currency (e.g. USD, AUD, EUR); IDR = 1.
3. Click **OK** → the system automatically creates the **closing Journal Vouchers**.

> The results appear as Journal Vouchers of type **Period End** and **Depreciation Asset** (e.g.
> "Period End Process for Jun 2026") — viewable & verifiable in the Journal Voucher list.

---

## What Period End auto-journals

**1. Fixed-asset depreciation (Depreciation Asset).**
The system computes depreciation for **all assets at once** for that period, detailed per asset & per
department:
```
Dr  Depreciation Expense (per asset category)
    Cr  Accumulated Depreciation (per asset category)
```
*(This is the monthly depreciation from the [Fixed Asset Module](fixed-asset-module.md) — no manual JV.)*

**2. Foreign-exchange adjustment (currency revaluation).**
Balances held in **foreign currency** (cash, bank, receivables, payables in USD/AUD/EUR) are
**revalued to the closing rate** you entered. The difference is recorded as a **forex gain/loss**:
- **Realized** and **Unrealized** — posted to the *Gain/Loss* accounts already mapped in
  **Preferences → Currency Default Account**.

Simple example: the company holds **USD 1,000**. Recorded at a rate of IDR 15,000 (value IDR
15,000,000). At month-end the closing rate is IDR 15,200 → value becomes IDR 15,200,000. The
**IDR 200,000** difference is recorded as an **(unrealized) forex gain**:
```
Dr  Cash USD                        200,000
    Cr  Forex Gain (Unrealized)          200,000
```

*(Other process types that may appear: Roll Over Goods and Project Expense Payment — depending on the
modules the company uses.)*

---

## When to run Period End (relation to closing the books)

Period End is run **after**:
1. **All transactions for the current period are fully entered**, and
2. **Bank & cash reconciliation is zero** (see [Tips: prerequisite for closing FS](tips-finding-discrepancies.md#the-main-prerequisite-before-closing-the-books-closing-fs)).

Only then is Period End run to post depreciation & forex differences, so the **period's Financial
Statements are ready to close** and the next period can open.

---

## Bottom line

> **Period End = one button to post depreciation & forex differences at month close.** The system
> computes and journals everything (detailed per asset/currency), and the results can be checked as
> Journal Vouchers. The user just ensures transactions are complete and cash/bank is balanced before
> running it.
