# Allocating One Payment/Receipt to Several Invoices (1-to-many)

The relationship between a **payment** and an **invoice** isn't always one-to-one. Besides one invoice
being paid in **installments** (many payments → 1 invoice), a single cash/bank transaction can also
**settle several invoices at once** (1 payment → many invoices). This page covers the second direction.

## Purchase Payment → several Purchase Invoices

- One **Purchase Payment** transaction can pay **several Purchase Invoices** from the **same vendor**.
- The user picks several Purchase Invoices that still have an **owing** balance, then **allocates** the
  payment amount to each invoice.
- The **total allocation must not exceed** the Purchase Payment amount.
- The system **records the allocation** to each invoice; **each invoice's status is updated** — it can
  become **fully paid** or **partially paid**.
- The Purchase Payment remains **one transaction**, even when allocated to several invoices.

## Sales Receipt → several Sales Invoices

The mirror on the collection side:
- One **Sales Receipt** can receive payment for **several Sales Invoices** from the **same customer**.
- The user picks several Sales Invoices still owing, then **allocates** the receipt amount to each.
- The **total allocation ≤ the Sales Receipt amount**; each invoice becomes **fully** or **partially
  received**; the Sales Receipt stays **one transaction**.

## Key accounting concept

- The relationship is **1-to-many**: **1 Purchase Payment → several Purchase Invoices**; **1 Sales
  Receipt → several Sales Invoices**.
- The system **must not force** the user to create one payment/receipt transaction **per invoice** when
  a single bank/cash transaction is genuinely used to settle several invoices at once.
- **The allocation detail must be traceable** — the user can see which invoices were paid/received
  through a particular Purchase Payment or Sales Receipt.

## Journal form (concept)

One Purchase Payment of **IDR 100m** for 3 Purchase Invoices (allocation IDR 40m + 35m + 25m):
```
Dr  Accounts Payable             100,000,000   (allocated: PI-A 40m, PI-B 35m, PI-C 25m)
    Cr  Cash/Bank                 100,000,000
```
> One cash/bank credit; **Accounts Payable decreases per invoice** by its allocation. The Sales side is
> simply reversed: `Dr Cash/Bank | Cr Accounts Receivable`, allocated across several Sales Invoices.

## Relation to installment payment

Combined with the **[installment payment (Owing)](sales-invoice-installment-payment.md)** concept —
many payments → 1 invoice — the payment↔invoice relationship is really **many-to-many**. The reference
is always each invoice's **Owing** (invoice amount − amount allocated) until it reaches zero.

> **Bottom line:** one bank transaction can be **allocated across several invoices**; each invoice's
> status is updated (fully/partially), and the **allocation stays traceable** — without forcing one
> payment per invoice.
