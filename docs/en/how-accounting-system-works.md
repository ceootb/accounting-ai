# How an Accounting System Is Set Up & Works (for Users & Companies)

> A practical guide: **how accounting software is prepared and operates**, so a company can be
> run even by **junior / fresh-graduate** accounting staff — just enter a **voucher**, and the
> **journal is generated automatically (auto-journal)**. Debit/credit complexity is "hidden"
> behind the voucher, so there is no need to hire a senior accountant just for daily operations.
>
> Curated by a practicing accountant (20+ years, Indonesian accounting).

---

## Part 1 — Initial Setup

Order of preparing accounting software for a new company:

### Step 1 — Preparation
Details & order to follow (to be completed).

### Step 2 — Prepare Master Data
Set up master lists **before** any transaction is possible. Example lists:
- **Chart of Accounts (COA)**
- **Customer list**
- **Vendor list**
- **Department list** — for *costing*: **Business Unit** vs **Cost Center**
- **Item list** — *inventory part* / *non-inventory part* / *service*
- **Fixed Assets**
- (more to follow)

### Step 3 — Opening Balance
- Needed **only if migrating data** — the company already has legacy accounting software.
- If the company is **new / has no data** → **no opening balance** needed.

### Step 4 — Tax Setup
- **VAT (PPN) 11%**.
- **Withholding (PPh)** → depends on the **type of expense** and the **taxpayer (WP) type**.

---

## Part 2 — Principle: The 5 Ledgers (Books)

Following basic accounting principles & practice, the software is organized around **5 books**
(applies to both **trading and service** companies). Each book produces an **auto-journal**.

### 1. Purchase Book
Records purchases of goods / expenses; **recognizes payables**.
Auto-journal (depends on item setup):
```
Dr  Inventory / Expense
    Cr  Accounts Payable / Accrued Expense
```

### 2. Sales Book
Records sales of goods / services; **recognizes receivables** (+ COGS & inventory reduction for goods).
Auto-journal:
```
Dr  Accounts Receivable
    Cr  Sales / Service Revenue
```
*(for trading goods, add: `Dr COGS | Cr Inventory`)*

### 3. Cash/Bank Disbursement Book
Records payment of payables for purchases / expenses.
Auto-journal:
```
Dr  Accounts Payable / Accrued Expense
    Cr  Cash / Bank
```

### 4. Cash/Bank Receipt Book
Records collection of receivables from sales of goods / services.
Auto-journal:
```
Dr  Cash / Bank
    Cr  Accounts Receivable
```
If it is a **sales advance / down payment** (e.g. a property company — unit DP before deed):
```
Dr  Cash / Bank
    Cr  Sales Advance (Unearned)
```

### 5. Journal Voucher
For transactions **outside the 4 books above**. Mostly **expense accruals**.
> Important: **revenue must not be accrued** — it would contradict the sales report.

Manual, but can be **recurring** for monthly transactions. Example (office rent accrual):
```
Dr  Office Rent Expense
    Cr  Accrued Expense
```

---

## Philosophy

With the flow **enter voucher → auto-journal → posting**, a company **does not need a senior
accountant** for daily operations; an **SMA / fresh-graduate** accountant can operate it.
Debit/credit complexity is handled by the system via master setup (items, COA, tax) configured
once at the start.
