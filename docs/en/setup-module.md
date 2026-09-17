# Setup / Initial Preparation Module (Step 1)

> Initial configuration under the **Setup** menu before the company starts transacting. This
> completes **Step 1 (Preparation)** in [how-accounting-system-works.md](how-accounting-system-works.md).
> *(Framework; per-menu field details to follow.)*

---

## Setup Menu Contents

### 1. Company Info
Company identity & base parameters:
- Name, address, **Tax ID (NPWP)**, logo.
- **Fiscal year / period** (start date).
- Base **currency**.

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
