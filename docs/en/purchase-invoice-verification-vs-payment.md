# Purchase Invoice — Document Verification & Payment Control

One boundary is often blurred in practice: **"may be recorded as a payable"** is not the same as
**"may be paid"**. These are **two separate gates**. Mixing them corrupts the accounting — either the
payable is recognized late, or payment control leaks.

## Two different gates

### 1. Accounting gate — *may it be recorded as a payable?*
Focused on the **correctness of the record** and the **auto-journal**. What is verified:
- **Supplier**, **invoice number & date**, **item**, **qty**, **price**, **tax**, **account**, and
- **Debit/Credit validation** (the journal must balance).

If all of this is correct, the Purchase Invoice **may be recognized as Accounts Payable (A/P)** —
because the obligation has **already arisen** when the goods/services were received (*accrual* &
*matching* principles).

### 2. Finance / AP gate — *may it be paid?*
Focused on **document completeness & approval** as a **payment prerequisite**. What is verified
includes: **PO**, **goods-receipt evidence**, **invoice**, **tax documents**, **approval**, and
**payment terms**. This gate exists to **prevent unauthorized payment** (double payment, no PO, goods
not received).

## The boundary principles

- **Do not mix payment control into accounting journal logic.** The journal follows economic substance
  (the payable has arisen), not the status of payment paperwork.
- **An invoice already valid for accounting is still recorded as Accounts Payable**, even if the
  payment documents are incomplete. Delaying payable recognition just because payment paperwork isn't
  ready = **understated liabilities** (misstated reports).
- **If payment requirements aren't met → the status is *payment hold*, not a cancellation of the
  accounting transaction.** The payable stays recorded; only the **right to be paid** is held until
  the finance gate is satisfied.

## Summary

| Dimension | **Accounting** gate | **Finance / AP** gate |
|---|---|---|
| Question | May it be **recorded** as a payable? | May it be **paid**? |
| What is checked | Supplier, invoice, date, item, qty, price, tax, account, Dr/Cr balance | PO, goods receipt, invoice, tax docs, approval, payment terms |
| Result | Recognized as **Accounts Payable** (auto-journal) | **Payable to pay** / **payment hold** |
| If incomplete | Still **recorded** as a payable | Payment **held**; accounting transaction **not cancelled** |

> **Bottom line:** accounting records the **obligation that has already arisen**; finance/AP controls
> **when it may be paid**. Keep them separate — this is also **segregation of duties**. The accounting
> system just records the payable and its journal; the payment-approval flow is a **separate control
> layer**, not an extension of journal logic.

---

## Partial / Installment Payment

**One Purchase Invoice may be paid more than once** per the SLA / payment terms agreed with the
supplier. The key rule: **do not create a new Purchase Invoice for each payment.** The Purchase Invoice
remains the **source of the payable**; each payment entry only **reduces the Accounts Payable balance
of the same invoice** until the outstanding reaches zero.

**Example** — a Purchase Invoice of **IDR 100m**, paid in 3 installments:

| Step | Journal | Outstanding |
|---|---|---|
| Purchase Invoice | `Dr Inventory/Expense 100m \| Cr Accounts Payable 100m` | 100m |
| Payment 1 (IDR 30m) | `Dr Accounts Payable 30m \| Cr Cash/Bank 30m` | 70m |
| Payment 2 (IDR 40m) | `Dr Accounts Payable 40m \| Cr Cash/Bank 40m` | 30m |
| Payment 3 (IDR 30m) | `Dr Accounts Payable 30m \| Cr Cash/Bank 30m` | **0** |

- The **Accounts Payable for that invoice decreases with each payment**; the principal is not
  re-recorded.
- The system can show **total invoice, total paid, and outstanding balance** — typically in the
  **owing** column on the Purchase Invoice. That owing column is "the amount still due".
- While owing isn't zero, the invoice is **not yet fully paid** (partially paid).

> **Mirror on the Receivable (AR) side:** the same concept works in reverse — one **Sales Invoice** can
> be collected in installments; each **Sales Receipt** reduces the **Accounts Receivable** of the same
> invoice until its outstanding is zero. No new Sales Invoice is created per collection.
