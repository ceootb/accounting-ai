# Formats of the 3 Core Financial Statements

> This is the **format/layout** of the three main financial statements — line by line. All numbers
> here are **illustrative only**. A report is **not** a new transaction: it merely **pulls and tidies
> the ending account balances from the General Ledger**, so it can only print once the data exists.
> The layout follows **PSAK** (financial-statement presentation) and commonly published statements.
>
> Concepts & how the statements connect: [Financial Statement Forms (Foundation)](financial-statements.md).

---

## 1. Income Statement (Profit & Loss) — for the period

Measures **performance** over a period: revenue minus expenses = profit/loss.

```
INCOME STATEMENT
For the year ended 31 December 20XX
─────────────────────────────────────────────
Sales Revenue                        1,000,000,000
(-) Sales Returns & Discounts           (20,000,000)
                                     ───────────────
Net Revenue                            980,000,000
(-) Cost of Goods Sold (COGS)         (600,000,000)
                                     ───────────────
GROSS PROFIT                           380,000,000

Operating Expenses:
   Selling Expenses                    (90,000,000)
   General & Administrative Expenses  (150,000,000)
                                     ───────────────
OPERATING PROFIT                       140,000,000

Other Income / (Expenses):
   Interest income                       5,000,000
   (Interest expense)                   (8,000,000)
   Forex gain/(loss)                     2,000,000
                                     ───────────────
PROFIT BEFORE TAX                      139,000,000
(-) Income Tax Expense                 (30,580,000)
                                     ═══════════════
NET PROFIT                             108,420,000
```

---

## 2. Statement of Changes in Equity

Explains the **change in equity** from the start to the end of the period. **Net profit** from the
Income Statement flows in here.

**Sole proprietorship / partnership form:**
```
STATEMENT OF CHANGES IN EQUITY
For the year ended 31 December 20XX
─────────────────────────────────────────────
Opening capital                        500,000,000
(+) Net profit for the period          108,420,000
(-) Owner's drawings                    (30,000,000)
                                     ═══════════════
Closing capital                        578,420,000
```

**Limited company (PT) form:**
```
Share Capital (paid-in)                400,000,000
Retained Earnings, opening             100,000,000
(+) Net profit for the period          108,420,000
(-) Dividends                           (30,000,000)
                                     ═══════════════
Total Equity, closing                  578,420,000
```

---

## 3. Statement of Financial Position (Balance Sheet)

A snapshot of the **financial position** at one date: what is **owned** (Assets) = where it **came
from** (Liabilities + Equity). The **closing equity** from the Changes-in-Equity statement flows in here.

```
STATEMENT OF FINANCIAL POSITION (BALANCE SHEET)
As at 31 December 20XX
─────────────────────────────────────────────
ASSETS
 Current Assets:
   Cash & Bank                         150,000,000
   Accounts Receivable                  200,000,000
   Inventory                            250,000,000
   Prepaid Expenses                      20,000,000
                                     ───────────────
   Total Current Assets                 620,000,000
 Non-current Assets:
   Fixed Assets                         500,000,000
   (Accumulated Depreciation)           (90,000,000)
                                     ───────────────
   Total Non-current Assets             410,000,000
                                     ═══════════════
 TOTAL ASSETS                        1,030,000,000

LIABILITIES & EQUITY
 Current Liabilities:
   Accounts Payable                     280,000,000
   Taxes Payable                         31,580,000
   Accrued Expenses                      40,000,000
                                     ───────────────
   Total Current Liabilities            351,580,000
 Non-current Liabilities:
   Long-term Bank Loan                  100,000,000
                                     ───────────────
 Total Liabilities                      451,580,000

 Equity:
   Share Capital / Paid-in Capital      400,000,000
   Retained Earnings                    178,420,000
                                     ───────────────
   Total Equity                         578,420,000
                                     ═══════════════
 TOTAL LIABILITIES & EQUITY          1,030,000,000
```

> **TOTAL ASSETS = TOTAL LIABILITIES & EQUITY** (1,030,000,000 = 1,030,000,000). If they don't match,
> some entry isn't balanced.

---

## How the three connect

```
Income Statement  →  Net Profit  →  goes into Changes in Equity
Changes in Equity  →  Closing Equity  →  goes into the Balance Sheet
Balance Sheet  →  Assets = Liabilities + Equity (always balances)
```

> **Order of preparation:** do the **Income Statement** first (get net profit) → feed it into
> **Changes in Equity** (get closing equity) → feed that into the **Balance Sheet**. All three stay
> consistent because they all draw from the **General Ledger balances** produced by auto-journaling. A
> report can only be populated once transactions are entered and (for period-end reports) the
> period-end process has been run.
