# Fixed Asset Disposal

Disposal is **not merely deleting an asset from the list**. It is **one workflow** that changes the
asset's **status**, moves its **historical record**, and **automatically generates the journal** up to
the **gain/loss on disposal** — **without the user writing any manual journal**.

## 1. How it works (workflow)

- Disposal is done **directly from the asset** to be sold (the **Dispose** button on that asset).
- The user simply enters the **sale value (proceeds)**; the account used is **Fixed Asset Transaction**
  (an **intermediary/clearing** account, same as when the asset was acquired — **not** a revenue account).
- The user does **not** create the disposal journal manually — the **system generates it
  automatically**. That journal is *auto-generated* and **hidden** from the user. After processing, the
  asset is stamped **DISPOSED**, and an **Undo Dispose** button remains available until **Period End**.

## 2. Status change & historical record

- After processing, the asset **no longer appears** in the **active Fixed Assets list**.
- The **asset data is not lost** — it moves to the **Fixed Assets Disposal** menu as a **historical
  disposal record**, so the transaction **remains traceable**.

## 3. Accounting treatment (done automatically)

Disposal runs in **two steps** through the intermediary **Fixed Asset Transaction** account:

**a) When the sale proceeds are received** (an ordinary receipt):
```
Dr  Cash/Bank
    Cr  Fixed Asset Transaction        (sale value / proceeds)
```

**b) When the disposal is executed** (auto-journal), the system automatically:
1. **Removes the cost / original value** of the asset from Fixed Assets.
2. **Reverses the Accumulated Depreciation** formed **up to the period before disposal**.
3. **Offsets** the **Fixed Asset Transaction** account (the proceeds received earlier).
4. **Computes the difference** as **Gain or Loss on Fixed Asset Disposal**.
```
Dr  Fixed Asset Transaction          (proceeds — offsets step a)
Dr  Accumulated Depreciation         (balance up to period before disposal)
    Cr  Fixed Asset (original cost)    (cost)
    Cr  Gain on Fixed Asset Disposal   (if a gain)   ── or ──
Dr  Loss on Fixed Asset Disposal     (if a loss)
```
> The **Fixed Asset Transaction** account nets to **zero** across the two steps: **credited** when
> proceeds are received, then **debited** on disposal. Cash does **not** enter the disposal journal
> directly — disposal goes only through the intermediary. *(Same pattern as acquisition: transaction →
> Fixed Asset Transaction → Fixed Asset.)*

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

**a) Receive proceeds:**
```
Dr  Cash/Bank                          40m
    Cr  Fixed Asset Transaction        40m
```
**b) Disposal executed:**
```
Dr  Fixed Asset Transaction            40m      (offsets proceeds)
Dr  Accumulated Depreciation           90m
    Cr  Fixed Asset (original cost)     120m
    Cr  Gain on Fixed Asset Disposal    10m      (Other Income)
```
> Fixed Asset Transaction: Cr 40m (step a) + Dr 40m (step b) = **zero**. Net gain IDR 10m.
> *(If sold for IDR 25m → Loss IDR 5m: `Dr Loss on Fixed Asset Disposal 5m` replaces the gain line; the
> entry still balances.)*

> **Bottom line:** disposal = a workflow that **changes the asset status + moves the historical record
> + auto-journals** (remove cost, reverse accumulated depreciation up to before disposal, **proceeds via
> the Fixed Asset Transaction clearing account**, compute gain/loss) — **with no manual journal**. See
> also [Fixed Asset Module](fixed-asset-module.md).
