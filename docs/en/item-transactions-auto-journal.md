# Items in Transactions: Account Mapping & Auto-Journal (by Item Type)

A **Master Item** with correct account mapping can be used in both the **purchase and sales cycles**,
and the system builds the **journal automatically** based on the **item type + mapped accounts**. The
principle:

> **Correct item → correct mapping → correct auto-journal.** The operational user just picks the item;
> they don't manually choose the Inventory/COGS/Expense account on each transaction.

*(Account names below are **generic** — map them to the company's COA; what matters is the function.)*

## 1. Inventory Part (stocked goods)

Bought → goes to **Inventory**; sold → **Revenue** + inventory release to **COGS**. One item, two cycles.

**Purchase (Purchase Invoice):**
```
Dr  Inventory
Dr  Input VAT              (if any)
    Cr  Accounts Payable
```
**Sale (Sales Invoice):**
```
Dr  Accounts Receivable
    Cr  Revenue
    Cr  Output VAT          (if any)
Dr  COGS
    Cr  Inventory
```

## 2. Non-Inventory Part (not stocked → straight to expense)

A Non-Inventory Part is **not** recorded as inventory. Its mapped account = an **Expense Account**. When
bought, the value is **expensed directly**, not turned into an inventory asset.

**Purchase (Purchase Invoice):**
```
Dr  Expense (the item's expense account)
Dr  Input VAT              (if any)
    Cr  Accounts Payable
```
> **Non-Inventory Part ≠ Inventory Part.** Don't apply the inventory journal to a non-inventory item —
> its purchase goes **straight to expense**, not through an inventory asset.

## 3. Service (service → revenue)

A Service Item = **selling a service**, not inventory. Its mapped account = a **Revenue (Sales)
Account**.

**Sale (Sales Invoice):**
```
Dr  Accounts Receivable
    Cr  Service Revenue
    Cr  Output VAT          (if any)
```
A **discount** (if recorded separately) is treated as a **reduction of revenue** (contra-revenue, on
the **Debit** side) per **PSAK 72**. If the price is already recorded **net**, **no** separate discount
journal is needed.

## Principle & distinguishing error types

Because the treatment is prepared in the master item, routine transactions are safe. If a journal looks
wrong, distinguish the **source**:

| Symptom | Source of error |
|---|---|
| The user picked the wrong item | **Human input error** (not a system fault) |
| The item mapping was wrong since setup | **Master-data / setup error** |
| The journal doesn't match the mapping/rules | **Accounting engine / system error** |

> **Bottom line:** *the item type determines the mapped account, and that account determines the
> auto-journal on purchase/sale.* Accounting control lives in the **master item** — not on the
> transaction screen.
