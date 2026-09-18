# Cara Kerja Sistem Akuntansi (untuk User & Perusahaan)

> Panduan praktik: **bagaimana software akuntansi disiapkan dan bekerja**, supaya
> perusahaan bisa dijalankan bahkan oleh staf akuntansi **junior / fresh graduate** —
> cukup input lewat **voucher**, dan **jurnal terbentuk otomatis (auto-jurnal)**.
> Konsep debit/kredit "disembunyikan" di balik voucher, sehingga tidak perlu
> merekrut akuntan senior hanya untuk operasional harian.
>
> Dikurasi oleh akuntan praktik (20+ tahun, akuntansi Indonesia).

---

## Bagian 1 — Persiapan Awal (Setup)

Urutan menyiapkan software akuntansi untuk sebuah perusahaan:

### Tahap 1 — Persiapan (Setup)
Konfigurasi awal di menu **Setup**: Company Info, Preferences, User Profile & Hak Akses,
Change Password, Quick Setup, Form Templates. Detail: [modul-setup-persiapan.md](modul-setup-persiapan.md).

### Tahap 2 — Menyiapkan Master Data
Siapkan daftar master **sebelum** bisa bertransaksi. Contoh daftar:
- **COA** (Bagan Akun / Chart of Accounts)
- **Daftar Customer** (Nasabah / Pelanggan)
- **Daftar Vendor** (Pemasok)
- **Daftar Departemen** — untuk *costing*: **Business Unit** vs **Cost Center**
- **Daftar Item** — *inventory part* / *non-inventory part* / *service*
- **Fixed Asset** (Aset Tetap)
- (lainnya menyusul bila ada update)

### Tahap 3 — Saldo Awal
- Diperlukan **hanya jika ada migrasi data** — perusahaan sudah punya software akuntansi lama.
- Jika perusahaan **baru / belum punya data** → **tidak perlu** saldo awal.

### Tahap 4 — Setup Pajak
- **PPN 11%**.
- **PPh** → tergantung **jenis biaya** dan **jenis Wajib Pajak (WP)**.

---

## Bagian 2 — Prinsip: 5 Buku Besar

Sesuai prinsip akuntansi dasar & praktik, software akuntansi di-set berdasarkan **5 buku**
(berlaku untuk **perusahaan dagang maupun jasa**). Setiap buku menghasilkan **auto-jurnal**.

### 1. Buku Pembelian
Mencatat pembelian barang dagangan / biaya; **pengakuan hutang**.
Auto-jurnal (tergantung setting item di awal):
```
Dr  Persediaan / Biaya
    Cr  Hutang Dagang / Hutang Biaya
```
Buku Pembelian juga dipakai mencatat **biaya yang masih harus dibayar** (*accrued expense*) —
biaya sudah terjadi tetapi belum dibayar/ditagih. Contoh (biaya sewa kantor terutang):
```
Dr  Biaya Sewa Kantor
    Cr  Hutang Biaya
```

### 2. Buku Penjualan
Mencatat penjualan barang dagang / jasa; **pengakuan Piutang** (+ HPP & pengurangan persediaan untuk barang dagang).
Auto-jurnal:
```
Dr  Piutang
    Cr  Pendapatan Penjualan / Jasa
```
*(untuk barang dagang, ditambah: `Dr HPP | Cr Persediaan`)*

### 3. Buku Pengeluaran Kas / Bank
Mencatat pembayaran hutang atas pembelian / biaya.
Auto-jurnal:
```
Dr  Hutang Dagang / Hutang Biaya
    Cr  Kas / Bank
```

### 4. Buku Penerimaan Kas / Bank
Mencatat penerimaan piutang atas penjualan barang dagang / jasa.
Auto-jurnal:
```
Dr  Kas / Bank
    Cr  Piutang Dagang
```
Jika **penerimaan uang muka penjualan** (mis. perusahaan properti — DP unit sebelum akad):
```
Dr  Kas / Bank
    Cr  Uang Muka Penjualan
```

### 5. Jurnal Voucher
Khusus mencatat transaksi **di luar 4 buku di atas** — umumnya **penyesuaian**: amortisasi
biaya dibayar dimuka, reklasifikasi, dan koreksi.
> Catatan:
> - **Pendapatan tidak boleh di-accrual** — akan kontradiksi dengan laporan penjualan **secara fiskal**.
> - **Accrual biaya** (biaya yang masih harus dibayar) cukup dientri lewat **Buku Pembelian**
>   (auto-jurnal `Dr Biaya | Cr Hutang Biaya`) — tidak perlu jurnal voucher manual.

Bersifat **manual**, tapi bisa dibuat **recurring** untuk transaksi bulanan.
Contoh — amortisasi sewa kantor dibayar dimuka (bulanan; sewa dibayar di muka lalu diakui tiap bulan):
```
Dr  Biaya Sewa Kantor
    Cr  Sewa Kantor Dibayar Dimuka
```
> **Detail field & contoh lengkap JV** (settlement uang muka, dll) ada di
> [Modul General Ledger — Journal Voucher](modul-general-ledger-jv.md).

---

## Filosofi

Dengan alur **input voucher → auto-jurnal → posting**, perusahaan **tidak perlu akuntan senior**
untuk operasional harian; lulusan **SMA / fresh graduate akuntansi** pun bisa mengoperasikan.
Kerumitan debit/kredit ditangani oleh sistem lewat setting master (item, COA, pajak) yang
disiapkan sekali di awal.
