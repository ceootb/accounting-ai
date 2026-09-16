# Purchase Module — Framework & Logic

> The **Procure-to-Pay (P2P)** cycle and its accounting logic. Focus first on **flow + logic +
> auto-journal per step**; **field details** to follow.
> *(Draft — curated by a practicing accountant.)*

---

## 1. The 6-Step Flow (Procure-to-Pay)

```
1. Purchase Requisition (PR)   — internal request to buy
2. Purchase Order (PO)         — official order to the vendor
3. Receive Items (GRN)         — goods/services received
4. Purchase Invoice            — vendor's bill/invoice
5. Purchase Return             — return of goods (if any)
6. Purchase Payment            — payment to the vendor
```

---

## 2. Journaling Logic per Step

| Step | Journal? | Auto-journal | Notes |
|---|---|---|---|
| **1. Purchase Requisition** | ❌ No | — | Internal document (request/approval). No financial impact yet. |
| **2. Purchase Order** | ❌ No | — | Commitment to vendor (off-balance). Position unchanged. |
| **3. Receive Items** | ✅ Yes | `Dr Inventory` \| `Cr Accrued Purchase (GRNI)` | Goods received → asset up, temporary liability (received-not-invoiced). |
| **4. Purchase Invoice** | ✅ Yes | `Dr Accrued Purchase` (or Inventory/Expense) + `Dr Input VAT` \| `Cr Accounts Payable` | Vendor invoice → recognize **AP** & **Input VAT**; clear the GRNI. |
| **5. Purchase Return** | ✅ Yes | `Dr Accounts Payable` \| `Cr Inventory` (+ reverse Input VAT) | Reverse of purchase; reduces payable & inventory. |
| **6. Purchase Payment** | ✅ Yes | `Dr Accounts Payable` \| `Cr Cash/Bank` | Settle the payable; cash/bank down. |

> **Key:** Steps **1-2 do not journal** (commitment docs). Journals start at **Receive Items**, then
> **Purchase Invoice** (recognize payable + VAT), and close at **Purchase Payment**.

---

## 3. Key Logic Principles

1. **3-Way Match** (core control): before paying, match **PO ↔ Goods Receipt ↔ Invoice** (qty & price).
   Prevents paying for goods not ordered / not received / mispriced.
2. **Item type drives the debit account:**
   - *Inventory part* → **Inventory** (asset).
   - *Non-inventory / service / expense* → straight to **Expense** (may skip "Receive Items").
3. **Input VAT** is recognized at the **Purchase Invoice** (tax invoice), **not** at goods receipt.
4. **Received-not-invoiced:** if goods arrive before the invoice, use a temporary "Accrued Purchase"
   account, then move it to Accounts Payable when the invoice arrives.
5. **AP flow:** Invoice increases AP → Payment decreases AP. AP balance = unpaid bills.

---

## 4. In One Breath

`PR & PO = commitment (no journal)` → `Receive = asset in + temporary payable` →
`Invoice = Accounts Payable + Input VAT` → `Payment = AP settled, cash out`.
(Return = the reversal when goods are sent back.)

*Field details for each document (vendor, item, qty, price, tax, terms, etc.) to follow in the next doc.*
