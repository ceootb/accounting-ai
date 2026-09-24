# Fixed Asset Disposal

Disposal is **not merely deleting an asset from the list**. It is **one workflow** that changes the
asset's **status**, moves its **historical record**, and **automatically generates the journal** up to
the **gain/loss on disposal** — **without the user writing any manual journal**.

## 1. How it works (workflow)

- Disposal is done **directly from the asset** to be sold (the **Dispose** button on that asset).
- The user simply enters the **sale value (proceeds)**.
- The user does **not** create the disposal journal manually — the **system generates it
  automatically**. That journal is *auto-generated* and **hidden** from the user.

## 2. Status change & historical record

- After processing, the asset **no longer appears** in the **active Fixed Assets list**.
- The **asset data is not lost** — it moves to the **Fixed Assets Disposal** menu as a **historical
  disposal record**, so the transaction **remains traceable**.

## 3. Accounting treatment (done automatically)

When the asset is sold, the system automatically:
1. **Removes the cost / original value** of the asset from Fixed Assets.
2. **Reverses the Accumulated Depreciation** formed **up to the period before disposal**.
3. **Records the proceeds / sale value**.
4. **Computes the difference** as **Gain or Loss on Fixed Asset Disposal**.

**The journal (concept):**
```
Dr  Cash/Bank                          (proceeds / sale value)
Dr  Accumulated Depreciation           (balance up to period before disposal)
    Cr  Fixed Asset (original cost)      (cost)
    Cr  Gain on Fixed Asset Disposal     (if a gain)   ── or ──
Dr  Loss on Fixed Asset Disposal       (if a loss)
```

## 4. Limit of the Accumulated Depreciation reversal

The accumulated-depreciation reversal is **only up to YTD of the period before the asset is sold** —
**not** depreciation for periods after disposal.

> **Example:** the asset is sold in **September** → the accumulated depreciation reversed = **YTD
> through August**. Depreciation for **September and later is not formed / reversed**, because the
> asset has been disposed of.

## 5. Gain / Loss account

The difference between the asset's **carrying amount / net book value (NBV)** and the **sale value**
goes to the **Gain or Loss on Fixed Asset Disposal** account, with **parent account Other Income**.

- **NBV = original cost − accumulated depreciation** (up to the period before disposal).
- **Proceeds > NBV → Gain**; **Proceeds < NBV → Loss**.

## Worked example

Asset: original cost **IDR 120m**, accumulated depreciation through August **IDR 90m** → **NBV IDR
30m**. Sold in September for **IDR 40m** → **Gain IDR 10m** (40 − 30).

```
Dr  Cash/Bank                          40m
Dr  Accumulated Depreciation           90m
    Cr  Fixed Asset (original cost)     120m
    Cr  Gain on Fixed Asset Disposal    10m      (Other Income)
```
*(If sold for IDR 25m → Loss IDR 5m: `Dr Loss on Fixed Asset Disposal 5m` replaces the gain line; the
entry still balances.)*

> **Bottom line:** disposal = a workflow that **changes the asset status + moves the historical record
> + auto-journals** (remove cost, reverse accumulated depreciation up to before disposal, record
> proceeds, compute gain/loss) — **with no manual journal**. See also [Fixed Asset Module](fixed-asset-module.md).
