# Other Deposit (Non-Customer Cash/Bank Receipt, outside AR)

**Other Deposit** records **money coming into Cash/Bank** that is **not** from a **Customer/AR** and
**not** a receipt from the sales cycle.

**Its journal:**
```
Dr  Cash / Bank
    Cr  Counter account
```
> The **counter account is determined by the transaction's SUBSTANCE**, not by the module name. **Other
> Deposit ≠ always Other Income.**

## Function & limits

- Used for **Cash/Bank receipts outside Customer Receipt / AR**.
- **Don't** use it to **settle a Customer receivable.** If the money in = a Sales Invoice/AR payment
  (`Dr Cash/Bank | Cr Customer Receivable`), it **must** go through a **Customer Receipt** so the
  Customer & Invoice/AR *linkage* is formed.
- **Also not** for **transfers between Cash/Bank** — use the proper transfer mechanism.

## The counter account follows substance (not automatically income)

```
Bank interest received : Dr Bank | Cr Interest Income
Substantively an asset : Dr Bank | Cr the appropriate Asset account
Substantively a liability: Dr Bank | Cr the appropriate Liability account
```

## Fields (UI reference)

- **Deposit To** = the **Cash/Bank** account that **receives** the money.
- **Account No** = the **counter account** from the COA. **The AR account is not used**; **don't** create
  an AR/Customer *linkage*.
- **Detail:** Account No, Account Name, **Amount** (the counter-account value), **Department** (a reporting
  dimension; doesn't change the function), **Memo**.
- **Total Deposit** must **balance** with the total detail.

## Examples

```
1. Bank interest received IDR 500,000:
   Deposit To = Bank ; Account No = Interest Income
   Dr Bank 500,000 | Cr Interest Income 500,000

2. A receipt that is substantively an asset:
   Dr Bank xxx | Cr Asset account xxx
```
> **Don't** automatically classify every Other Deposit as *revenue*.

## Relationship with Other Payment

A pair of Cash/Bank transactions **outside the AR/AP cycle**:

| | Cash/Bank | Counter account |
|---|---|---|
| **[Other Deposit](other-deposit-cash-bank.md)** | **in** (Debit) | **credited** |
| **[Other Payment](other-payment-cash-bank.md)** | **out** (Credit) | **debited** |

> The counter account is **still** determined by the transaction's **substance**.

## Principle

> Understand Other Deposit as a **"non-Customer / non-AR money-in form"** — **not** an *"Other Income
> form"*. Don't assume every receipt is income. **Always identify the substance** & pick the right counter
> account. **Don't** create a Customer/Invoice/AR *linkage* if the transaction isn't from a Customer/AR.

> **Note:** the *screenshot* is a **UI** reference to reinforce the concept — don't invent fields/behavior
> not shown. Separate **(1) the accounting concept, (2) software behavior, (3) UI restriction**; don't
> change the accounting concept just because of a UI limitation. The goal is to understand the **logic** &
> produce a **correct journal based on substance**, not to mimic the software's look.
