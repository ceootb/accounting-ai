# Tips: Cash in Transit (CIT) for Aggregating Retail Sales

> A **time-saving trick** for businesses with **very many, low-value retail transactions** (e.g.
> cafés & restaurants). Instead of entering each sale one by one every day (a waste of time, and each
> transaction is immaterial), daily receipts are **parked** in a **Cash in Transit (CIT)** account,
> then **aggregated** into **one Sales Invoice** at month-end for tax reporting.
>
> ⚠️ **Honest note:** the CIT technique is **purely a practical time-saving workflow — not part of
> standard accounting theory.** Its goal is entry efficiency while keeping sales & VAT figures correct
> for tax.

---

## Account setup & its control

- **The CIT account is registered in the COA as a Cash/Bank-type account.** It holds money "in
  transit" from retail receipts before it becomes formal sales.
- **Mandatory control: at every month-end the CIT balance must be ZERO.** If it isn't zero, some
  receipts haven't been aggregated into a Sales Invoice, or there's a mismatch with the POS report —
  it must be investigated before closing. A zero CIT balance at month-end is the **sign that all
  retail receipts have been booked correctly**.

---

## The flow

**1. Daily — park receipts into CIT (via a Journal Voucher).**
Each day, the total café/resto receipts (all of that day's transactions combined) that land in the
bank are recorded with a JV:
```
Dr  Bank                         (that day's total receipts)
    Cr  CIT - Cafe/Resto             (that day's total receipts)
```
Example for one day: `Dr Bank 72,562 | Cr CIT - Cafe/Resto 72,562`. Repeated daily, so **CIT
accumulates the receipts** not yet booked as formal sales.

**2. Month-end — check & compare.**
The total accumulated in the **CIT summary** is reconciled against the **sales report from the café's
operational system** (POS). So the check is: *total sales per the café ops report* vs *total receipts
in CIT* — they must match.

**3. Month-end — aggregate into one Sales Invoice.**
Once matched, the whole month's transactions are booked as **one Sales Invoice** to a generic
"CASH SALES" customer, combined (aggregated). Since prices already include VAT, just tick **Inclusive
Tax** → the system separates net sales & Output VAT. This SI becomes the basis for the **fiscal sales
report** filed with the **tax office**.

---

## The journal produced (month-end)

**Aggregated Sales Invoice** (example: Total IDR 5,454,713 *incl* VAT, VAT IDR 540,557):
```
Dr  Accounts Receivable           5,454,713
    Cr  Sales (F&B)                   4,914,156
    Cr  Output VAT                      540,557
```
**Its receipt is cleared from CIT** (Sales Receipt via the CIT account), so the CIT balance that had
built up **returns to zero**:
```
Dr  CIT - Cafe/Resto              (the total previously parked)
    Cr  Accounts Receivable          (settlement of the aggregated SI)
```

> **Net result:** cash entered the bank daily (real), sales & VAT are recognized **once** via the
> aggregated SI at month-end, and the **CIT account nets to zero** (in daily → out on aggregation).

---

## Why use this?

- **Saves time:** entering an SI per retail customer every day is very time-consuming; retail is
  high-volume but **immaterial** per transaction.
- **Still correct for tax:** total sales & VAT are ultimately recorded via the aggregated SI.
- **Has a control:** you must **reconcile** the CIT summary against the café POS report before
  aggregating.

> **Remember:** this is a **practical tip, not an accounting rule.** Make sure the aggregated figure
> **matches** the operational report, and that VAT is computed correctly (tick *Inclusive Tax* if the
> price already includes VAT).
