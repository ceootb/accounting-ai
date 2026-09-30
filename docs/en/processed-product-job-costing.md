# Processed Product (Manufactured): Cost Flow & Job Costing

This page explains the **cost flow** for a **processed product** — a product made from several
materials, then sold. Example: **Items A, B, C** (materials) are processed into **Product D**.

## Scenario

- **Items A, B, C** are **materials** that are: bought to be **held as inventory**, have a **quantity &
  inventory value**, and are **used** as inputs to produce **Product D**.
- **Product D** is the **processed/manufactured output**, later **sold** to a customer.

## Accounting flow

**1. Buying materials** — Items A/B/C are bought and enter inventory:
```
Dr  Inventory
Dr  Input VAT              (if applicable)
    Cr  Accounts Payable
```
> No COGS yet — the goods haven't been used/sold.

**2. Using materials to make Product D** — materials leave inventory into Job Costing/production:
```
Dr  Direct Cost / Job Cost
    Cr  Inventory
```
> The cost of Items A/B/C accumulates as Product D's cost. The quantity & value of A/B/C inventory
> **decrease** by what was used.

**3. Job Costing result** — accumulates the material cost for Product D. Example:

| Material | Cost |
|---|---|
| Item A | 10,000 |
| Item B | 20,000 |
| Item C | 15,000 |
| **Total Direct Cost of Product D** | **45,000** |

> Job Costing shows Product D costs **45,000** from materials A+B+C. If there are other relevant **direct
> costs**, they can be added to Job Costing per the transaction flow.

**4. Product D is sold** — say a selling price of **70,000**:
```
Dr  Accounts Receivable / Cash   70,000
    Cr  Sales Revenue             70,000
Dr  COGS / Cost of Sales         45,000
    Cr  related cost/product account  45,000
```

## Core logic

> **Items A/B/C** → *Inventory Part* → **purchase enters Inventory** → **materials used** → **Job Costing
> accumulates Direct Cost** → yields **Product D's cost** → **Product D sold** → the related cost becomes
> **COGS / Cost of Sales**.

## Key principle (where the cost sits)

| Material state | Account |
|---|---|
| **Still owned** | **Inventory** |
| **Already used** to produce a product/job | **Direct Cost / Production Cost** |
| **Product/job sold** & cost recognized | **COGS / Cost of Sales** |

> **Watch out (don't assume):**
> - don't immediately treat **all** goods used in work as *Non-Inventory*;
> - **Direct Cost is not always the same** as the COGS account;
> - **Job Costing is not just a report** — it's part of the *cost flow* linking material usage to the
>   product/job produced.
>
> Make sure **every cost movement balances** (debit = credit) and there is **no double counting**.
