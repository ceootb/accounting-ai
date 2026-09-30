# Other Payment (Direct Cash/Bank Outflow to a GL Account)

**Other Payment** is a **direct Cash/Bank outflow to a GL account** that is **NOT** used to *settle* a
**Sales Invoice (AR)** or a **Purchase Invoice (AP)**.

**Its journal:**
```
Dr  Target account (Expense / Asset / Liability)
    Cr  Cash / Bank
```

## When it's used (typical use)

- **Direct** expense/cost payment; **bank administration fee**;
- Buying **supplies** expensed directly; **cash purchase of a Fixed Asset**; **prepaid expense**;
- Paying a **non-trade / Other Liability**;
- Other Cash/Bank outflows **unrelated** to an AR/AP vendor.

## AR / AP separation is mandatory

There are **three routes** that must never be confused:

| Route | Flow |
|---|---|
| **AR** (customer invoice) | Customer → **Sales Receipt** → AR **Customer Sub-GL** → Cash/Bank |
| **AP** (vendor invoice) | Vendor → **Purchase Payment** → AP **Vendor Sub-GL** → Cash/Bank |
| **Other Payment** | **Direct** → **GL account** → Cash/Bank |

**Other Payment does NOT:** use a Customer/Vendor Sub-GL; pick a Sales/Purchase Invoice to *settle*; do
an AR/AP allocation; change a **customer receivable** balance; or change a **trade/vendor payable**
balance.

## "Paying a debt" ≠ always a Purchase Payment

What decides is **not** the phrase "paying a debt" but the **liability type & its subledger**:
- **Accounts Payable / AP** that is **linked to a Vendor** → **Purchase Payment**.
- An **Other Liability** that is **not** linked to a Vendor/AP → may be settled via **Other Payment**.

```
Settling an Other Liability (non-vendor):
Dr  Other Liability
    Cr  Bank
```
> This reduces the **Other Liability** GL balance, but does **not** reduce the **AP Vendor** balance and
> needs **no** Vendor.

## Journal examples

```
A. Pay electricity      : Dr Electricity Expense       | Cr Bank
B. Buy Fixed Asset (cash): Dr Fixed Asset              | Cr Bank
C. Pay bank admin       : Dr Bank Administration Expense | Cr Bank
D. Settle Other Liability: Dr Other Liability           | Cr Bank
```

## Fields (UI reference)

- **Header:** Paid From / **Cash-Bank** account, Voucher No., Cheque No. (if any), Date, Memo, Payee, Amount.
- **Detail:** Account No., Account Name, Amount, **Department**, Memo.
  - **Account No.** = **all accounts except AP accounts that have a Sub-GL** → hence **no Sub-GL column**
    on the Other Payment screen.
  - **Department** is only a **tracking dimension** if needed — **not** an indicator that the transaction
    is AR/AP.

## Core rule

> **Other Payment = a direct Cash/Bank outflow to a GL account, without an AR/AP subledger.** Don't
> assume *"paying a debt = AP Vendor"*. Check first: is the liability **Accounts Payable (Vendor-linked)**
> → Purchase Payment; or an **Other Liability (no Vendor/AP)** → Other Payment.

> **Its mirror — Other Deposit:** a direct Cash/Bank **inflow to a GL account** (not an AR *settlement*):
> `Dr Cash/Bank | Cr GL account`. *(Other Deposit details to follow.)*
