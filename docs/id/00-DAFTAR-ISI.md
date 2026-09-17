# Daftar Isi — Knowledge Akuntansi (Bahasa Indonesia)

Kurasi akuntan praktik (Tere). Semua contoh **anonim** & double-entry **balance**.
Versi Inggris ada di [`docs/en/`](../en/).

## Fondasi
1. [Cara Kerja Sistem Akuntansi](cara-kerja-sistem-akuntansi.md) — setup (master data, saldo awal, pajak) + **5 Buku Besar** + auto-jurnal + filosofi voucher→auto-jurnal.
2. [Bentuk Laporan Keuangan & Aturan Debit-Kredit](bentuk-laporan-keuangan.md) — persamaan dasar, **saldo normal (hafalan)**, 3 laporan (Neraca/L-R/Perubahan Modal) & keterkaitannya, kenapa selalu imbang.
3. [Struktur COA: Tipe Akun, Parent & Child](struktur-coa-tipe-parent-child.md) — 16 tipe akun (+saldo normal & laporan), parent vs child (sub-account of), contoh berjenjang.

## Panduan Sederhana (untuk pengguna non-akuntan)
- [Dari Input Transaksi sampai Laporan Keuangan](alur-entry-ke-laporan.md) — penjelasan bahasa sehari-hari: satu faktur penjualan → jurnal otomatis → Buku Besar → Laporan Keuangan. Staf tak harus mahir akuntansi; manajer yang wajib paham.

## Persiapan / Setup
3b. [Modul Setup / Persiapan Awal (Tahap 1)](modul-setup-persiapan.md) — menu Setup: Company Info, Preferences, **User Access Rights** (kontrol internal/segregation of duties), Quick Setup, Form Templates.

## Modul Transaksi (kerangka + logika auto-jurnal)
4. [Modul Pembelian (Purchase)](modul-purchase-kerangka.md) — Procure-to-Pay 6 langkah; jurnal di **Purchase Invoice** (`Dr Persediaan | Cr Utang Usaha`); Payment; Return=reversal.
5. [Modul Penjualan (Sales)](modul-sales-kerangka.md) — Order-to-Cash 6 langkah; jurnal di **Sales Invoice** (`Dr Piutang | Cr Pendapatan +PPN` **&** `Dr HPP | Cr Persediaan`); Receipt; Return=reversal.

## Studi Kasus (Pengendalian Internal / Temuan Audit)
6. [Studi Kasus Pengendalian Internal](studi-kasus-pengendalian-internal.md) —
   - #1 Kas kecil imprest membengkak & bon gantung
   - #2 Beban THR disembunyikan sebagai biaya dibayar dimuka (laba semu)
   - #3 AR macet 8 bulan (krisis likuiditas)
   - #4 Salah pricing (overhead tak dihitung → rugi struktural)

## Data Latih (JSONL) — [`data/`](../../data/)
`accounting_process.jsonl` · `financial_statements.jsonl` · `coa_structure.jsonl` ·
`purchase_module.jsonl` · `sales_module.jsonl` · `internal_control_cases.jsonl`

## Menyusul (pending)
- Detail **Tahap 1 (Persiapan)** setup.
- **SS field entry** modul Purchase & Sales (untuk finalisasi field).
- Konfirmasi arah repo dari owner (studi kasus pengalaman).
