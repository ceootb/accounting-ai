# Sales Receipt with Deduction

When receiving payment through a **Sales Receipt**, the cash received is sometimes **less than the
invoice** because of a **deduction** — e.g. the customer **withholds tax**, or the funds are **reduced
by a bank charge**. This is recorded in the **deduction field** (the software labels it *Discount /
Write-off*).

> **This is a *deduction* (a payment reduction), not a *sales discount* (a price cut).** A sales
> discount reduces **revenue**; the deduction here does **not** — its amount goes to a **tax/expense
> account** depending on the type. The receivable is still treated as **fully settled**.

## The account follows the type of deduction

| Deduction type | Target account | Nature |
|---|---|---|
| **PPh 23** (creditable) | **Prepaid PPh 23 / Prepaid Tax** | Asset (tax credit) |
| **Final PPh** (e.g. on rent) | **Final Tax Expense** | Expense (final, not creditable) |
| **Non-tax** (e.g. bank / admin fee) | related **Expense** account (e.g. Bank Charge) | Expense |

## Journal examples (concept)

**a) PPh 23 deduction** — invoice IDR 350m, PPh 23 withheld IDR 6,306,306:
```
Dr  Cash/Bank                    343,693,694
Dr  Prepaid PPh 23                 6,306,306
    Cr  Accounts Receivable       350,000,000
```

**b) Final PPh on rent** — one Sales Receipt settles **3 rental invoices** @IDR 11.1m (base IDR 10m +
VAT IDR 1.1m); each is withheld 10% × IDR 10m = IDR 1m:
```
Dr  Cash/Bank                     30,300,000
Dr  Final Tax Expense              3,000,000
    Cr  Accounts Receivable        33,300,000
```

**c) Bank charge** — the funds received are already net of a bank charge:
```
Dr  Cash/Bank                     (net amount received)
Dr  Bank Charge Expense           (bank charge)
    Cr  Accounts Receivable       (invoice amount)
```
*(For foreign-currency receipts an extra FX-difference line may appear; for Rupiah it does not.)*

## One Sales Receipt, several Sales Invoices

One Sales Receipt can **settle several Sales Invoices at once**, each with its own deduction (see the
rent example above). The remaining balance is still monitored via **Owing** — see
[Sales Invoice — Installment Payment (Owing)](sales-invoice-installment-payment.md).

> **Bottom line:** a deduction on a Sales Receipt is a **payment reduction**, not a price discount.
> Cash received = invoice − deduction; the difference goes to the **tax/expense account by type**, and
> the receivable stays recorded as settled. For the tax side, see [Tips: Withholding Tax (PPh 23)](tips-wht-article-23.md). Payment side (we withhold): [Purchase Payment with Deduction](purchase-payment-deduction.md).
