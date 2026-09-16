# Sales Module — Framework & Logic

> The **Order-to-Cash** cycle and its accounting logic. Focus on **flow + logic + auto-journal**
> first; **entry field details to follow.** *(Curated by a practicing accountant.)*

---

## 0. Setup Prerequisite

**Items are configured with a selling price** and **linked to a Sales Revenue COA** (revenue side)
plus an **Inventory COA** (for COGS). **VAT is calculated automatically** — choose **Including VAT**
or **Excluding VAT** at entry.

---

## 1. The 6-Step Flow (Order-to-Cash)

```
1. Sales Quotation (SQ)   — quote to the customer
2. Sales Order (SO)       — customer order (sales approval)
3. Delivery Order (DO)    — goods shipped by warehouse (pulls SO data)
4. Sales Invoice          — sales invoice (pulls DO data)
5. Sales Return           — sales return (if any)
6. Sales Receipt          — payment received
```

---

## 2. Journaling Logic per Step

| Step | Journal? | Auto-journal | Notes |
|---|---|---|---|
| **1. Sales Quotation** | ❌ No | — | Record & **approval** by sales dept/manager. No financial impact. |
| **2. Sales Order** | ❌ No | — | Customer order (approval). No journal. |
| **3. Delivery Order** | ⚪ Warehouse record | — (journal at Sales Invoice) | Goods shipped by **warehouse** by **pulling the SO**. No accounting journal yet. |
| **4. Sales Invoice** | ✅ Yes (2 journals) | **Revenue:** `Dr Accounts Receivable` \| `Cr Sales Revenue` (+ `Cr Output VAT` if a tax invoice). **COGS:** `Dr COGS` \| `Cr Inventory` | **Pulls DO** on entry. Recognizes revenue **and** COGS at once. |
| **5. Sales Return** | ✅ Yes | **Automatic reversal by the system** | Goods received back → system reverses the sales journal (revenue, VAT, AR, COGS, inventory). |
| **6. Sales Receipt** | ✅ Yes | `Dr Cash/Bank` \| `Cr Accounts Receivable` | On entry, input **received via bank/cash**; auto-journal settles the receivable. |

> **Key:** SQ & SO = record + approval (**no journal**). DO = **warehouse shipment** (pull SO, no
> journal yet). **The journal happens at Sales Invoice** — **two journals** at once: **revenue**
> (`Dr AR | Cr Sales Revenue (+Output VAT)`) and **COGS** (`Dr COGS | Cr Inventory`). Closed at
> **Sales Receipt** (`Dr Cash/Bank | Cr AR`).

---

## 3. Key Logic Principles

1. **Item → COA setup:** selling price linked to **Sales Revenue**; cost linked to **Inventory** (for COGS).
2. **Automatic VAT:** the system computes Output VAT; choose **Including / Excluding VAT** at entry.
3. **Data flows:** SQ → SO → DO → Sales Invoice (keeps order ↔ delivery ↔ invoice consistent).
4. **Journal point = Sales Invoice**, recording **2 journals**: revenue + COGS.
5. **Return = automatic reversal** by the system.
6. **AR flow:** Sales Invoice increases AR → Sales Receipt decreases AR.

---

## 4. Purchase vs Sales Mirror

| | Purchase | Sales |
|---|---|---|
| At invoice | `Dr Inventory \| Cr Accounts Payable (+Input VAT)` | `Dr AR \| Cr Sales Revenue (+Output VAT)` **&** `Dr COGS \| Cr Inventory` |
| At cash | `Dr Accounts Payable \| Cr Cash/Bank` | `Dr Cash/Bank \| Cr Accounts Receivable` |

---

## 5. In One Breath

`SQ & SO = approval (no journal)` → `DO = ship goods, pull SO` →
`Sales Invoice = JOURNAL: (Dr AR | Cr Sales Revenue +Output VAT) & (Dr COGS | Cr Inventory)` →
`Sales Receipt = Dr Cash/Bank | Cr AR`. (Return = automatic reversal.)

*Sales entry field details to follow.*
