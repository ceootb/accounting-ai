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
