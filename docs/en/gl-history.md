# General Ledger History (GL History)

**GL History** is a **collection of journal postings per GL account** that can be **filtered per column**,
printed via **Print Preview**, and **drilled down back to the source transaction (voucher)**. GL History
is the **detail that forms the Account Balance**, and the Account Balance flows into the **Financial
Statements** by **Account Type**.

## 1. Access & workflow

**General Ledger** menu → **GL History / Account History** → set the **period & account filter** → the
report shows **all journal transactions affecting** that account → a **Print Preview** is available for a
formal report.

## 2. Filter per column

**Every column can be used as a filter** (not just the period), so tracking can be specific. Columns:
**Date, Source Type, Source No., Account No., Account Name, Description, Debit, Credit, Department.**

## 3. Drill-down / trace to source

GL History is **not a static report.** **Double-click** a row → the system **drills down to the source
transaction** that produced the journal.
```
GL History → pick a transaction → double-click → Source Type (e.g. Purchase Invoice) → open its voucher
```
The **Source Type** can be various transactions: Purchase Invoice, Purchase Payment, Sales Invoice, Sales
Receipt, Journal Voucher, cash/bank transactions, etc. **Source No.** = the reference to find the right
source voucher.

## 4. Dimension follows the account's function

- **AR** → may carry **Customer / sub-GL** info.
- **AP** → may carry **Vendor / sub-GL** info.
- **Revenue / Expense** → may carry **Department**.
- **Other GL accounts** → plain GL postings without sub-GL/Department.

> Example (SS): the GL History of **Salaries & Wages Expense** shows a **Department** on each transaction —
> so it can be traced **by account and by Department** at once.
>
> **An AP account's GL History mirrors an AR account's.** Same entry point & format; the only
> difference is a **Vendor** column (instead of **Customer**) as the sub-GL. Reconciliation: **AP control ↔
> total Vendor Sub-GL**.
>
> **An Others account's GL History** (outside AR/AP/Revenue/Expense) also mirrors it, but **without** a
> sub-GL (Customer/Vendor) **or** a Department column — it shows as **plain GL**: Date, Source Type, Source
> No, Account No/Name, Description, Debit, Credit (+ balance). The entry point & drill-down to source stay the same.

## 5. Report purpose

Daily journal tracking · finding the **source of a GL number** · investigating a **discrepancy** · making
sure transactions hit the **correct account** · tracing to the **source voucher** · reviewing by
**Department** / by **Source Type** · a simple **audit trail** GL → source.

## 6. Print Preview (minimum format)

```
Date | Source Type | Source No. | Account No. | Account Name | Description | Debit | Credit | Dept. Name
```
The report also shows the **total Debit & Credit** at the end.

## 7. Relationship with Account Balance & Financial Statements

GL History = the **transaction-level detail**. The accumulation of all postings forms the **Account
Balance**, which then flows into the Financial Statements **by Account Type**:
- **Asset, Liability, Equity** → **Balance Sheet**
- **Revenue, Expense** → **Profit & Loss**

```
Transaction/Voucher → Journal Posting → GL History → Account Balance → Financial Statement
```
> **Account Balance** = the summary of an account's balance from GL postings (can show it **per period**),
> then becomes part of the Financial Statements per Account Type classification.

## 8. Three levels to keep separate (for the accounting engine)

| Level | Content |
|---|---|
| **A. Transaction level** | the **source voucher/transaction** the user creates |
| **B. GL transaction level** | the **journal posting** in GL History, **drillable** to source |
| **C. Account Balance / FS level** | **accumulation** of postings → Balance Sheet / P&L **by Account Type** |

> **Don't mix the three:** GL History = **transaction detail & audit trail**; Account Balance = **balance
> summary**; Balance Sheet / P&L = **financial statements** by account classification.

> **Core:** GL History = a **collection of journal postings per account** — *filterable*, *printable*
> (Print Preview), & *drillable* to source. It is the **detail forming the Account Balance**, and the
> Account Balance → **Balance Sheet / P&L** per Account Type. See also [AR History & Reports](account-history-ar-reports.md).
