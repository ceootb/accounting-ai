# Modul General Ledger — Journal Voucher (JV)

> **Jurnal Voucher (JV)** adalah **buku besar ke-5** dari [konsep 5 Buku Besar](cara-kerja-sistem-akuntansi.md#bagian-2--prinsip-5-buku-besar).
> Bedanya dengan 4 buku lain (Pembelian, Penjualan, Pengeluaran & Penerimaan Kas): JV adalah
> **jurnal manual** untuk hal-hal yang **tidak** tercakup transaksi otomatis. Bahasa awam untuk user;
> detail teknis disimpan untuk tahap build software.

---

## Untuk apa JV dipakai?

JV dipakai untuk **penyesuaian (adjustment) dan koreksi** — jurnal yang tidak muncul dari modul
Sales/Purchase/Kas. Contoh yang sering:
- **Amortisasi biaya dibayar dimuka** (sewa, asuransi, dll).
- **Reklasifikasi** akun (salah pos → dipindahkan).
- **Settlement uang muka** (cash advance) staf.
- **Koreksi** kesalahan pencatatan.

> **Catatan:** **penyusutan aset dihitung otomatis oleh modul Fixed Asset**, jadi *tidak* perlu JV manual.

> Karena sifatnya menyesuaikan angka secara manual, **JV umumnya dipegang supervisor/manager** —
> bukan staf input biasa. Ini bagian dari pengendalian internal (lihat hak akses di modul Setup).

---

## Field yang diisi

**a) Bagian atas:**
- **Voucher No.** — nomor bukti (otomatis).
- **Date** — tanggal jurnal.
- **Description** — keterangan (mis. "amortisasi sewa kantor September").
- **Multi Currency** — dicentang bila melibatkan mata uang asing.

**b) Grid baris jurnal:**
- **Account No. / Account Name** — pilih akun dari daftar **COA**. Bisa lewat **opsi search**
  atau cukup **mengetik nama/nomor akun** (mis. ketik "pet" → muncul *Cash - Petty Cash*).
- **Debit** / **Credit** — isi nilai di sisi yang tepat.
- **Memo** — catatan per baris.
- **Department** — pusat biaya (opsional).
- **Subsidiary Ledger** — bila akun punya sub-buku besar (mis. Piutang/Utang per orang/vendor),
  pilih sub-akun terkait agar rincian per pihak ikut ter-update.

**c) Bawah:** total **Debits** dan **Credits** ditampilkan. **Voucher hanya bisa disimpan bila
Debit = Kredit (balance).** Bisa dibuat **Recurring** untuk penyesuaian bulanan.

---

## Contoh 1 — Amortisasi biaya sewa dibayar dimuka (yang diminta)

Misal perusahaan membayar **sewa kantor 1 tahun di muka Rp12.000.000** di bulan Januari. Saat
membayar, nilainya masuk ke akun aset **"Sewa Dibayar Dimuka"** (prepaid), belum jadi biaya.

Tiap akhir bulan, **1/12 = Rp1.000.000** diakui sebagai biaya lewat JV:
```
Dr  Biaya Sewa Kantor              1.000.000
    Cr  Sewa Dibayar Dimuka            1.000.000
```
> Aset prepaid berkurang tiap bulan, biaya diakui sesuai bulan berjalan (prinsip **matching**).
> Setelah 12 bulan, saldo prepaid habis. JV ini cocok dibuat **recurring** karena berulang tiap bulan.

---

## Contoh 2 — Settlement uang muka (cash advance) staf

Misal staf purchasing diberi **uang muka Rp3.200.000** untuk keperluan acara (saat diberikan,
tercatat sebagai **Uang Muka / Piutang Karyawan**). Setelah acara, dipertanggungjawabkan: realisasi
biaya **Rp2.900.000**, sisa kas dikembalikan **Rp300.000**. JV-nya:
```
Dr  Biaya Kegiatan                2.900.000
Dr  Kas/Bank (sisa dikembalikan)    300.000
    Cr  Uang Muka Karyawan             3.200.000
```
> Uang muka "dibersihkan" (Cr) sebesar yang tadi diberikan; sisi debit merinci ke mana uang itu
> terpakai + sisa yang kembali. Total debit = kredit. Bila memakai akun ber–sub-buku besar (mis. per
> nama staf), kolom **Subsidiary Ledger** dipilih agar rincian per orang ikut ter-update.

---

## Intinya

> **JV = jurnal manual untuk penyesuaian & koreksi** yang tidak dihasilkan modul otomatis. Aturannya
> tetap sama: **harus balance (Debit = Kredit)**. Karena berdampak langsung ke Buku Besar, aksesnya
> dibatasi ke supervisor/manager. Ini melengkapi 4 buku otomatis lainnya menjadi **5 Buku Besar**
> yang utuh.
