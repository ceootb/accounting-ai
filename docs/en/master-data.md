# Master Data (Department, Customer, Vendor, Item)

**Master data** is reference data you **set up once** and then **reuse** across many transactions.
Preparing it neatly up front makes transaction entry fast and reports tidy automatically. The main
masters are: **Chart of Accounts (COA)**, **Department**, **Customer**, **Vendor**, **Item**, and
**Fixed Assets**. COA and Fixed Assets have their own pages; this page covers the other four.

All masters share the **same pattern**: each type is shown as a **list (data grid)** that can be
**filtered per column**, drilled into for detail, and printed. Records can be entered **one by one** or
**imported from a file** when there are many. A record no longer in use is usually **suspended
(deactivated)** rather than deleted — so the **old transaction history stays intact**.

---

## Department

A **Department** is a **unit / cost center** for costing and reporting. Its purpose: so that **cost and
profit can be seen per unit** (e.g. per branch, division, or project), not just one combined
company-wide figure. That's why many transaction screens include a **Department** field — so each cost
or revenue can be tagged to the unit it belongs to.

As a master, a department is simple:
- **Department No. & Name** — the unit's identity.
- **Sub-Department** — a department can be made a **child** of another, forming a **hierarchy** (e.g.
  Division → Sub-division). Useful for tiered reports.
- **Suspended (inactive) status** — a department no longer in use can be **deactivated** so it doesn't
  appear on new entries, while its **old records remain**.

All departments appear in a **list** that can be filtered — for example by **active/inactive status**
— then opened for detail or printed.

> **Bottom line:** a department isn't part of debit-credit accounting itself; it's a **unit tag** that
> lets reports be split by segment. Set it up once, then just pick it on transactions.

---

## Customer

A **Customer** is the master record for a party you sell to. It **links to the Sales Invoice →
Accounts Receivable (AR) → and the AR Sub Ledger** (the subsidiary book per customer). So correct
customer data makes **receivables and aging tidy** by itself.

The information is grouped into a few sections; the most important:
- **Address** — **mandatory** (for billing / shipping).
- **Payment Term** — e.g. 30 days. This is the **basis for computing receivable aging (AR aging)**, so
  it should always be filled in.
- **Currency** — when the customer transacts in a **foreign currency**.
- **Tax** — two settings: **Tax 1 = VAT** and **Tax 2 = withholding tax (PPh)** — so that when an
  invoice is created, the tax is **applied automatically and correctly**. There's also a **tax-included
  price** option. Example: a **foreign** customer usually **isn't charged VAT**, so the tax setting is
  left blank.
- **Customer Type** — grouping for analysis / reporting.

Other sections (Contacts, Notes, Custom Field) are **optional** and often unused.

> **Bottom line:** the parts that truly affect accounting are the **Term** (for aging), **Tax** (VAT &
> withholding), and **Currency**. Set them once, and the customer's invoices and receivables stay
> consistent.

---

## Vendor

A **Vendor** is the master record for a party you **buy** from — the **mirror** of a Customer. It links
to the **Purchase Invoice → Accounts Payable (AP) → and the AP Sub Ledger** (subsidiary book per
vendor). Its content follows the same pattern as Customer: **address** (mandatory), **payment term**,
**tax** (VAT & withholding PPh), and **currency**. Other parts (Contacts, Notes, Custom Field) are
optional.

> **Consistent with Customer:** what affects accounting is still the **Term**, **Tax**, and
> **Currency**. Once correct, purchase invoices and vendor payables stay consistent automatically.

## Term & Tax = reusable masters

**Payment Term** and **Tax** are not retyped for every Customer or Vendor — both are **masters created
once and reused**:
- **Term** — e.g. *COD, Net 14, Net 30*. Created once (a *New Term* option), then just picked for the
  next party. Avoids duplicate terms and keeps consistency (the basis for aging).
- **Tax** — e.g. *VAT* and *withholding PPh (W/H Tax)*. Also a reusable master (a *New Tax* option). A
  party can have more than one **independent** tax setting (e.g. VAT **and** PPh), and these may differ
  between parties.

> **Bottom line:** create the **Term/Tax master once**, then **pick** it on each Customer/Vendor — don't
> recreate it. This keeps data clean and consistent.

---

## Item (Goods, Service, or Expense)

**Not every Item is an inventory good.** An Item is a **representation** of whatever is picked on a
transaction, and its **accounting treatment is set by the Item's function + its default account (COA
mapping)** defined **when the item is created** — not merely by appearing on a transaction. There are
**three kinds**:

**1. Inventory Item** — a good that truly becomes **stock** (e.g. coffee, sugar, merchandise). Default
account = **Inventory**.
```
Purchase:  Dr Inventory | Cr Accounts Payable / Cash
```
When used/sold, inventory follows **costing/COGS** per the system's mechanism.

**2. Revenue Item** — for transactions that **generate income**; **not necessarily** inventory:
- **Made/mixed product** (e.g. *a barista coffee drink*) → default **Revenue – Beverage Sales**. Its
  ingredients (coffee/sugar/milk) are first bought as **inventory**, then the portion used is allocated
  to **Direct Cost / COGS** via **job costing**. See the cost flow: [Processed Product: Cost Flow & Job Costing](processed-product-job-costing.md).
- **Service** (consulting, design, maintenance) → default **Revenue – Service Income**. A service item
  **never** has a purchase transaction (the company doesn't buy the service to resell).
```
Service invoice:  Dr Accounts Receivable | Cr Service Income
```

**3. Expense Item** — linked directly to a specific **expense account** (e.g. *Parking* & *Toll* →
**Parking Expense**). This helps users who don't master the COA.
```
Dr Expense (e.g. Parking Expense) | Cr Cash / Bank
```

### Setting the item once = preventive control

The account mapping on an Item is a **preventive control**: an **admin who understands accounting** sets
it **when the master item is created**. Once correct, the **operational user just picks the Item** → the
system takes the **default account** → **auto-journal**. No manual COA selection per entry.

> **Control concept:** *errors are prevented up front, not repeatedly corrected later.* With correct
> master items from the start, the risk of a wrong account/journal at transaction time drops to nearly
> **zero** — operational users need little accounting knowledge, while control stays at master setup.

> **Changing the mapping:** for an item **already used** in transactions, changing the default account
> must be controlled. If the change **alters the item's accounting nature**, **create a new item** with
> the new mapping — so **old transaction history stays consistent**.

> **How an item drives the auto-journal in transactions** (per item type): see [Items in Transactions: Account Mapping & Auto-Journal](item-transactions-auto-journal.md).
