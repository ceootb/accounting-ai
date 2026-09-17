# Modul Setup / Persiapan Awal (Tahap 1)

> Konfigurasi awal di menu **Setup** sebelum perusahaan mulai bertransaksi. Ini melengkapi
> **Tahap 1 (Persiapan)** pada [cara-kerja-sistem-akuntansi.md](cara-kerja-sistem-akuntansi.md).
> *(Kerangka; detail field per menu menyusul.)*

---

## Isi Menu Setup

### 1. Company Info (Info Perusahaan)
Terdiri dari beberapa **tab**: **General · Accounting Period · Tax · Branch ID**.

**a) Tab General** — identitas dasar:
- Company Name, Address, Zip Code, Phone No., Fax No., Country.
- **Default Currency** (mis. IDR).

**b) Tab Accounting Period** — **kontrol periode (penting):**
- **Start Date** — tanggal perusahaan mulai beroperasi/pembukuan.
- **Fiscal Year** — tahun buku.
- **Default Period** — **periode berjalan** (current period).
- **Warn if** — *N* bulan **sebelum / sesudah** Default Period → memunculkan **peringatan**.
- **Error if** — *N* bulan **sebelum / sesudah** Default Period → **menolak/mengunci** entry (error).
- **Locking Period:** mencegah user **sembarangan entry** — mis. saat FS sudah **closing**, atau input
  transaksi ke **periode masa depan** tanpa dokumen/alasan jelas. Data masa depan umumnya hanya untuk
  transaksi **recurring**.

**c) Tab Tax** — data perpajakan:
- Form Serial Number, **Tax Registration Number (NPWP)**, **Taxable Company's No.** (No. PKP),
  Taxable Company's Date, Branch Code, Type, **KLU** (Klasifikasi Lapangan Usaha).

### 2. Preferences (Preferensi)
Pengaturan global sistem:
- **Akun default** (mis. kas/bank default, akun pembulatan, laba ditahan).
- Format nomor dokumen, format angka & tanggal.
- **Pengaturan pajak** (PPN default) & fitur on/off.

### 3. User Profile & Hak Akses (Access Rights) — **kontrol internal utama**
- Buat **user (login)** untuk tiap staf.
- **Hak akses per modul** (Sales, Purchase, GL, dll): centang **Create / Edit / Delete**.
- **Hak khusus**, mis. *Print Sales Invoice*, *Change Selling Price*.
- **Prinsip pengendalian:** terapkan **segregation of duties** — pisahkan yang **input**, yang
  **approve**, dan **pemegang kas**. Batasi hak **Delete** & **Change Selling Price** hanya ke role
  tertentu (rawan penyalahgunaan).

### 4. Change Password
Ganti password berkala — keamanan akses akun.

### 5. Quick Setup
**Wizard setup awal terpandu** (COA, saldo, dsb) untuk perusahaan baru.

### 6. Form Templates
**Template cetak dokumen** (Faktur, PO, Kwitansi) — logo, layout, kolom.

---

## Kaitan dengan Tahapan Persiapan

`Setup Menu (Tahap 1)` → lalu **Tahap 2 Master Data** (COA, customer, vendor, item, aset) →
**Tahap 3 Saldo Awal** (bila migrasi) → **Tahap 4 Setup Pajak** (PPN 11%, PPh sesuai jenis WP).

---

## Poin Pengendalian Internal (penting)

- **Hak akses = kontrol utama.** Batasi Create/Edit/Delete sesuai peran.
- **Delete** & **ubah harga jual** paling rawan → batasi ketat + butuh approval.
- **Segregation of duties:** fungsi **input ≠ approve ≠ pemegang kas** untuk mencegah fraud.
