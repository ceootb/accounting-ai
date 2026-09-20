# Tips: VAT Setup on Purchases & Splitting the PI Across Periods

> Two practical points about **VAT** on purchases: (1) where the VAT setup comes from, and (2) the
> trick of **splitting one Purchase Invoice (PI) into two** when the **VAT period differs** from the
> expense period.

---

## 1. Where does the VAT setup come from?

VAT is **not** retyped on each invoice — it comes from the **vendor master**. In the vendor profile
(*Terms, etc.* tab) there is a **Taxes** section:
- **Tax 1: VAT** and **Tax 2: W/H TAX** (withholding),
- a **Default Invoice is Tax Included** option,
- **Vendor's Tax No.**, **PKP No.**, and **Tax Type**.

Because the vendor is already set as **taxable**, when you create a Purchase Invoice the **Vendor is
Taxable** box is on and the **Tax** column on each line shows **T** → the system computes **Input VAT**
automatically. Payment terms (e.g. Net 14, Net 30, C.O.D) also come from the vendor master.

---

## 2. Trick: Split into 2 PIs when the VAT period ≠ the expense period

**Problem:** sometimes the **expense/goods** belong to one month, but the vendor's **tax invoice
(VAT)** is only issued the next month. Example: **goods received & expense belong to July**, but the
**tax invoice is issued in August**. Putting them in one PI means one of them lands in the wrong
period — either the expense slips, or the VAT jumps ahead.

**Solution — split into 2 Purchase Invoices:**

**PI-A — base/expense only** (in the expense period, e.g. July). Entered via the **item/expense
account**, no VAT.
```
PI-A (July) — base IDR 8,887,500
Dr  Expense / Inventory            8,887,500
    Cr  Accounts Payable               8,887,500
```

**PI-B — VAT only** (in the tax-invoice period, e.g. August). Entered via the **Expense tab** straight
to the **Input VAT** account.
```
PI-B (August) — VAT IDR 977,625
Dr  Input VAT                        977,625
    Cr  Accounts Payable                 977,625
```

**At payment (Purchase Payment):** open the payment to that vendor and **tick both PI vouchers**
(PI-A + PI-B) to pay them together.
```
Dr  Accounts Payable (PI-A)        8,887,500
Dr  Accounts Payable (PI-B)          977,625
    Cr  Cash/Bank                       9,865,125
```

**Why split?**
- The **expense** is recognized **in the period it occurred** (matching principle) → that month's
  profit is correct.
- **Input VAT** is credited **in the tax-invoice's tax period** (VAT rule: input VAT is credited by
  the tax-invoice date) → it matches the periodic VAT return, no month mismatch.

> **Bottom line:** if the tax-invoice date falls in a different month from the expense, **separate the
> base and the VAT into two PIs** so both the books (expense) and the tax (VAT) land in the right
> period. At settlement, both PIs are paid together.

---

*VAT setup on the **Sales Invoice** works similarly (from the customer master) — covered separately.*
