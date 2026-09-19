# Modul Aset Tetap (Fixed Asset)

> Modul untuk mencatat **aset tetap** (gedung, kendaraan, mesin, komputer, dll), menghitung
> **penyusutan otomatis tiap bulan**, dan membuat **jurnalnya sendiri**. Bahasa awam untuk user;
> detail teknis disimpan untuk tahap build software.

---

## Gambaran: 3 sub-modul (dari umum ke rinci)

```
1. Fiscal Fixed Asset Type  → "kelompok pajak" (patokan umur & tarif penyusutan fiskal)
2. Fixed Asset Type         → kategori aset perusahaan, dihubungkan ke kelompok pajak di atas
3. Fixed Asset List         → daftar aset yang benar-benar dibeli (data entry per aset)
```
Dua yang pertama adalah **setup awal** (disiapkan sekali). Yang ketiga diisi tiap kali beli aset baru.

---

## 1. Fiscal Fixed Asset Type — kelompok pajak

Ini daftar **kelompok penyusutan menurut pajak**. Tiap kelompok punya: **metode penyusutan**,
**estimasi umur (tahun)**, dan **tarif % (dihitung otomatis dari umur)**. Contoh: umur 20 tahun →
tarif garis lurus **5%** (100% ÷ 20).

> ⚠️ **Penting — samakan dengan aturan pajak terbaru.** Kelompok fiskal Indonesia (UU PPh Pasal 11
> & PMK 72/2023) yang **benar**:
>
> | Kelompok | Masa manfaat | Garis lurus | Saldo menurun |
> |---|---|---|---|
> | **Bukan bangunan — Kelompok 1** | 4 tahun | 25% | 50% |
> | **Kelompok 2** | 8 tahun | 12,5% | 25% |
> | **Kelompok 3** | 16 tahun | 6,25% | 12,5% |
> | **Kelompok 4** | **20 tahun** | **5%** | 10% |
> | **Bangunan Permanen** | 20 tahun | 5% | — (hanya garis lurus) |
> | **Bangunan Tidak Permanen** | 10 tahun | 10% | — |
>
> Jadi **Kelompok 4 = 20 tahun (5%)**, *bukan* 32 tahun. Pastikan tabel di sistem mengikuti angka ini.

Pilihan **metode penyusutan** yang tersedia: **Non Depreciable** (tidak disusutkan, mis. Tanah),
**Straight Line (garis lurus)**, dan **Declining (saldo menurun)**.

---

## 2. Fixed Asset Type — kategori aset perusahaan

Menghubungkan **kategori aset perusahaan** (mis. Building, Vehicle, Computer, Machinery, Land) ke
**kelompok pajak** di atas. Setelah kelompok pajak dipilih, field umur/metode/tarif **terisi otomatis
(abu-abu)** mengikuti kelompoknya. Contoh: *Computer* → Kelompok 1 → garis lurus, 4 tahun, 25%.

---

## 3. Fixed Asset List — data entry aset yang dibeli

Setiap aset yang dibeli didaftarkan di sini. Semua entry membentuk **daftar aset** lengkap.

**Header:** Asset Code, **Asset Type** (dropdown, dari daftar Fixed Asset Type), Acquisition Date,
Usage Date, Asset Description, jumlah, **Department** (dropdown).

**Tab General** (yang utama):
- **Estimated Life** — umur (tahun & bulan), diisi manual.
- **Depreciation Method** — pilih dari dropdown (garis lurus, saldo menurun, sum-of-year-digit, atau
  non-depreciable). **Rate** terisi otomatis dari umur + metode.
- **Asset Account** — akun aset di COA (mis. Bangunan).
- **Accumulated Depreciation Account** — akun akumulasi penyusutan di COA.
- **Depreciation Expense Account** — akun beban penyusutan di COA.
- **Fiscal Fixed Asset** — dicentang bila aset ini ikut aturan fiskal.

**Tab Expenditures:** merekam **biaya perolehan** aset, yang masuk lewat **akun perantara "Fixed
Asset Transaction"** (lihat auto-jurnal di bawah). *(Tab Notes diabaikan.)*

> Tombol **Dispose** (pelepasan aset) & **Revaluation** (revaluasi) ada di sini, **dibahas terpisah**.

---

## Auto-jurnal — 3 tahap

**Tahap 1 — Beli aset (lewat Purchase Invoice):** nilai masuk ke **akun perantara** dulu.
```
Dr  Fixed Asset Transaction (perantara)
    Cr  Kas/Bank atau Utang Usaha
```

**Tahap 2 — Daftarkan aset di Fixed Asset List:** nilai dipindah dari perantara ke akun aset.
```
Dr  Aset Tetap (mis. Bangunan)
    Cr  Fixed Asset Transaction (perantara)
```
> Akun **Fixed Asset Transaction** = "jembatan" antara pembelian dan pendaftaran aset. Setelah kedua
> tahap selesai, saldo akun perantara ini kembali **nol** (masuk lalu keluar).

**Tahap 3 — Penyusutan bulanan (otomatis, lewat [Period End](proses-tutup-periode-period-end.md)):**
```
Dr  Beban Penyusutan (Depreciation Expense)
    Cr  Akumulasi Penyusutan (Accumulated Depreciation)
```
> Cukup **klik tombol "Period End"** saat tutup buku bulanan — sistem **menghitung & menjurnal
> penyusutan semua aset sekaligus** (satu voucher, dirinci per aset & per departemen). User tidak
> menghitung manual.

**Contoh angka:** bangunan Rp1.200.000.000, umur 20 tahun (garis lurus 5%/tahun) → penyusutan
Rp60.000.000/tahun = **Rp5.000.000/bulan**:
```
Dr  Beban Penyusutan - Bangunan     5.000.000
    Cr  Akumulasi Penyusutan - Bangunan   5.000.000
```

---

## Intinya

> **Setup sekali** (kelompok pajak → kategori aset), lalu **daftarkan tiap aset** dengan akun-akun
> COA-nya. Sistem mengurus sisanya: pembelian lewat akun perantara, lalu **penyusutan tiap bulan
> otomatis hanya dengan klik "Period End"**. User tak perlu menghitung penyusutan manual, dan angka
> selalu konsisten ke Buku Besar & Laporan Keuangan.
