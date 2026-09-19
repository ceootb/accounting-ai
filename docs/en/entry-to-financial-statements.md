# From Transaction Entry to Financial Statements — A Simple Explanation

> For **users who don't need to be accounting experts**. The goal: to
> understand *how* a single transaction entry turns itself into financial statements. The example
> uses a **Sales Invoice** worth IDR 450,000.
>
> *(Technical terms/logic for building the software are kept separately — used when creating the program.)*

---

## The big picture

Think of a "conveyor belt". The user only places **sales data** at the front; out the back comes
tidy **financial statements**. In between sit 3 automatic machines: the **journal**, the **general
ledger**, then the **reports**. The user doesn't need to know what's inside — they just enter the
right data.

```
Transaction entry  →  Auto journal  →  General Ledger  →  Financial Statements
   (user fills)         (system)         (system)             (system)
```

---

## 1. What the user does: just fill in data

On the Sales Invoice screen, the user only **selects and fills**, never calculates:

- Pick a **Customer** from the list.
- Pull in a **Delivery Order** if there is one, or enter the goods directly.
- Pick the **item**, enter **quantity** and **price**.
- Choose the **receivable account** (what kind of receivable to record it as).

Done. Total, tax, and discount are computed automatically, because each item was already "linked" to
the right account during initial setup. **The user focuses on getting the data right, not on the math.**

---

## 2. First machine: data becomes a journal

The moment the invoice is saved, the system automatically writes the **accounting records**. The
rule is simple: **every record always has two sides that add up to the same amount** (in = out). For
the IDR 450,000 invoice, the system records two things:

**a) The company has the right to collect money (recognizing the sale):**
- **Receivable** (money to be received) increases by **IDR 450,000**.
- Against it: **Sales** is recognized at **IDR 405,406** and **Tax (VAT)** payable at **IDR 44,594**.
  (Because the price already includes tax, the tax is "stripped out" of the total.)

**b) Goods leave the warehouse (recognizing the cost of goods):**
- The **cost of goods sold** is recorded at **IDR 234,000**.
- **Inventory** (stock value) decreases by **IDR 234,000**.

This is the bridge: a *selling activity* instantly becomes a *financial record that always
balances*, without the user calculating or writing anything.

---

## 3. Second machine: the journal flows into the General Ledger

All those records are then "sorted by account" in the **General Ledger**. If the journal is like
*daily receipts*, the General Ledger is like a *bank statement per category*: there's a dedicated
page for Receivables, one for Sales, one for Inventory, and so on. Every time a new transaction
touches an account, its balance is updated here.

So the General Ledger answers: *"How much did we sell this month? How much are our receivables now?"*
— no longer per invoice, but as a total per category.

---

## 4. Third machine: the General Ledger is summarized into Financial Statements

The ending balance of each account is pulled into statements management can read:

- **Sales** and **Cost of goods sold** roll up into the **Income Statement** → the difference = **profit**.
- **Receivables** and **Inventory** appear as **assets** in the **Balance Sheet**; **unpaid tax**
  appears as a **liability**.
- The **profit** from the Income Statement then adds to the company's **equity** in the Balance Sheet.

All of this happens automatically. The manager just reads the results to make decisions.

---

## In one breath

> **The user only needs to enter correct sales data. The system does the journaling, summarizes it
> into the General Ledger, then builds the Financial Statements.** That's why staff don't have to be
> accounting experts — they just need to be careful with the data. The one who **must understand
> accounting is the manager/supervisor**, so they can read the statements, judge whether the numbers
> make sense, and make decisions.
