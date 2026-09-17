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
Pengaturan **global sistem** + **akun default** yang dipakai otomatis saat posting jurnal.
Terbagi menjadi beberapa sub-menu. **Inti konsepnya:** sebelum transaksi bisa jalan, tiap jenis
transaksi harus sudah dipetakan ke **akun default** di COA — inilah yang membuat jurnal terbentuk
otomatis. *(Nomor akun di bawah hanya contoh/ilustrasi mapping ke COA.)*

**a) Company** — perilaku aplikasi: *Backup on close*, *Confirm before exit*, *Open last company*,
*Show purchase & sales price in item history*.
- **Retained Earning Account** (contoh `3200001` — Laba Ditahan): akun tujuan penutupan laba/rugi
  tiap akhir periode. **Wajib** diisi.

**b) Feature** — mengaktifkan struktur data & metode:
- **Inventory Costing Method**: **FIFO** atau Average — menentukan cara hitung HPP persediaan.
- Toggle: *Multi Warehouse*, *Quantity can < 0*, **Multi Unit**, *Use Salesman*, *Can Edit Invoice
  Number*, *Control Qty Measurement*.
- **Cost & Profit Center**: **Multi Department** / **Multi Project** — supaya biaya & laba bisa
  dilaporkan per departemen/proyek.
- **Audit Trail**: **Transaction Log** (jejak siapa input/ubah — kontrol internal) & Recalculating
  Cost Log.

**c) Currency Default Account** — akun default **per mata uang** (mis. IDR):
- *Account Payable* (utang usaha), *Account Receivable* (piutang usaha), *Advance Purchase*
  (uang muka beli), *Advance Sales* (uang muka jual), *Sales Discount* (diskon penjualan),
  *Realized Gain/Loss* & *Unrealized Gain/Loss* (selisih kurs).

**d) Item Default Account** — akun default untuk transaksi **barang/persediaan**:
- *Inventory* (persediaan), *Sales* (pendapatan penjualan), *Sales Return*, *Item Discount*,
  *Goods In Transit* (barang dalam perjalanan), **COGS** (HPP), *Purchase Return*, *Expense*,
  *Unbilled Goods* (barang diterima belum ditagih).

**e) Purchases** — perilaku modul pembelian:
- *Remember Vendor*, peringatan bila beli item Serial Number yang sudah pernah dibeli.
- **Purchase Return**: pilih *All Purchase Invoices* / *Outstanding Invoices*.
- **Receive Item → Default Receive Cost**: *Reupdate by bill* / *Do not reupdate* / *Set to
  reupdate by bill bila tanggal bill pertama satu periode dengan tanggal terima* — menentukan
  bagaimana biaya penerimaan disesuaikan saat tagihan datang.
- **Default Difference Unbilled Account**: akun penampung selisih barang diterima vs ditagih.

**f) Cost & Profit Center** — akun default untuk **proyek & departemen**:
- Peringatan bila **Department** belum diisi.
- **Labour Cost** (Expense Account) dan akun proyek: *Project In Process*, *Advanced Revenue*,
  *Revenue*, *Cost of Project Sold*.

**g) Job Costing** — opsi *Save different cost to account* + akun penampungnya.

**h) Taxation** — pengaturan pajak:
- *Code in Invoice Tax No*, *Number for each invoice*, pembulatan **Rounded (Upper)**.
- **Income Tax Account** (contoh `7300000` — PPh Badan).

**i) Reminder** — pengingat saat aplikasi start: *Item to Reorder*, *Expired Serial Number*,
**Receivable due** & **Payable due** (mis. 7 hari sebelum jatuh tempo), diskon jatuh tempo,
serta transaksi **Recurring** (Sales/Purchase Invoice, Payment, Deposit).

**j) Templates Setting** — jumlah copy cetak (mis. **VAT Invoice Copies**).

**k) Miscellaneous** — *Auto pop-up search*, **Invoice Aging** (Aging Range mis. 30 hari; dihitung
dari **Due Date** atau **Invoice Date**), **Language** (English/Indonesia), **Date Format**
(mis. `dd mmm yy`) & format angka.

**l) Font Setting & Skin Option** — ukuran/jenis font & tampilan (kosmetik).

### 3. User Profile & Hak Akses (Access Rights) — **kontrol internal utama**

Layar **Edit User** mengatur identitas login + hak akses per user.

**a) Header (identitas user):**
- **Login Name**, **Full Name**, **Password** + **Confirmation**.
- **Level** (dropdown): **Admin · Supervisor · User** — preset tingkat akses. Admin biasanya semua
  hak tercentang; User default kosong (harus diberi hak sesuai kebutuhan).
- Tombol: **New**, **Save**, **Delete**, **Close**, dan **Get Privilege**.

**b) Get Privilege** — saat membuat user baru, tombol ini otomatis aktif. Gunanya **menyalin hak
akses dari user yang sudah ada** ke user baru, biar tidak perlu centang ulang satu per satu.

**c) Hak akses per aktivitas — 6 kolom izin:**
Tiap baris aktivitas bisa dicentang di kolom: **Create · Edit · Delete · Report · View · List**.
Hak dikelompokkan dalam beberapa **tab modul**:
- **Sales:** Sales Quotation, Sales Order, Delivery Order, Invoicing, Customer Receipt, Sales Return,
  RMA. Hak khusus: *Print Sales Invoice*, **Change Selling Price**, *Commission*, *AR Reminder*,
  *Change Customer Info in Invoice*, *Allow over limit*, *Allow over qty in Invoice*, *Reprint
  Delivery & Invoice*.
- **Purchase:** Purchase Requisition, Purchase Order, Receive Item, Purchasing, Vendor Payment,
  Purchase Return + *AP Reminder*.
- **Item & Inventory:** Item, Warehouse, Item Transfer, Grouping, Job Costing, Inventory Adjustment,
  Selling Price Adjustment + *Change Item Account*, *Create/Enter Serial/Batch Number*.
- **Project:** Labour Cost (+ Adjustment), Material Budget & Price Adjustment, Work Price Analysis,
  Project, Material In Used, Project Survey, Project Ending + *Show RAB*, *Project Control*,
  *Project Expense Payment*.
- **General Ledger & Others:** Chart of Account, Journal Voucher, Budgeting, Customer Data, Vendor
  Data, Financial Report, Tax Report, Department + *Export Data* / *Import Data*.
- **Bank & Fixed Asset:** Other Payment, Other Deposit, Fixed Asset + *Bank Reconciliation*,
  *Revaluate/Dispose Fixed Asset*, *View & print bank book*.
- **Memorized Reports · Designed Reports · Memorized Transaction** (tab tersendiri).

**d) Prinsip pengendalian:** terapkan **segregation of duties** — pisahkan yang **input**, yang
**approve**, dan **pemegang kas**. Batasi hak **Delete** & **Change Selling Price** hanya ke role
tertentu (paling rawan penyalahgunaan). Hindari memberi semua user level **Admin**.

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
