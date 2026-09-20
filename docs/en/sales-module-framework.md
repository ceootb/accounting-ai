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

---

## 6. Sales Invoice — Field Data Entry Detail

The entry screen is built so the **user only picks data** (via **dropdowns ▼** and **search option**
that link to master data); the system **computes Amount/VAT/Total and creates the journal
automatically**.

**a) Header — parties & document:**
- **Customer** ▼ — links to the **customer master**; auto-pulls Bill To/Ship To, Terms, and default AR.
- **Select DO / Select SO** (search) — links to the **Delivery Order / Sales Order** voucher. **Optional:**
  if a DO is entered, items are pulled from the DO; if not, **Finance** enters directly on the Sales
  Invoice to **recognize the Receivable**.
- **Cust. is Taxable** ☑ and **Inclusive Tax** ☑ — whether the customer is taxable & whether prices
  already include VAT.
- **Bill To / Ship To** — billing & shipping address (▼).
- **PO No.**, **Invoice No.** (auto), **Invoice Date**, **Ship Date**, **FOB**, **Terms** ▼ (e.g.
  C.O.D), **Ship Via** ▼.
- **Template** ▼ (A4 / A4 FULL / Sales Invoice) & **Preview** ▼ (Preview / Printer / VAT Invoice).

**b) Item grid** (tabs **# Items** / **Down Payment**):
- **Item** ▼ / search — links to the **item master**; pulls description, price, and COA (revenue/inventory/COGS).
- **Item Description**, **Qty**, **Item Unit**, **Unit Price**, **Disc %**, **Tax** (T = taxable),
  **Amount** (auto = Qty × Unit Price − Disc), **Dept.** ▼ (cost/profit center), **SN** (serial/batch).

**c) Footer — tax, account & totals:**
- **Inv. Tax No** + tax invoice number + date.
- **Description** — transaction note.
- **AR Account** ▼ — pick the **Receivable** account: AR Trade, AR Nontrade, AR Affiliates,
  AR Employee, AR Officers, AR Others, or Advance Payment.
- **Sub Total** (auto), **Discount** (value / %), **VAT** (auto), **Freight**, **Total Invoice** (auto).
- Status: Balance, Paid, Paid Disc, Withholding (PPh 23), Return.
- Buttons: **Pay**, **Print**, **Save & New**, **Save & Close**, **Cancel**.
- Toolbar: **Get from Memorize**, **Recurring**, **Sales Receipt**, and **Show Journal** (view the
  auto-generated journal).

**d) The auto-journal produced** (example: *Inclusive Tax*, Total Invoice IDR 450,000):

*Entry 1 — revenue recognition (from header + total):*
```
Dr  Accounts Receivable (AR)       450,000
    Cr  Output VAT                       44,594
    Cr  Sales Revenue                   405,406
```
*Entry 2 — COGS recognition (from item × cost):*
```
Dr  COGS                           234,000
    Cr  Inventory                       234,000
```
> Because of **Inclusive Tax**, VAT is stripped out of the total (450,000 − 44,594 = 405,406 net
> revenue). One Sales Invoice → **two balanced journal entries** at once (revenue + COGS), with no
> manual journaling. The **Show Journal** button displays this Transaction Journal for verification.

---

## 7. Sales Receipt (Customer Payment) — Field Data Entry Detail

**Sales Receipt = recording money in when a customer pays an invoice.** It opens from the **Sales
Invoice screen → "Sales Receipt"**, so many fields are **auto-filled** from the
invoice. The screen is called **Cust. Receipt**. Many fields fill in by themselves; the user just completes the rest.

**a) Top section — from whom & when:**
- **Received From** — **auto-filled** with the customer name (pulled from the Sales Invoice).
- **Form No.** — receipt number (auto). **Payment Date** — the date money was received.

**b) Receiving-account section — where the money lands:**
- **Bank** — the cash/bank account that **receives** the money. It can be a normal bank account, or a
  special **Cash in Transit (CIT)** account — see the note below.
- **Cheque No. / Cheque Date** (if paid by cheque), **Currency / Rate** (if foreign currency).
- **Cheque Amount** — the amount received; **Distribute Amount** — the amount allocated to invoices.

**c) Paid-invoices grid:**
- **Invoice No., Date, Amount, Owing, Payment Amount (auto), Total Disc., Paid (tick when settled),
  Discount Date.** The **Paid** and **Payment Amount** columns auto-fill based on the selected invoice.
- **Memo** — a note.
- Buttons: **Print, Save & New, Save & Close, Cancel.**

**d) The auto-journal produced** (example: settlement of IDR 15,300,000):
```
Dr  Receiving Cash/Bank (e.g. Cash in Transit)   15,300,000
    Cr  Accounts Receivable (AR)                      15,300,000
```
> One simple entry: **cash/bank goes up, receivables go down.** This closes the sales cycle — the
> invoice that was "unpaid" is now settled.

---

### Special note: the **Cash in Transit (CIT)** account for retail sales

For **retail sales** with high volume, receipts can be directed to a **temporary holding account**
called **Cash in Transit (CIT)** — not straight to the bank. The goal is to **aggregate** retail
receipts so you **don't have to enter each one**, because the marketing team already issues its own
**OR (Official Receipt)** for each retail customer. The CIT balance is later "cleared" to the bank
when the actual deposit comes in.

> Full detail of this technique is in [Tips: CIT for Aggregating Retail Sales](tips-cit-retail-aggregation.md).

---

*The flow and logic above complete the Sales module framework.*
