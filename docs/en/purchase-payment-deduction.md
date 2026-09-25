# Purchase Payment with Deduction

When **paying a vendor** through a **Purchase Payment**, the company (as the **withholding agent**)
withholds PPh from the payment. The deduction is recorded in the **deduction field** (the software
labels it *Discount / Write-off*); cash out = invoice − deduction.

> **Key — the opposite of the Sales Receipt side:** here every tax deduction goes to a **Tax Payable**
> account, because the company **withholds** tax from the vendor **to remit to the state**. Not an asset
> and not an expense — a **liability**.

## The account: all to Tax Payable (by PPh type)

| Deduction type | Target account | Nature |
|---|---|---|
| **PPh 23** (services) | **PPh 23 Payable** *(Tax Payable – W/H art.23)* | Liability |
| **PPh 21** (e.g. individual's services) | **PPh 21 Payable** *(Tax Payable – W/H art.21)* | Liability |
| **Final PPh on rent** (Article 4(2)) | **Final PPh Payable Art.4(2)** *(Tax Payable – W/H art.4(2))* | Liability |

## Journal examples (concept)

**a) PPh 23** — invoice IDR 5m, PPh 23 withheld IDR 90k:
```
Dr  Accounts Payable               5,000,000
    Cr  PPh 23 Payable                 90,000
    Cr  Cash/Bank                   4,910,000
```

**b) PPh 21** — service (retainer) IDR 10m, PPh 21 withheld IDR 250k (2.5%):
```
Dr  Accounts Payable              10,000,000
    Cr  PPh 21 Payable                250,000
    Cr  Cash/Bank                   9,750,000
```

**c) Final PPh on building rent** (Article 4(2)) — rent IDR 149.85m, final 10% withheld IDR 14,985,000:
```
Dr  Accounts Payable             149,850,000
    Cr  Final PPh Payable Art.4(2)   14,985,000
    Cr  Cash/Bank                  134,865,000
```

The company then **remits** the withheld tax to the state and **issues a withholding slip** to the vendor.

## Contrast with the collection side (Sales Receipt)

| PPh deduction | **Purchase Payment** (we **withhold**) | **Sales Receipt** (we are **withheld from**) |
|---|---|---|
| PPh 23 | **PPh 23 Payable** (liability) | **Prepaid PPh 23** (asset / tax credit) |
| Final PPh (rent) | **Final PPh Payable** (liability) | **Final Tax Expense** (expense) |

> **Bottom line:** the party that **withholds** records **Tax Payable** (withhold → remit to the state);
> the party **withheld from** records a **tax credit / expense**. See both sides in
> [Tips: Withholding Tax (PPh 23)](tips-wht-article-23.md) and the collection side in
> [Sales Receipt with Deduction](sales-receipt-deduction.md).
