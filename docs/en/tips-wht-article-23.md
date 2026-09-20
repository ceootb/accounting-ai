# Tips: Journaling Withholding Tax (PPh Article 23) — Both Sides

> **PPh Article 23** = tax withheld on **services** (and rent, royalties, etc.). There are **two
> sides** that often confuse people: when the company **withholds** (buying services) vs when the
> company **is withheld from** (selling services). The key: the withholder records **PPh 23 Payable**,
> the party withheld from records **Prepaid PPh 23**. The example uses a **2%** rate on the service
> value (tax base).

---

## Side 1 — The company as WITHHOLDER (buying services from a vendor)

When buying **services**, the company **must withhold** PPh 23 from the vendor and **remit it to the
state**. So the amount paid to the vendor is **reduced** by the tax withheld.

**On the Purchase Invoice:** fill in the **PPh 23** section (pick the account & rate) → the system
computes the withholding and creates **PPh 23 Payable**.

**Example:** consulting service, base IDR 10,000,000 + Input VAT IDR 1,100,000; PPh 23 2% = IDR 200,000.
```
Dr  Consulting Expense            10,000,000
Dr  Input VAT                      1,100,000
    Cr  Accounts Payable (vendor)     10,900,000
    Cr  PPh 23 Payable (remit to state)  200,000
```
> The vendor bills IDR 11,100,000, but only **IDR 10,900,000** is paid; the remaining **IDR 200,000**
> is held as **PPh 23 Payable** to remit to the state. The company then issues a **withholding slip**
> to the vendor. *(This also appears at [Purchase Payment](purchase-module-framework.md#6-purchase-payment-paying-the-vendor--field-data-entry-detail) — cash out is smaller than the payable.)*

---

## Side 2 — The company as the PARTY WITHHELD FROM (selling services to a customer)

When **selling services**, the customer (if a withholding agent) will **withhold** PPh 23 from their
payment. As a result the **cash received is less** than the invoice value. That "short payment" is
**not a loss** — it is **Prepaid PPh 23**, a **tax credit** that later reduces the company's
corporate income tax at year-end.

**At the Sales Invoice** (recognizing service revenue) — full value:
```
Dr  Accounts Receivable           11,100,000
    Cr  Service Revenue               10,000,000
    Cr  Output VAT                     1,100,000
```

**When payment is received** (the customer withholds PPh 23 of IDR 200,000) — the key point:
```
Dr  Cash/Bank                     10,900,000
Dr  Prepaid PPh 23                    200,000
    Cr  Accounts Receivable           11,100,000
```
> The receivable is **fully settled at IDR 11,100,000**, but cash in is only **IDR 10,900,000**. The
> **IDR 200,000** difference **must not** be left hanging in receivables — it must be **journaled to
> Prepaid PPh 23** (an **Asset** account). The basis is the **withholding slip** the customer
> provides; keep it, as it **reduces corporate income tax** in the annual return.

---

## Summary

| Position | Role | PPh 23 account | Nature |
|---|---|---|---|
| **Buying services** | Withholder | **PPh 23 Payable** | Liability (remit to state) |
| **Selling services** | Withheld from | **Prepaid PPh 23** | Asset (tax credit) |

> **Key:** the PPh 23 base = the **service** value (excluding VAT). The one who withholds → **PPh 23
> Payable**; the one withheld from → **Prepaid PPh 23**. For the seller, the "short payment" from
> withholding **must** be moved to Prepaid PPh 23 so the receivable stays fully settled and the tax
> credit is recorded.
