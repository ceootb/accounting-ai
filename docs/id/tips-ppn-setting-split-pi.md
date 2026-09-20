# Tips: Setting PPN di Pembelian & Split PI Saat Beda Periode

> Dua hal praktik seputar **PPN** pada pembelian: (1) dari mana setting PPN berasal, dan (2) trik
> **memecah Purchase Invoice (PI) menjadi 2** ketika **periode PPN berbeda** dengan periode bebannya.

---

## 1. Dari mana setting PPN berasal?

PPN **tidak** diketik ulang tiap faktur — sumbernya dari **master vendor**. Di profil vendor
(tab *Terms, etc.*) ada bagian **Taxes**:
- **Tax 1: VAT** (PPN) dan **Tax 2: W/H TAX** (PPh potong),
- opsi **Default Invoice is Tax Included**,
- **Vendor's Tax No.**, **PKP No.**, dan **Tax Type**.

Karena vendor sudah diset **kena PPN**, maka saat membuat Purchase Invoice, centang **Vendor is
Taxable** aktif dan kolom **Tax** pada baris item bertanda **T** → sistem menghitung **PPN Masukan**
otomatis. Termin pembayaran (mis. Net 14, Net 30, C.O.D) juga diambil dari master vendor.

---

## 2. Trik: Split 2 PI saat periode PPN ≠ periode beban

**Masalah:** kadang **beban/barang** diakui di satu bulan, tapi **faktur pajak (PPN)** dari vendor
baru terbit di bulan berikutnya. Contoh: **barang diterima & beban milik Juli**, tapi **faktur pajak
terbit Agustus**. Kalau dijadikan satu PI, salah satu pasti "meleset" periodenya — entah bebannya
mundur, atau PPN-nya maju.

**Solusi — pecah jadi 2 Purchase Invoice:**

**PI-A — hanya DPP / beban** (di periode beban, mis. Juli). Diinput lewat **item/akun beban**, tanpa
PPN.
```
PI-A (Juli) — DPP Rp8.887.500
Dr  Beban / Persediaan            8.887.500
    Cr  Utang Usaha                   8.887.500
```

**PI-B — hanya PPN** (di periode faktur pajak terbit, mis. Agustus). Diinput lewat **tab Expense**
langsung ke akun **PPN Masukan (VAT In)**.
```
PI-B (Agustus) — PPN Rp977.625
Dr  PPN Masukan (VAT In)             977.625
    Cr  Utang Usaha                     977.625
```

**Saat bayar (Purchase Payment):** buka pembayaran ke vendor itu, lalu **centang kedua voucher PI**
(PI-A + PI-B) untuk dibayar bersamaan.
```
Dr  Utang Usaha (PI-A)             8.887.500
Dr  Utang Usaha (PI-B)              977.625
    Cr  Kas/Bank                       9.865.125
```

**Kenapa dipisah?**
- **Beban** tetap diakui **sesuai periode terjadinya** (prinsip matching) → laba bulan itu benar.
- **PPN Masukan** dikreditkan **sesuai masa pajak faktur** (aturan PPN: pengkreditan PM mengikuti
  tanggal faktur pajak) → cocok dengan SPT Masa PPN, tidak beda bulan.

> **Intinya:** kalau tanggal faktur pajak beda bulan dengan bebannya, **pisahkan DPP dan PPN ke 2 PI**
> agar buku (beban) dan pajak (PPN) sama-sama jatuh di periode yang benar. Saat pelunasan, kedua PI
> dibayar sekaligus.

---

*Setting PPN di **Sales Invoice** memakai cara serupa (dari master customer) — dibahas terpisah.*
