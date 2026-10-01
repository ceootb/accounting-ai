# Per-Account Transaction History & Receivable (AR / Customer) Reports

Once transactions are recorded, the two things needed most often are: **reviewing each account's
transaction history**, and **pulling reports** (especially receivables/AR). This page covers both,
plus the **Sub Ledger** concept that keeps receivable/payable control clean.

## 1. Account History — a transaction recap per account

Every COA account has an **Account History**: a list of all transactions that ever touched that
account. It's a **filterable table (data grid)** — for example by date — with information columns and a
filter panel.

Its purpose: when you want the **recap of transactions for one specific account**, this is where it
lives — no need to open vouchers one by one. This view **works the same for every COA account**, and
can show **Sub Ledger** detail (see section 4).

## 2. From history to reports

From the ledger history, the system leads into a set of **reports** arranged on two levels: **Report
Category** (a group of reports) and **Report Detail** (the specific report within it). So each group of
transactions has its own report, ready to open by category and by detail.

## 3. The AR & Customer reports you'll use most

- **Outstanding Invoices** — a list of **Sales Invoices that are still unpaid, only**. It shows the
  remaining balance per invoice — quick for seeing who hasn't paid.
- **Aging Receivable Summary** — a summary of **receivable aging** per customer (grouped by how long
  overdue), shown compactly.
- **Aging Receivable Detail** — the same aging, down to each transaction.
- **AR Sub Ledger Detail** — a recap of the **full receivable movement per customer**, i.e.:

  > **Opening balance + Sales Invoice − Sales Receipt − Sales Return − Down Payment
  > + Journal Voucher = Ending balance.**

  The difference from *Outstanding Invoices*: the Sub Ledger Detail shows **all** the movements that
  form the receivable balance, whereas Outstanding Invoices shows **only unpaid invoices**.

All of these can be **exported to PDF or Excel**. From a report, a row can be **traced back to its
source** — from the summary down to the detail, then to the original voucher (for example, a row that
came from a Sales Invoice opens that Sales Invoice's detail).

## 4. Sub Ledger (Sub GL) on AR & AP — why it matters

A **Sub Ledger** is a **subsidiary book per customer / supplier** under a single control account. The
benefit is large: you only need **one Accounts Receivable (AR) account** and **one Accounts Payable
(AP) account**, while the per-party detail is held by the Sub Ledger.

Without a Sub Ledger, people are tempted to create many separate accounts — *AR Store ABC*, *AR Store
XYZ*, and so on — bloating the COA. With a Sub Ledger, **one AR account is enough**, yet per-customer
control stays detailed. The same concept applies on the **AP side (per supplier)**.

> **Bottom line:** one control account + a detailed Sub Ledger = a lean COA with clear per-party
> control of receivables and payables.

## 5. GL History — the dimension follows the account's function

Every **posted** transaction forms a **journal**, which is recapped into the **General Ledger (GL) per
account**. **GL History** shows the **per-account movement** from all transactions touching it — with
**Date, Reference, Description, Debit, Credit, and Running balance** — and stays traceable back to the
**journal → its source transaction**.

> **Its main purpose:** *daily journal tracking* and helping **trace when a discrepancy is found** — GL
> History is essentially a **collection of journal entries shown per GL account**. Full workflow (filter, drill-down, Print Preview, Account Balance→statements): [General Ledger History](gl-history.md).

The key: **don't force every account into the same structure.** Extra columns/dimensions **follow the
account's accounting function**:

| Account type | Required dimension | Purpose |
|---|---|---|
| **Receivable (AR)** | **Sub Ledger per Customer** | per-customer detail & balance; reconcile **AR control ↔ total Sub-GL** |
| **Payable (AP)** | **Sub Ledger per Vendor** | per-vendor detail & balance; reconcile **AP control ↔ total Sub-GL** |
| **Revenue** | **Department** | *Revenue by Department* → **P&L per Department** |
| **Expense/Cost** | **Department** | *Expense by Department* → **P&L per Department** |
| **Other accounts** | — (plain GL) | not forced to have Sub-GL/Department if the function doesn't need it |

> **The principle:** the dimension follows the **accounting purpose**, not uniformity — AR/AP → **Sub
> Ledger**; Revenue/Expense → **Department**; other accounts → **plain GL**. The report **always pulls
> from the same journal/GL engine** (it must not produce a different balance). The result: a simple
> display up front, with correct structure and traceability behind.
