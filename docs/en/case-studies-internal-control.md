# Case Studies — Internal Control (Real Findings)

> A collection of **real, anonymized cases** from the practice of an accounting head.
> Goal: train the model to recognize **red flags**, understand **controls**, and know the correct
> accounting **treatment** — not just theory. All names/entities are removed.

---

## Case 1 — Petty Cash Ballooning (Imprest / Fixed-Fund Method)

**Context:** A cleaning-service company. Found in the first week after a new *accounting head* joined.

**Findings:**
- The **Petty Cash** ledger showed a balance of about **IDR 100 million**.
- Yet the director's policy was an **imprest (fixed-fund) method** of **IDR 10 million**.
- Physical **cash count (opname)**: the cash on hand was **less than IDR 10 million** (far below).
- Many **outstanding advances (bon gantung)** — cash taken in advance **with no settlement/receipt**.
- A prior audit had **not** found any issue in finance/accounting.

**Principle violated:**
- Under the **imprest** method, the Petty Cash ledger balance must **ALWAYS equal the fixed fund
  (IDR 10 million)**. Only its **composition** changes: `physical cash + supported vouchers` = fixed fund.
  Replenishment covers **only what was spent and documented**.
- A ledger ballooning to IDR 100 million → replenishment was done **without clearing vouchers**,
  meaning the imprest method was not actually applied (negligence or misuse).
- **Outstanding advances** should be **reclassified to Advances / Employee Receivable**, not left
  piling up in Petty Cash.

**Red flags:**
1. Petty Cash ledger balance **≠** the fixed fund amount.
2. Physical **cash count** does not reconcile under the imprest formula.
3. **Advances outstanding** for a long time with no receipt/settlement.

**How to verify (imprest reconciliation):**
```
Physical cash (count) + Supported vouchers (not yet replenished) + Unsettled advances = Fixed Fund
```
If it doesn't balance → there is a difference to investigate.

**Accounting treatment (reclassify outstanding advances):**
```
Dr  Advances / Employee Receivable
    Cr  Petty Cash
```

**Lessons:**
- **Document review alone is not enough** — records can look tidy. A **surprise cash count** plus
  imprest reconciliation is required to surface a physical shortfall.
- **Proper controls:** fixed imprest fund; documented replenishment; a **settlement deadline** for
  advances; separate advances into a Receivable/Advance account.

---

## Case 2 — Expense Hidden as "Prepaid Expense" (Fictitious Profit)

**Context:** The same company. Recently **acquired by new management** from a former owner facing
a **liquidity crisis** — yet, oddly, the financial statements showed a **PROFIT**. The new
management's auditor (before the accounting head joined) had not found the error either.

**Finding:** A **Prepaid Expense** account worth **hundreds of millions** actually contained
**employee THR (holiday allowance) expense** — an expense already incurred, **not** a future-benefit asset.

**Principle violated:** THR is a **current-period expense** (recognized when the obligation arises/
is paid), **not** a prepaid item. Parking it in *prepaid* **defers/hides the expense** →
**overstated (fictitious) profit**.

**Correction / reclass:**
```
Dr  Employee THR Expense
    Cr  Prepaid Expense
```
**Impact:** the P&L **automatically drops** — here it turned into a **large loss**. HQ's board
finally understood they had bought a **company that was actually deeply loss-making**, not profitable.

**Red flags:**
1. Company in a **liquidity crisis** but FS shows **profit** — an inconsistency (healthy profit
   should come with healthy cash flow).
2. **Prepaid / deferred asset accounts ballooning** unnaturally.
3. The *prepaid* account actually holds an **already-incurred expense** (THR), not a future benefit.

**Lessons:**
- **Open up the detail of prepaid / deferred accounts** — confirm they are truly future benefits,
  not hidden expenses.
- **Reconcile Profit vs Cash Flow:** large profit but tight cash = a manipulation signal.
- **Acquisition due diligence** must dissect account details, not just review summary FS.
