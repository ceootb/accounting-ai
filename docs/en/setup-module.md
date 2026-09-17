# Setup / Initial Preparation Module (Step 1)

> Initial configuration under the **Setup** menu before the company starts transacting. This
> completes **Step 1 (Preparation)** in [how-accounting-system-works.md](how-accounting-system-works.md).
> *(Framework; per-menu field details to follow.)*

---

## Setup Menu Contents

### 1. Company Info
Has several **tabs**: **General · Accounting Period · Tax · Branch ID**.

**a) General tab** — basic identity:
- Company Name, Address, Zip Code, Phone, Fax, Country.
- **Default Currency** (e.g. IDR).

**b) Accounting Period tab** — **period control (important):**
- **Start Date** — the date the company starts operating/bookkeeping.
- **Fiscal Year** — the accounting year.
- **Default Period** — the **current period**.
- **Warn if** — *N* months **before / after** the Default Period → shows a **warning**.
- **Error if** — *N* months **before / after** → **blocks/locks** entry (error).
- **Locking Period:** prevents users from entering data carelessly — e.g. after the FS are **closed**,
  or posting to a **future period** without a clear document/reason. Future data is usually only for
  **recurring** transactions.

**c) Tax tab** — tax data:
- Form Serial Number, **Tax Registration Number (NPWP)**, **Taxable Company's No.** (PKP no.),
  Taxable Company's Date, Branch Code, Type, **KLU** (business field classification).

### 2. Preferences
**Global system settings** + the **default accounts** used to auto-post journals. Split into several
sub-menus. **Core idea:** before any transaction can run, each transaction type must be mapped to a
**default account** in the COA — this is what makes journals form automatically. *(Account numbers
below are illustrative COA-mapping examples only.)*

**a) Company** — app behavior: *Backup on close*, *Confirm before exit*, *Open last company*,
*Show purchase & sales price in item history*.
- **Retained Earning Account** (e.g. `3200001`): the account that closing profit/loss rolls into
  each period. **Required.**

**b) Feature** — enables data structures & methods:
- **Inventory Costing Method**: **FIFO** or Average — how inventory COGS is computed.
- Toggles: *Multi Warehouse*, *Quantity can < 0*, **Multi Unit**, *Use Salesman*, *Can Edit Invoice
  Number*, *Control Qty Measurement*.
- **Cost & Profit Center**: **Multi Department** / **Multi Project** — so cost & profit can be
  reported per department/project.
- **Audit Trail**: **Transaction Log** (who created/edited — internal control) & Recalculating Cost Log.

**c) Currency Default Account** — default accounts **per currency** (e.g. IDR):
- *Account Payable*, *Account Receivable*, *Advance Purchase*, *Advance Sales*, *Sales Discount*,
  *Realized Gain/Loss* & *Unrealized Gain/Loss* (FX differences).

**d) Item Default Account** — defaults for **inventory/item** transactions:
- *Inventory*, *Sales*, *Sales Return*, *Item Discount*, *Goods In Transit*, **COGS**,
  *Purchase Return*, *Expense*, *Unbilled Goods* (received not yet billed).

**e) Purchases** — purchasing module behavior:
- *Remember Vendor*, warning when buying a Serial Number item already bought.
- **Purchase Return**: *All Purchase Invoices* / *Outstanding Invoices*.
- **Receive Item → Default Receive Cost**: *Reupdate by bill* / *Do not reupdate* / *Set to reupdate
  by bill if the first bill date falls in the same period as the receive date*.
- **Default Difference Unbilled Account**: absorbs the received-vs-billed difference.

**f) Cost & Profit Center** — defaults for **projects & departments**:
- Warning when **Department** is not filled.
- **Labour Cost** (Expense Account) and project accounts: *Project In Process*, *Advanced Revenue*,
  *Revenue*, *Cost of Project Sold*.

**g) Job Costing** — *Save different cost to account* option + its holding account.

**h) Taxation** — tax settings:
- *Code in Invoice Tax No*, *Number for each invoice*, **Rounded (Upper)** rounding.
- **Income Tax Account** (e.g. `7300000` — Corporate Income Tax).

**i) Reminder** — startup reminders: *Item to Reorder*, *Expired Serial Number*, **Receivable due**
& **Payable due** (e.g. 7 days before due date), discount due, and **Recurring** transactions
(Sales/Purchase Invoice, Payment, Deposit).

**j) Templates Setting** — print copies (e.g. **VAT Invoice Copies**).

**k) Miscellaneous** — *Auto pop-up search*, **Invoice Aging** (Aging Range e.g. 30 days; computed
from **Due Date** or **Invoice Date**), **Language** (English/Indonesia), **Date Format**
(e.g. `dd mmm yy`) & number format.

**l) Font Setting & Skin Option** — font size/name & appearance (cosmetic).

### 3. User Profile & Access Rights — **the key internal control**

The **Edit User** screen manages login identity + per-user access rights.

**a) Header (user identity):**
- **Login Name**, **Full Name**, **Password** + **Confirmation**.
- **Level** (dropdown): **Admin · Supervisor · User** — access-level presets. Admin usually has all
  rights ticked; User is empty by default (must be granted rights as needed).
- Buttons: **New**, **Save**, **Delete**, **Close**, and **Get Privilege**.

**b) Get Privilege** — when creating a new user this button turns on automatically. It **copies the
access rights of an existing user** to the new one, so you don't have to tick everything manually.

**c) Access rights per activity — 6 permission columns:**
Each activity row can be ticked under: **Create · Edit · Delete · Report · View · List**.
Rights are grouped into **module tabs**:
- **Sales:** Sales Quotation, Sales Order, Delivery Order, Invoicing, Customer Receipt, Sales Return,
  RMA. Special rights: *Print Sales Invoice*, **Change Selling Price**, *Commission*, *AR Reminder*,
  *Change Customer Info in Invoice*, *Allow over limit*, *Allow over qty in Invoice*, *Reprint
  Delivery & Invoice*.
- **Purchase:** Purchase Requisition, Purchase Order, Receive Item, Purchasing, Vendor Payment,
  Purchase Return + *AP Reminder*.
- **Item & Inventory:** Item, Warehouse, Item Transfer, Grouping, Job Costing, Inventory Adjustment,
  Selling Price Adjustment + *Change Item Account*, *Create/Enter Serial/Batch Number*.
- **Project:** Labour Cost (+ Adjustment), Material Budget & Price Adjustment, Work Price Analysis,
  Project, Material In Used, Project Survey, Project Ending + *Show RAB*, *Project Control*,
  *Project Expense Payment*.
- **General Ledger & Others:** Chart of Account, Journal Voucher, Budgeting, Customer Data, Vendor
  Data, Financial Report, Tax Report, Department + *Export Data* / *Import Data*.
- **Bank & Fixed Asset:** Other Payment, Other Deposit, Fixed Asset + *Bank Reconciliation*,
  *Revaluate/Dispose Fixed Asset*, *View & print bank book*.
- **Memorized Reports · Designed Reports · Memorized Transaction** (separate tabs).

**d) Control principle:** apply **segregation of duties** — separate whoever **inputs**, **approves**,
and **holds cash**. Restrict **Delete** & **Change Selling Price** to specific roles (most prone to
misuse). Avoid giving every user the **Admin** level.

### 4. Change Password
Periodic password change — account access security.

### 5. Quick Setup
A **guided initial setup wizard** (COA, balances, etc.) for a new company.

### 6. Form Templates
**Document print templates** (Invoice, PO, Receipt) — logo, layout, columns.

---

## Link to the Preparation Steps

`Setup Menu (Step 1)` → then **Step 2 Master Data** (COA, customers, vendors, items, assets) →
**Step 3 Opening Balance** (if migrating) → **Step 4 Tax Setup** (VAT 11%, withholding per taxpayer type).

---

## Internal Control Points (important)

- **Access rights = the main control.** Restrict Create/Edit/Delete by role.
- **Delete** & **change selling price** are the riskiest → restrict tightly + require approval.
- **Segregation of duties:** **input ≠ approve ≠ cash holder** to prevent fraud.
