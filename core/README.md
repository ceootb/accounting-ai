# core — Master Accounting Engine (deterministic backbone)

Lapisan yang **harus pasti benar**, bukan ditebak AI: COA, aturan double-entry,
validasi balance, perhitungan pajak (PPN). Model AI **mengusulkan** jurnal; engine
ini **mengunci kebenarannya**. Reusable untuk edge AI, app UMKM, enterprise.

```python
from core import ChartOfAccounts, JournalEntry, split_inclusive
coa = ChartOfAccounts.default_id()
dpp, ppn = split_inclusive(1_110_000)          # harga termasuk PPN 11% -> DPP, PPN
je = JournalEntry("Penjualan tunai + PPN")
je.add("1-101", debit=1_110_000).add("4-101", credit=dpp).add("2-102", credit=ppn)
je.assert_valid(coa)                           # raise kalau tak balance / akun tak ada
```

Coba: `python -m core.example`

**TODO (butuh arahan ibu Tere):** COA penuh (kelompok & sub-akun), akun kontra
(mis. Akumulasi Penyusutan = saldo normal kredit), aturan pajak lengkap (PPh 21/23/final),
posting ke buku besar & laporan.
