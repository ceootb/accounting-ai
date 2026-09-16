# Purchase Module — Framework & Logic

> The **Procure-to-Pay (P2P)** cycle and its accounting logic. Focus first on **flow + logic +
> auto-journal per step**; **field details** to follow.
> *(Curated by a practicing accountant.)*

---

## 0. Setup Prerequisite

**Items are configured up front**, and **each item is linked to a COA** account (e.g. Inventory).
This item → COA mapping is what lets the **auto-journal** know which account to use during transactions.

---

## 1. The 6-Step Flow (Procure-to-Pay)

```
1. Purchase Requisition (PR)   — internal request to buy
2. Purchase Order (PO)         — official order to the vendor
3. Receive Items (GRN)         — goods received by warehouse (pulls PO data)
4. Purchase Invoice            — vendor's bill (pulls Received Item data)
5. Purchase Return             — return of goods (if any)
6. Purchase Payment            — payment to the vendor
```

---

## 2. Journaling Logic per Step

| Step | Journal? | Auto-journal | Notes |
|---|---|---|---|
| **1. Purchase Requisition** | ❌ No | — | Record & **approval** by user/manager only. No financial impact. |
| **2. Purchase Order** | ❌ No | — | Official order to vendor (commitment). No journal. |
| **3. Receive Items** | ⚪ Warehouse record | — (journal at Purchase Invoice) | Goods received by **warehouse** by **pulling the PO** data. No accounting journal yet. |
| **4. Purchase Invoice** | ✅ Yes | `Dr Inventory` \| `Cr Accounts Payable`  *(+ `Dr Input VAT` if a tax invoice exists)* | **Pulls Received Item** data on entry. **This is where the accounting journal happens** — recognize inventory & AP. |
| **5. Purchase Return** | ✅ Yes | **Automatic reversal by the system** | Goods returned → the system reverses the purchase journal (reduces inventory & payable). |
| **6. Purchase Payment** | ✅ Yes | `Dr Accounts Payable` \| `Cr Cash/Bank` | On entry, just input **paid via bank/cash**; auto-journal settles the payable. |

> **Key:** PR & PO = record + approval (**no journal**). Receive Items = **warehouse receipt**
> (pulls PO, no journal yet). **The accounting journal happens at Purchase Invoice** (`Dr Inventory |
> Cr Accounts Payable`), and closes at **Purchase Payment** (`Dr AP | Cr Cash/Bank`).

---

## 3. Key Logic Principles

1. **Item → COA setup:** each item is linked to an Inventory account up front → the basis of auto-journal.
2. **Data flows between documents:** PO → pulled by Receive Items → pulled by Purchase Invoice. This
   naturally enforces the **3-way match** (order ↔ receipt ↔ invoice) and prevents wrong qty/price.
3. **Journal point = Purchase Invoice** (not at goods receipt, in this model).
4. **Input VAT** is recognized at the Purchase Invoice (if a tax invoice exists).
5. **Return = automatic reversal** by the system (no manual journal needed).
6. **AP flow:** Purchase Invoice increases AP → Purchase Payment decreases AP.

**Why journal at Purchase Invoice (not at Receive Items)?** Because **vendors usually ship the goods
together with the invoice/bill** — once goods arrive, the bill already exists, so the payable is certain
even if the **payment term** is later. Thus a **single journal at Purchase Invoice** suffices.
*(Some systems offer a "goods received not invoiced / GRNI" auto-journal at Receive Items; that only
matters when there is a **significant time gap** between goods receipt and invoice issuance.)*

---

## 4. In One Breath

`PR & PO = record + approval (no journal)` → `Receive Items = warehouse receipt, pull PO` →
`Purchase Invoice = JOURNAL: Dr Inventory | Cr Accounts Payable (+ Input VAT)` →
`Purchase Payment = Dr AP | Cr Cash/Bank`. (Return = automatic reversal.)

*Field details for each document (vendor, item, qty, price, tax, terms, etc.) to follow.*
