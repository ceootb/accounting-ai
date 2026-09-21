# Tips: Recurring (Automatic Repeating Transactions)

> **Recurring** = a feature to create **routine/repeating vouchers** periodically (monthly,
> quarterly) without retyping them each period. **A time-saving tip** — instead of entering them one by
> one. It works for **Sales Invoices, Purchase Invoices, and Journal Vouchers**.

**Example uses:**
- **Sales Invoice** → a **monthly commission** billing to a customer.
- **Purchase Invoice** → routine bills: **water, electricity, phone**, rent, etc.
- **Journal Voucher** → routine adjustments, e.g. a **tax allowance on employee income tax (PPh 21)**.

---

## Prerequisite: extend the Accounting Period first

Recurring will **create journals in future periods**. So **before** you start, open **Company Info →
Accounting Period** and **extend the period limit to at least 12 months after the current period**
(the *Warn if* / *Error if* fields). Otherwise the system will reject (error) entries outside the
allowed period range.

---

## How to create it (start from the master voucher)

> Recurring **starts from the voucher itself**, not from the List Recurring menu (the **New** button
> there is disabled).

1. **Enter a master voucher** (e.g. one ordinary Sales Invoice) and **Save**.
2. Click the **Recurring** button on that voucher → the screen switches to **New Recurring**.
3. Fill in:
   - **Recurring Period** → pick from the dropdown: **Monthly / Quarterly**.
   - **Number of Times** → how many to create (e.g. `4` → creates 4 future vouchers).
   - **Reference** & **Description**.
   - The system **auto-fills the grid** with a date per period (rows 1, 2, 3, …).
4. Tick **Assign Form/Invoice Number**, then click the **Start from** field (just place the cursor) →
   the invoice numbers **fill in automatically following the sequence** from the master voucher.
5. Click **Save** → you land in the **List Recurring**.

**Executed column:** a **checkmark** means that voucher has **actually been entered & saved**. The
**first** voucher (from the master) is auto-executed. Future-period vouchers not yet due are still
**accrual** (often shown on screen with a small *placeholder* value until they're actually created as
real vouchers).

---

## How to execute the next vouchers

The 2nd voucher onward is created one at a time as its period arrives:

1. In the **List Recurring**, **double-click** the recurring row (highlighted blue).
2. **Right-click** a row that is **not yet** executed → choose **Create Invoice**.
3. The screen switches to the **Sales Invoice** (data pre-filled from the master) → check → **Save**.
4. Back on the recurring screen → click **Refresh** → a **checkmark** appears in the **Executed**
   column (the voucher was created & saved).
5. **Repeat** for the next period (Create Invoice → Save → Refresh) until **all** are executed →
   **Save & Close**.

---

## Bottom line

> **Recurring = "auto re-print" of routine vouchers.** Make the master once → set the period & count
> → the system prepares a voucher for each period; you just *Create Invoice* when the time comes. It
> saves time for bills/costs/adjustments that are **the same every month**, and helps with **cost
> control & cash-flow estimation** ahead. *(This is an efficiency tip, not a new accounting rule — the
> journal produced is the same as an ordinary voucher.)*
