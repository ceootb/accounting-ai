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
