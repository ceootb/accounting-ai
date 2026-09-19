# Fixed Asset Module

> The module for recording **fixed assets** (buildings, vehicles, machines, computers, etc.),
> computing **depreciation automatically each month**, and creating **its own journals**. Plain
> language for users; technical detail is kept for the software-build stage.

---

## Overview: 3 sub-modules (general → specific)

```
1. Fiscal Fixed Asset Type  → the "tax group" (benchmark useful life & fiscal depreciation rate)
2. Fixed Asset Type         → the company's asset categories, linked to the tax group above
3. Fixed Asset List         → the actual assets purchased (per-asset data entry)
```
The first two are **initial setup** (done once). The third is filled every time a new asset is bought.

---

## 1. Fiscal Fixed Asset Type — the tax group

A list of **depreciation groups per tax rules**. Each group has a **depreciation method**, an
**estimated life (years)**, and a **rate % (computed automatically from the life)**. E.g. a 20-year
life → straight-line rate **5%** (100% ÷ 20).

> ⚠️ **Important — align with the latest tax rules.** The **correct** Indonesian fiscal groups
> (Income Tax Law Art. 11 & PMK 72/2023):
>
> | Group | Useful life | Straight-line | Declining balance |
> |---|---|---|---|
> | **Non-building — Group 1** | 4 years | 25% | 50% |
> | **Group 2** | 8 years | 12.5% | 25% |
> | **Group 3** | 16 years | 6.25% | 12.5% |
> | **Group 4** | **20 years** | **5%** | 10% |
> | **Permanent Building** | 20 years | 5% | — (straight-line only) |
> | **Non-permanent Building** | 10 years | 10% | — |
>
> So **Group 4 = 20 years (5%)**, *not* 32 years. Make sure the table in the system follows these figures.

Available **depreciation methods**: **Non Depreciable** (e.g. Land), **Straight Line**, and
**Declining** balance.

---

## 2. Fixed Asset Type — the company's asset categories

Links the **company's asset categories** (e.g. Building, Vehicle, Computer, Machinery, Land) to the
**tax group** above. Once the tax group is chosen, the life/method/rate fields fill in **automatically
(greyed out)** from that group. E.g. *Computer* → Group 1 → straight-line, 4 years, 25%.

---

## 3. Fixed Asset List — entering the assets purchased

Every asset bought is registered here. All entries form the complete **asset register**.

**Header:** Asset Code, **Asset Type** (dropdown, from the Fixed Asset Type list), Acquisition Date,
Usage Date, Asset Description, quantity, **Department** (dropdown).

**General tab** (the main one):
- **Estimated Life** — life (years & months), entered manually.
- **Depreciation Method** — pick from the dropdown (straight-line, declining, sum-of-years-digits, or
  non-depreciable). **Rate** fills in automatically from life + method.
- **Asset Account** — the asset account in the COA (e.g. Building).
- **Accumulated Depreciation Account** — the accumulated-depreciation account in the COA.
- **Depreciation Expense Account** — the depreciation-expense account in the COA.
- **Fiscal Fixed Asset** — tick if this asset follows fiscal rules.

**Expenditures tab:** records the **acquisition cost**, which comes in via the intermediary account
**"Fixed Asset Transaction"** (see auto-journal below). *(The Notes tab is ignored.)*

> The **Dispose** (asset disposal) & **Revaluation** buttons are here, **covered separately**.

---

## Auto-journal — 3 stages

**Stage 1 — Buy the asset (via Purchase Invoice):** the value first lands in an **intermediary account**.
```
Dr  Fixed Asset Transaction (intermediary)
    Cr  Cash/Bank or Accounts Payable
```

**Stage 2 — Register the asset in the Fixed Asset List:** the value moves from the intermediary to the
asset account.
```
Dr  Fixed Asset (e.g. Building)
    Cr  Fixed Asset Transaction (intermediary)
```
> The **Fixed Asset Transaction** account is the "bridge" between the purchase and the asset
> registration. After both stages, this intermediary balance returns to **zero** (in then out).

**Stage 3 — Monthly depreciation (automatic, via [Period End](period-end-closing-process.md)):**
```
Dr  Depreciation Expense
    Cr  Accumulated Depreciation
```
> Just **click the "Period End" button** at monthly closing — the system **computes & journals
> depreciation for all assets at once** (one voucher, detailed per asset & per department). The user
> does no manual math.

**Numeric example:** a building of IDR 1,200,000,000, 20-year life (straight-line 5%/year) →
depreciation IDR 60,000,000/year = **IDR 5,000,000/month**:
```
Dr  Depreciation Expense - Building     5,000,000
    Cr  Accumulated Depreciation - Building   5,000,000
```

---

## Bottom line

> **Set up once** (tax group → asset category), then **register each asset** with its COA accounts.
> The system handles the rest: the purchase via an intermediary account, then **monthly depreciation
> automatically with a single "Period End" click**. Users never compute depreciation manually, and the
> figures stay consistent all the way to the General Ledger & Financial Statements.
