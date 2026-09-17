# Quick Tips for Finding Discrepancies (Reconciliation & Journals) — Simple Language

> Practitioner tricks to **quickly guess the cause of a discrepancy** without checking every
> transaction one by one. Useful during **bank reconciliation** or whenever numbers don't match.
> Written for general users. *(Curated by a practicing accountant.)*

---

## Trick 1: Difference divisible by 9 → likely a **transposed number**

If there's a discrepancy and the amount is **divisible by 9 (no remainder)**, it's usually not a
missing transaction — but **two digits swapped places** when the number was written.

**Example:**
- Should be `24,000`, written as `42,000` → difference **18,000**. 18,000 ÷ 9 = 2,000 → divisible by 9. ✓
- The digits 2 and 4 simply **swapped positions**.

**How to use it:** as soon as you find a discrepancy, **divide by 9 first**. If it divides evenly,
don't waste time hunting for a missing transaction — look for a number written **backwards** (e.g.
1,360 vs 1,630, difference 270, also divisible by 9).

**Bonus:** the quotient shows the **difference between the swapped digits**. Example: 18,000 ÷ 9 =
2,000 → the swapped digits differ by 2 (i.e. 4 − 2). So you just look for the matching pair.

---

## Trick 2: Difference is exactly **double** → likely a **wrong debit/credit side**

If the discrepancy is **exactly twice** the value of some transaction, the amount was probably
**recorded on the wrong side** — it should have been a **debit** but went to **credit** (or vice
versa).

Why double? Because the amount isn't just "missing" from the correct side, it also "adds" to the
wrong side — the effect is doubled.

**Important practice note:** within **a single journal voucher**, this is usually **caught
immediately** because the system **refuses to save** a voucher that isn't balanced (total debits ≠
total credits). So a wrong-side error most often slips through not inside one voucher, but when
**comparing against another record** (e.g. book balance vs the bank statement).

**How to use it:** if the difference is even, try **dividing by 2**. If the result matches a
transaction you recognize, check that transaction — its debit and credit may be swapped.

---

## Quick summary

| If the difference... | Likely cause | Step |
|---|---|---|
| **Is divisible by 9** | Transposed number (digits swapped) | Look for a number written backwards |
| **Is exactly 2× a transaction** | Wrong debit/credit side | Divide by 2, check the matching transaction |

> **Bottom line:** before checking one by one, **look at the pattern of the difference first**.
> Divisible by 9 → transposed number. Double → wrong debit/credit side. These small tricks save a
> lot of time during reconciliation.
