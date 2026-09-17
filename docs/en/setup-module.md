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
Global system settings:
- **Default accounts** (e.g. default cash/bank, rounding account, retained earnings).
- Document number formats, number & date formats.
- **Tax settings** (default VAT) & feature toggles.

### 3. User Profile & Access Rights — **the key internal control**
- Create a **user (login)** for each staff member.
- **Access rights per module** (Sales, Purchase, GL, etc.): tick **Create / Edit / Delete**.
- **Specific rights**, e.g. *Print Sales Invoice*, *Change Selling Price*.
- **Control principle:** apply **segregation of duties** — separate whoever **inputs**, **approves**,
  and **holds cash**. Restrict **Delete** & **Change Selling Price** to specific roles (prone to misuse).

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
