# Tips: Cash Clearing Account (CCA) for Aggregating Retail Sales

> A **time-saving trick** for businesses with **very many, low-value retail transactions** (e.g.
> cafés & restaurants). Instead of entering each sale one by one every day (a waste of time, and each
> transaction is immaterial), daily receipts are **parked** in a **clearing account / Cash Clearing
> Account (CCA)**, then **aggregated** into **one Sales Invoice** at month-end for tax reporting.
>
> ⚠️ **Honest note:** this is **purely a practical time-saving workflow — not part of standard
> accounting theory.** Its goal is entry efficiency while keeping sales & VAT figures correct for tax.

---

## Terminology note: why "CCA", not "CIT"?

Some software labels this account **CIT (Cash in Transit)**, but that's **imprecise**. Strictly,
**Cash in Transit** means **cash received but not yet deposited to the bank** (e.g. cash taken at
night when the bank is closed). In this retail case the **money is already in the bank** — so it isn't
"in transit".

The more accurate concept is a **clearing account**: a temporary account deliberately used to
**bridge two entries** and that **must clear to zero** once done. We use the term **Cash Clearing
Account (CCA)**.

| Term | Meaning | Fits here? |
|---|---|---|
| **Clearing account (CCA)** | A temporary bridging account, deliberately zeroed | ✅ Yes |
| **Suspense account** | A holding account when the **classification is not yet clear** | ❌ (here it's clearly retail sales) |
| **Sundry account** | A "miscellaneous / other" account | ❌ (not a bridging account) |

> **On PSAK:** PSAK **does not prescribe internal account names** like this — it's the company's
> internal chart-of-accounts policy. PSAK governs **revenue recognition** (PSAK 72) & **statement
> presentation** (PSAK 1 / PSAK 201). The requirements: the CCA is **temporary & zero at period-end**,
> and revenue is **still recognized in the correct period**.

---

## Account setup & its control

- **The CCA is registered in the COA as a Cash/Bank-type account.** Practical reason: so it can be
  picked as the "receiving bank" in a Sales Receipt. Presentation is fine because its month-end
  balance is zero.
- **You may have more than one CCA — split by retail stream** for per-stream control. Consistent
  naming example:
  - `CCA - Cafe`
  - `CCA - Merchandise`
  - `CCA - Food`
  Each CCA is reconciled with its own stream's POS report, so any mismatch is spotted per stream.
- **Mandatory control: at every month-end each CCA balance must be ZERO.** If not, some receipts
  haven't been aggregated into a Sales Invoice, or there's a mismatch with the POS report — it must be
  investigated before closing.

---

## The flow

**1. Daily — park receipts into the CCA (via a Journal Voucher).**
Each day, the total café/resto receipts (all of that day's transactions combined) that land in the
bank are recorded with a JV:
```
Dr  Bank                         (that day's total receipts)
    Cr  CCA - Cafe                   (that day's total receipts)
```
Example for one day: `Dr Bank 72,562 | Cr CCA - Cafe 72,562`. Repeated daily, so the **CCA
accumulates the receipts** not yet booked as formal sales.

**2. Month-end — check & compare.**
The **CCA summary** total is reconciled against the café's **operational (POS) sales report**: *total
sales per ops* vs *total receipts in the CCA* — they must match.

**3. Month-end — aggregate into one Sales Invoice.**
Once matched, the whole month is booked as **one Sales Invoice** to a generic "CASH SALES" customer,
combined. Since prices already include VAT, just tick **Inclusive Tax** → the system separates net
sales & Output VAT. This SI is the basis for the **fiscal sales report** filed with the **tax office**.

---

## The journal produced (month-end)

**Aggregated Sales Invoice** (example: Total IDR 5,454,713 *incl* VAT, VAT IDR 540,557):
```
Dr  Accounts Receivable           5,454,713
    Cr  Sales (F&B)                   4,914,156
    Cr  Output VAT                      540,557
```
**Its receipt is cleared from the CCA** (Sales Receipt via the CCA account), so the balance that had
built up **returns to zero**:
```
Dr  CCA - Cafe                    (the total previously parked)
    Cr  Accounts Receivable          (settlement of the aggregated SI)
```

> **Net result:** cash entered the bank daily (real), sales & VAT are recognized **once** via the
> aggregated SI at month-end, and the **CCA nets to zero** (in daily → out on aggregation).

---

## Why use this?

- **Saves time:** entering an SI per retail customer every day is very time-consuming; retail is
  high-volume but **immaterial** per transaction.
- **Still correct for tax:** total sales & VAT are ultimately recorded via the aggregated SI.
- **Has a control:** you must **reconcile** each CCA against its café POS report, and each **CCA must
  be zero** at month-end.

> **Remember:** this is a **practical tip, not an accounting rule.** Make sure the aggregated figure
> **matches** the operational report, VAT is computed correctly (tick *Inclusive Tax* if prices
> already include VAT), and each CCA is **zero** at month-end.
