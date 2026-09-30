# Processed Product (Manufactured): PSAK vs Company Practice

A **processed/manufactured product** (materials → finished product → sold) can be recorded under **two
different treatments**. **Before answering, identify the context first:**

1. **PSAK / ideal accounting treatment**; or
2. A specific company's **practical accounting treatment**.

> **Do not mix** the two versions. Don't treat a company's practical *shortcut* as a PSAK principle. If
> asked for a **comparison**, show **both, clearly labeled**.

---

## Version A — PSAK / Ideal (with Inventory & Job Costing)

Materials = **Inventory Part** (quantity & inventory value tracked).

**1. Buy materials** → enter inventory:
```
Dr  Inventory
Dr  Input VAT              (if applicable)
    Cr  Accounts Payable
```
**2. Materials used** to make Product D → leave inventory:
```
Dr  Direct Cost / Job Cost
    Cr  Inventory
```
**3. Job Costing** accumulates material cost (e.g. A 10,000 + B 20,000 + C 15,000 = **45,000**).
**4. Product D sold** (e.g. 70,000):
```
Dr  Accounts Receivable / Cash   70,000
    Cr  Sales Revenue             70,000
Dr  COGS / Cost of Sales         45,000
    Cr  related cost/product account  45,000
```
> **Cost position:** material owned → **Inventory**; used → **Direct/Production Cost**; product sold →
> **COGS/Cost of Sales**.

---

## Version B — Company Accounting Practice (no inventory tracking)

The treatment of a company that **does NOT track inventory** for the materials (e.g. *training/practice
supply*). Materials = **Non-Inventory Part**.

**1. Buy materials** → **expensed directly** as Direct Cost (not an inventory asset):
```
Dr  Direct Cost / Training Supply
Dr  Input VAT              (if applicable)
    Cr  Accounts Payable
```
**2. Materials used** to make Product D → **no** inventory-issue journal
(`Dr Direct Cost | Cr Inventory` is **not** made), because no inventory asset was recorded. *Job Costing
(if used) only traces cost — not a reason to book the same cost twice.*
**3. Product D sold** (e.g. 70,000):
```
Dr  Accounts Receivable / Cash   70,000
    Cr  Sales Revenue             70,000
    Cr  Output VAT                (if applicable)
```
> **Important:** selling Product D does **not** automatically mean `Dr COGS | Cr Inventory` — because the
> materials were **never** recorded as inventory. The material cost was **already recognized at purchase**
> as Direct Cost / Training Supply per the company's policy.

**Example:** buy A 10,000 + B 20,000 + C 15,000 → `Dr Direct Cost/Training Supply 45,000 | Cr AP
45,000`. Product D is tagged as a sales item; **no** inventory-consumption journal. Sold for 70,000 →
`Dr Receivable 70,000 | Cr Sales Revenue 70,000`. The A+B+C cost remains the Direct Cost already booked.

---

## Comparison

| | **A. PSAK / Ideal** | **B. Company Practice** |
|---|---|---|
| Material Item Type | **Inventory Part** | **Non-Inventory Part** |
| At purchase | enters **Inventory** | **directly Direct Cost** (expensed) |
| At production | `Dr Direct Cost \| Cr Inventory` | **no** inventory journal |
| Cost recognized | when **sold** (as COGS) | when **bought** (Direct Cost) |
| When sold | Revenue **&** `Dr COGS \| Cr Inventory` | **Revenue only** (no inventory COGS) |

> **Don't generalize:** *"a processed product always uses Non-Inventory"* is **wrong**. Version B applies
> **only** because that company doesn't track inventory and expenses cost at purchase — **different** from
> the PSAK version. Ensure **no double counting** in either version.

> **Knowledge priority:** asked for the **PSAK** treatment → use **Version A**; asked for **this
> company's practice** → use **Version B**; asked for a **comparison** → show **both, labeled**.
