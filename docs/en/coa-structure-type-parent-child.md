# COA Structure: Account Type, Parent & Child Accounts

> How to structure the Chart of Accounts correctly: every account has an **Account Type**, and can be
> a **parent** or a **child** (*sub-account of*). The account type determines its **normal balance** &
> **target statement** — see [financial-statements.md](financial-statements.md).

---

## 1. Account Type — 16 standard types

Every account **must** have one type. The type sets the normal balance (Debit/Credit) and which
statement the account appears in (Balance Sheet / Income Statement).

| Type (EN) | Indonesian | Normal Balance | Statement |
|---|---|---|---|
| Cash/Bank | Kas/Bank | Debit | Balance Sheet |
| Account Receivable | Piutang Usaha | Debit | Balance Sheet |
| Inventory | Persediaan | Debit | Balance Sheet |
| Other Current Asset | Aset Lancar Lainnya | Debit | Balance Sheet |
| Fixed Asset | Aset Tetap | Debit | Balance Sheet |
| Accumulated Depreciation | Akumulasi Penyusutan | Credit | Balance Sheet (contra-asset) |
| Other Asset | Aset Lainnya | Debit | Balance Sheet |
| Account Payable | Utang Usaha | Credit | Balance Sheet |
| Other Current Liability | Utang Lancar Lainnya | Credit | Balance Sheet |
| Long Term Liability | Utang Jangka Panjang | Credit | Balance Sheet |
| Equity | Ekuitas | Credit | Balance Sheet / Changes in Equity |
| Revenue | Pendapatan | Credit | Income Statement |
| Cost of Goods Sold | Beban Pokok Penjualan (HPP) | Debit | Income Statement |
| Expense | Beban | Debit | Income Statement |
| Other Expense | Beban Lain-lain | Debit | Income Statement |
| Other Income | Pendapatan Lain-lain | Credit | Income Statement |

---

## 2. Parent Account vs Child Account

- **Parent account** = header/summary account (e.g. **Cash/Bank**).
- **Child account** = detail under a parent, flagged as **"Sub Account of"** that parent.
- A **child inherits the type** of its parent; the **parent balance = sum of all its children**.
- **Transactions are posted to the child** (most detailed account); the parent is used for
  **summary in reports**.

**Example:**
```
Cash/Bank                      (PARENT — type Cash/Bank)
 ├─ Main Cash                  (child / sub-account of Cash/Bank)
 ├─ Petty Cash                 (child)
 ├─ Bank BCA                   (child)
 ├─ Bank CIMB                  (child)
 └─ Bank Mega                  (child)
```

---

## 3. Sample tiered COA (property / trading company — illustration)

```
Account Receivable             (PARENT)
 ├─ Trade Receivable
 ├─ Mortgage/Bank Receivable
 └─ Retention Receivable

Inventory                      (PARENT)
 ├─ Merchandise Inventory
 ├─ Work in Process (WIP)
 └─ Finished Units

Account Payable                (PARENT)
 ├─ Trade Payable
 └─ Accrued Expense

Expense                        (PARENT)
 ├─ Salary Expense
 ├─ Electricity & Water
 ├─ Rent Expense
 └─ Maintenance Expense
```
*(Same pattern used when drafting an initial COA for a property company before the client sends their
final version — parents as the skeleton, children per real needs.)*

---

## 4. Why this structure matters

- **Clean, tiered reports:** parents for summary, children for detail.
- **Correct auto-journaling & mapping:** transactions go to the right child; the system knows its type
  and normal balance, so journals land on the correct statement line automatically.
- **Consistency:** account type keeps normal balance & statement classification correct across all accounts.
