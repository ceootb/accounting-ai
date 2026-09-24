# Sales Invoice — Partial / Installment Payment (Owing)

**One Sales Invoice can receive more than one payment** through several **Sales Receipts**, per the
payment terms / SLA with the customer. All those Sales Receipts **still refer to the same Sales
Invoice** — **do not create a new Sales Invoice for each payment.** The Sales Invoice remains the
**source of the receivable**; each Sales Receipt only **reduces the Accounts Receivable balance** of
the same invoice until the outstanding reaches zero.

**Example** — a Sales Invoice of **IDR 100m**, collected in 3 installments:

| Step | Journal | Outstanding (*Owing*) |
|---|---|---|
| Sales Invoice | `Dr Accounts Receivable 100m \| Cr Revenue (+VAT) 100m` | 100m |
| Sales Receipt 1 (IDR 30m) | `Dr Cash/Bank 30m \| Cr Accounts Receivable 30m` | 70m |
| Sales Receipt 2 (IDR 40m) | `Dr Cash/Bank 40m \| Cr Accounts Receivable 40m` | 30m |
| Sales Receipt 3 (IDR 30m) | `Dr Cash/Bank 30m \| Cr Accounts Receivable 30m` | **0** |

## Monitoring via the Owing column

> **Owing = Sales Invoice value − total Sales Receipts already received.**

- **Owing = 0** → the invoice is **fully paid**.
- **Owing > 0** → there is still a **receivable not yet collected** (partially paid invoice).

The receivable for that invoice **decreases with each collection**; the principal is **not re-recorded**
and no new Sales Invoice is created.

## Consistent with the Payable (AP) side

This is the **mirror** of the purchasing side. See
[Purchase Invoice — Installment Payment](purchase-invoice-verification-vs-payment.md#partial--installment-payment):

| | **Sales Invoice (AR)** | **Purchase Invoice (AP)** |
|---|---|---|
| Source | 1 Sales Invoice | 1 Purchase Invoice |
| Payment entry | many **Sales Receipts** | many **Payments** |
| What decreases | **Accounts Receivable** | **Accounts Payable** |
| Monitor column | **Owing** (remaining receivable) | **Owing** (remaining payable) |
| Rule | 1 invoice, many payments; **not** a new invoice per payment | same |

> **Bottom line:** one invoice = one source of receivable/payable; installment payments **reduce its
> outstanding**, monitored via **Owing**, until zero (fully paid).
