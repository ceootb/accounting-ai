# Fixed Asset Revaluation — Revaluation Model (PSAK 16)

> **PSAK / ideal-accounting version** (for review). The **tax/fiscal** treatment is covered
> **separately** (see the note below). The software UI/UX steps & comparison will follow (Tere's
> simulation).

After initial recognition, PPE can be measured under **two models**:
- **Cost model** — carried at **cost − accumulated depreciation − impairment**.
- **Revaluation model** — carried at **fair value at the revaluation date**, less subsequent
  **accumulated depreciation & impairment** (provided fair value can be measured reliably).

## Principles

- Revaluations are made **regularly enough** that the carrying amount **doesn't differ materially** from
  fair value.
- **The entire class of assets is revalued** (e.g. all Land, or all Buildings) — **not** cherry-picking a
  single asset.

## Accumulated depreciation at revaluation (two methods)

1. **Proportional (gross-up)** — gross cost & accumulated depreciation are **restated proportionately** so
   the net book value equals the revalued amount.
2. **Elimination (net)** — accumulated depreciation is **eliminated** against gross cost first, then the
   net book value is adjusted to fair value.

## Journal at revaluation

**Increase (revaluation surplus):** recognized in **Other Comprehensive Income (OCI)** and accumulated in
equity as **Revaluation Surplus** — **except** to the extent it **reverses** a previous revaluation
decrease of the same asset recognized in **profit or loss**, which is then recognized in **profit or
loss**.

**Example (elimination method):** cost **IDR 100m**, accumulated depreciation **IDR 40m** → NBV **IDR
60m**; fair value **IDR 90m** → **surplus IDR 30m**:
```
Dr  Accumulated Depreciation    40m
    Cr  Fixed Asset              40m      (eliminate → NBV 60m)
Dr  Fixed Asset                 30m
    Cr  Revaluation Surplus (OCI) 30m     (raise to fair value 90m)
```

**Decrease (revaluation decrease):** recognized as an **expense in profit or loss** — **except** if there
is a **Revaluation Surplus balance** for that asset, the decrease **reduces the surplus first** (via OCI),
and only the remainder goes to profit or loss.

## After revaluation

- **Subsequent depreciation** is based on the **revalued amount** over the **remaining useful life**.
- The **Revaluation Surplus** may be **transferred to Retained Earnings** — when the asset is
  **derecognized**, or **as the asset is used** (the difference between depreciation on the revalued
  amount vs on the original cost). This transfer does **not** go through profit or loss.

## Tax note (SEPARATE)

> Commercial **(PSAK)** revaluation is **not automatically** a **fiscal** revaluation. Tax-purpose
> revaluation has its **own rules** (e.g. the relevant PMK), with its own conditions & final income-tax
> rate. **Do not mix** the two — the difference is settled in **tax reconciliation**, not by changing the
> commercial journal. (See [Tax Strategy & Fiscal Correction](tax-strategy-fiscal-correction.md).)

---

*Note: this page is a **general/ideal PSAK concept** for reference & review, not a substitute for the
official standard/rules. Figures are illustrative. The specific tax treatment & software steps are
confirmed separately.*
