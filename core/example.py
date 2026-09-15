"""Demo: engine mengunci kebenaran jurnal yang (misalnya) diusulkan AI.
Jalankan: python -m core.example
"""
from core import ChartOfAccounts, JournalEntry, split_inclusive

coa = ChartOfAccounts.default_id()
print("COA jumlah akun:", len(coa))

# Penjualan tunai Rp1.110.000 TERMASUK PPN 11%
dpp, tax = split_inclusive(1_110_000)
je = JournalEntry("Penjualan tunai termasuk PPN 11%")
je.add("1-101", debit=1_110_000)   # Kas
je.add("4-101", credit=dpp)        # Penjualan
je.add("2-102", credit=tax)        # PPN Keluaran
je.assert_valid(coa)               # <- error kalau tidak balance / akun tak ada
print(f"OK balanced | DPP={dpp} PPN={tax} | debit={je.total_debit} kredit={je.total_credit}")

# Contoh AI ngaco (tidak balance) -> engine MENOLAK
bad = JournalEntry("salah (tidak balance)")
bad.add("1-101", debit=1000); bad.add("4-101", credit=900)
print("Deteksi error:", bad.validate(coa))
