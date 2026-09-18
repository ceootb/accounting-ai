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

---

## 5. Purchase Invoice — Field Data Entry Detail

**Purchase Invoice = the bill from a vendor.** As in sales, the user **selects data** via **dropdowns ▼**
and the **magnifier 🔍**; the system computes tax & totals, then creates the journal automatically.

### Fields to fill

**a) Top section (vendor & document):**
- **Vendor** ▼ — pick from the vendor master (auto-pulls address & terms).
- **Select PO** ▼ — pull data from a **Purchase Order** if any (items fill in automatically).
- **Vendor is Taxable** ☑ and **Inclusive Tax** ☑ — whether VAT applies & whether prices already
  include VAT.
- **Form No.** (auto), **Invoice No.**, **Invoice Date**, **Ship Date**, **Terms** ▼ (e.g. Net 14),
  **A/P Account** ▼ (the **Payable** account used).

**b) The transaction body — three ways to enter it:**

1. **Via Item** (*Items* tab) — for **buying goods/inventory**. Pick an **Item** 🔍 from the master
   (pulls price & COA), enter **Qty**, **Unit Price**, **Tax**, and **Dept.** 🔍. Amount is computed
   automatically. Best for stock entering the warehouse.
2. **Via COA account** (*Expense* tab) — for **buying services/expenses** (e.g. internet, bank
   charges). Pick an **Account No.** 🔍 from the COA list, enter **Amount**, **Notes**, and
   **Department** 🔍.
3. **Combination** — items **and** additional costs at once (e.g. goods + freight/admin fee).

> **Key insight:** an "item" can be **set up to equal an expense account in the COA** (item-for-expense).
> When it is, the **resulting journal is exactly the same** whether the cost is entered via **Item** or
> via the **Expense** tab — so the user can pick whichever is more convenient.

### VAT: Exclusive vs Inclusive
- **Exclusive:** VAT is **added** on top of the price. E.g. IDR 3,000,000 → VAT 330,000 → total 3,330,000.
- **Inclusive:** VAT is **stripped out** of the price. E.g. IDR 3,000,000 already includes VAT →
  net expense 2,702,702 + VAT 297,298.

### The auto-journal produced

**Example 1 — buying inventory (Exclusive VAT):** 50 units × IDR 110,000 = 5,500,000, VAT 605,000.
```
Dr  Inventory            5,500,000
Dr  Input VAT              605,000
    Cr  Accounts Payable       6,105,000
```

**Example 2 — buying an expense, item + bank charge combination (Inclusive VAT):** internet
IDR 3,000,000 (VAT-inclusive) + bank charge IDR 5,000 (not taxed).
```
Dr  Internet Expense     2,702,702
Dr  Bank Charges             5,000
Dr  Input VAT              297,298
    Cr  Accounts Payable       3,005,000
```
> General purchase pattern: **Dr Inventory/Expense + Dr Input VAT | Cr Accounts Payable.** If there's
> a **withholding tax (PPh 23)** (e.g. on services), it appears at the bottom and reduces the cash paid
> at settlement. The **Show Journal** button displays this journal for verification.

---

*The flow and logic above complete the Purchase module framework.*
