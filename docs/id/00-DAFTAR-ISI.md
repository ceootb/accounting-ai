# Daftar Isi — Knowledge Akuntansi (Bahasa Indonesia)

Kurasi akuntan praktik (Tere). Semua contoh **anonim** & double-entry **balance**.
Versi Inggris ada di [`docs/en/`](../en/).

## Fondasi
1. [Cara Kerja Sistem Akuntansi](cara-kerja-sistem-akuntansi.md) — setup (master data, saldo awal, pajak) + **5 Buku Besar** + auto-jurnal + filosofi voucher→auto-jurnal.
2. [Bentuk Laporan Keuangan & Aturan Debit-Kredit](bentuk-laporan-keuangan.md) — persamaan dasar, **saldo normal (hafalan)**, 3 laporan (Neraca/L-R/Perubahan Modal) & keterkaitannya, kenapa selalu imbang.
2b. [Format 3 Laporan Keuangan Inti](format-laporan-keuangan.md) — template baris demi baris Laba Rugi, Perubahan Modal, & Neraca (acuan PSAK); contoh angka balance. Laporan = tarikan saldo Buku Besar, bukan transaksi baru.
3. [Struktur COA: Tipe Akun, Parent & Child](struktur-coa-tipe-parent-child.md) — 16 tipe akun (+saldo normal & laporan), parent vs child (sub-account of), contoh berjenjang.

## Panduan Sederhana (untuk pengguna non-akuntan)
- [Menyiapkan Data Setup Sebelum Transaksi](persiapan-sebelum-transaksi.md) — kenapa Company Info, Preferences (peta akun), & User Profile disiapkan dulu; analogi "menyiapkan dapur". Data rapi di depan → laporan otomatis di belakang.
- [Dari Input Transaksi sampai Laporan Keuangan](alur-entry-ke-laporan.md) — penjelasan bahasa sehari-hari: satu faktur penjualan → jurnal otomatis → Buku Besar → Laporan Keuangan. Staf tak harus mahir akuntansi; manajer yang wajib paham.
- [Tips: CCA (Cash Clearing Account) untuk Gunggung Penjualan Retail](tips-cca-gunggung-retail.md) — penerimaan retail (cafe/resto) ditampung di akun perantara CCA lewat JV harian, digunggung jadi 1 Sales Invoice akhir bulan untuk pajak; CCA wajib nol akhir bulan. (Tips hemat waktu, bukan teori baku; catatan istilah CIT vs CCA vs suspense/sundry.)
- [Tips: Recurring (Transaksi Berulang Otomatis)](tips-recurring.md) — voucher rutin (SI/PI/JV) dibuat berkala otomatis; contoh komisi bulanan, PAM/PLN/Telp, tax allowance PPh 21. Perpanjang periode dulu.
- [Tips: Setting PPN & Split PI Beda Periode](tips-ppn-setting-split-pi.md) — PPN dari master vendor; pecah 2 PI (DPP di periode beban + PPN di periode faktur pajak) lalu bayar bersamaan.
- [Tips: Jurnal Potongan PPh 23](tips-pph23-jurnal.md) — dua sisi: memotong (beli jasa → Utang PPh 23) vs dipotong (jual jasa → kurang bayar → Prepaid PPh 23).
- [Tips Cepat Mencari Selisih](tips-cari-selisih.md) — trik praktik: selisih habis dibagi 9 = angka terbalik (transposisi); selisih 2× = salah sisi debit/kredit. Berguna saat rekonsiliasi bank.

## Persiapan / Setup
3b. [Modul Setup / Persiapan Awal (Tahap 1)](modul-setup-persiapan.md) — menu Setup: Company Info, Preferences, **User Access Rights** (kontrol internal/segregation of duties), Quick Setup, Form Templates.

## Modul Transaksi (kerangka + logika auto-jurnal)
4. [Modul Pembelian (Purchase)](modul-purchase-kerangka.md) — Procure-to-Pay 6 langkah; jurnal di **Purchase Invoice** (`Dr Persediaan | Cr Utang Usaha`); Payment; Return=reversal.
5. [Modul Penjualan (Sales)](modul-sales-kerangka.md) — Order-to-Cash 6 langkah; jurnal di **Sales Invoice** (`Dr Piutang | Cr Pendapatan +PPN` **&** `Dr HPP | Cr Persediaan`); Receipt; Return=reversal.
5b. [Modul General Ledger — Journal Voucher (JV)](modul-general-ledger-jv.md) — buku besar ke-5; **jurnal manual** untuk adjustment/koreksi (amortisasi prepaid, settlement uang muka); harus balance; akses supervisor/manager.
6. [Modul Aset Tetap (Fixed Asset)](modul-fixed-asset.md) — 3 sub-modul (kelompok pajak → kategori → daftar aset); akun perantara **Fixed Asset Transaction**; **penyusutan otomatis tiap bulan via "Period End"** (`Dr Beban Penyusutan | Cr Akumulasi Penyusutan`); tabel kelompok fiskal RI (UU PPh 11/PMK 72/2023).
7. [Proses Tutup Periode (Period End)](proses-tutup-periode-period-end.md) — satu klik saat tutup bulan; auto-jurnal **penyusutan aset** + **revaluasi selisih kurs** (Realized/Unrealized). Dijalankan setelah transaksi lengkap & rekonsiliasi nol.

## Laporan & Riwayat Transaksi
- [Riwayat Transaksi per Akun & Laporan Piutang (AR / Customer)](laporan-riwayat-akun-ar.md) — **Account History** (rekap transaksi per akun, data grid + filter); laporan AR yang sering dipakai (Outstanding Invoices, Aging Summary/Detail, **AR Sub Ledger Detail**); konsep **Sub Ledger** AR/AP (1 akun kontrol + buku pembantu per customer/vendor, COA tetap ramping). *(EN: `account-history-ar-reports.md`.)*

## Studi Kasus (Pengendalian Internal / Temuan Audit)
6. [Studi Kasus Pengendalian Internal](studi-kasus-pengendalian-internal.md) —
   - #1 Kas kecil imprest membengkak & bon gantung
   - #2 Beban THR disembunyikan sebagai biaya dibayar dimuka (laba semu)
   - #3 AR macet 8 bulan (krisis likuiditas)
   - #4 Salah pricing (overhead tak dihitung → rugi struktural)

## Data Latih (JSONL) — [`data/`](../../data/)
`accounting_process.jsonl` · `financial_statements.jsonl` · `coa_structure.jsonl` ·
`purchase_module.jsonl` · `sales_module.jsonl` · `setup_module.jsonl` ·
`general_ledger_jv.jsonl` · `fixed_asset_module.jsonl` · `bank_reconciliation.jsonl` ·
`internal_control_cases.jsonl`

## Menyusul (pending)
- **Buku Besar Utang (GL A/P) + Sub-GL per vendor.**
- **Dispose & Revaluation** aset tetap.
- **Setting PPN di Sales Invoice** (paralel dengan sisi Purchase).
