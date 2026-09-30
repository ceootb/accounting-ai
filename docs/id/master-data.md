# Master Data (Departemen, Pelanggan, Pemasok, Item)

**Master data** adalah data acuan yang **disiapkan sekali** lalu **dipakai berulang** di banyak
transaksi. Menyiapkannya rapi di depan membuat entry transaksi cepat dan laporan otomatis rapi di
belakang. Master utama: **Chart of Accounts (COA)**, **Departemen**, **Pelanggan (Customer)**,
**Pemasok (Vendor)**, **Item**, dan **Aset Tetap**. COA dan Aset Tetap punya halamannya sendiri;
halaman ini membahas empat sisanya.

Semua master punya **pola yang sama**: setiap jenis ditampilkan sebagai **daftar (data grid)** yang
bisa **disaring per kolom**, ditelusuri ke detailnya, dan dicetak. Data bisa diisi **satu per satu**
atau **diimpor dari file** bila jumlahnya banyak. Record yang tak dipakai lagi umumnya **dinonaktifkan
(suspend)**, bukan dihapus — supaya **histori transaksi lama tetap utuh**.

---

## Departemen

**Departemen** adalah **unit / pusat biaya** untuk keperluan *costing* dan pelaporan. Gunanya: agar
**biaya dan laba bisa dilihat per unit** (mis. per cabang, per divisi, per proyek), bukan hanya angka
gabungan satu perusahaan. Karena itu banyak layar transaksi menyediakan kolom **Department** — supaya
setiap biaya/pendapatan bisa ditandai miliknya unit mana.

Sebagai master, departemen sederhana isinya:
- **Nomor & Nama Departemen** — identitas unit.
- **Sub-Departemen** — sebuah departemen bisa dijadikan **anak** dari departemen lain, membentuk
  **hierarki** (mis. Divisi → Sub-divisi). Berguna untuk laporan berjenjang.
- **Status non-aktif (suspend)** — departemen yang sudah tidak dipakai bisa **dinonaktifkan** agar
  tak muncul saat entry baru, tetapi **catatan lamanya tetap ada**.

Seluruh departemen tampil di **daftar (list)** yang bisa disaring — misalnya menyaring berdasarkan
**status aktif/non-aktif** — lalu dibuka ke detailnya atau dicetak.

> **Intinya:** departemen bukan bagian akuntansi debit-kredit, tapi **penanda unit** yang membuat
> laporan bisa dipecah per bagian. Siapkan sekali, lalu tinggal dipilih di transaksi.

---

## Pelanggan (Customer)

**Customer** adalah master pihak yang kita jual kepadanya. Data ini **terhubung ke Sales Invoice →
Piutang Usaha (AR) → dan Sub Ledger AR** (buku pembantu per pelanggan). Karena itu, data pelanggan yang
benar membuat **piutang dan umur piutang (aging) rapi** dengan sendirinya.

Informasi yang disiapkan dikelompokkan dalam beberapa bagian; yang paling penting:
- **Alamat** — **wajib diisi** (untuk penagihan / pengiriman).
- **Termin pembayaran (Term)** — mis. 30 hari. Ini menjadi **dasar perhitungan umur piutang (aging
  AR)**, jadi sebaiknya selalu diisi.
- **Mata uang (Currency)** — bila pelanggan bertransaksi dalam **valuta asing**.
- **Pajak** — ada dua setelan: **Tax 1 = PPN (VAT)** dan **Tax 2 = pemotongan PPh (withholding)** —
  supaya saat membuat faktur, pajaknya **otomatis benar**. Ada juga opsi **harga sudah termasuk pajak
  (tax included)**. Contoh: pelanggan **luar negeri** umumnya **tidak dikenai PPN**, jadi setelan
  pajaknya dikosongkan.
- **Tipe Pelanggan (Customer Type)** — pengelompokan untuk analisa/laporan.

Bagian lain (Kontak, Catatan, Custom Field) sifatnya **opsional** dan sering tidak dipakai.

> **Intinya:** isi yang benar-benar berdampak ke akuntansi adalah **Termin** (untuk aging), **Pajak**
> (PPN & PPh), dan **Mata uang**. Sekali disiapkan, faktur & piutang pelanggan itu jadi konsisten.

---

## Pemasok (Vendor)

**Vendor** adalah master pihak yang kita **beli** darinya — **cerminan** dari Customer. Data ini
terhubung ke **Purchase Invoice → Utang Usaha (AP) → dan Sub Ledger AP** (buku pembantu per pemasok).
Isinya sama polanya dengan Customer: **alamat** (wajib), **termin pembayaran**, **pajak** (PPN &
pemotongan PPh), dan **mata uang**. Bagian lain (Kontak, Catatan, Custom Field) opsional.

> **Konsisten dengan Customer:** yang berdampak ke akuntansi tetap **Termin**, **Pajak**, dan **Mata
> uang**. Setelah benar, faktur pembelian & utang pemasok otomatis konsisten.

## Termin & Pajak = master yang bisa dipakai ulang

**Termin (payment terms)** dan **Pajak (Tax)** bukan data yang diketik ulang tiap kali membuat Customer
atau Vendor — keduanya **master yang dibuat sekali lalu dipakai ulang**:
- **Termin** — mis. *COD, Net 14, Net 30*. Dibuat sekali (opsi *New Term*), lalu tinggal dipilih untuk
  pihak berikutnya. Menghindari termin ganda & menjaga konsistensi (dasar hitung aging).
- **Pajak** — mis. *PPN (VAT)* dan *pemotongan PPh (W/H Tax)*. Juga master reusable (opsi *New Tax*).
  Satu pihak bisa punya lebih dari satu setelan pajak yang **berdiri sendiri** (mis. PPN **dan** PPh),
  dan boleh berbeda antar pihak.

> **Intinya:** buat **master Termin/Pajak sekali**, lalu **pilih** di tiap Customer/Vendor — jangan
> bikin ulang. Ini menjaga data rapi dan konsisten.

---

## Item (Barang, Jasa, atau Biaya)

**Tidak semua Item adalah barang persediaan.** Item adalah **representasi** apa pun yang dipilih di
transaksi, dan **perlakuan akuntansinya ditentukan oleh fungsi Item + akun default (COA mapping)** yang
diatur **saat item dibuat** — bukan sekadar karena item muncul di transaksi. Ada **tiga jenis**:

**1. Item Persediaan (Inventory)** — barang yang benar-benar menjadi **stok** (mis. kopi, gula, barang
dagangan). Akun default = **Persediaan**.
```
Beli:  Dr Persediaan | Cr Utang Usaha / Kas
```
Saat dipakai/terjual, persediaan mengikuti **costing/HPP** sesuai mekanisme sistem.

**2. Item Pendapatan (Revenue)** — untuk transaksi yang **menghasilkan pendapatan**; **tidak harus**
inventory:
- **Produk olahan / hasil produksi** (mis. *minuman kopi hasil olahan*) → default **Revenue – Penjualan
  Minuman**. Bahannya (kopi/gula/susu) dibeli dulu sebagai **inventory**, lalu yang terpakai dialokasikan
  jadi **Direct Cost / HPP** lewat *job costing* / proses costing. Detail alur biayanya:
  [Produk Olahan: Cost Flow & Job Costing](produk-olahan-job-costing.md).
- **Jasa** (konsultasi, desain, maintenance) → default **Revenue – Pendapatan Jasa**. Item jasa **tidak
  pernah** punya transaksi beli (perusahaan tak membeli jasa untuk dijual lagi).
```
Faktur jasa:  Dr Piutang Usaha | Cr Pendapatan Jasa
```

**3. Item Biaya (Expense)** — ditautkan langsung ke **akun beban** tertentu (mis. *Parkir* & *Toll* →
**Parking Expense**). Memudahkan user yang tak menguasai COA.
```
Dr Beban (mis. Parking Expense) | Cr Kas / Bank
```

### Setting item sekali di awal = kontrol preventif

Mapping akun pada Item adalah **kontrol pencegahan**: **admin yang paham akuntansi** menetapkannya
**saat master item dibuat**. Setelah benar, **user operasional cukup memilih Item** → sistem mengambil
**akun default** → **jurnal otomatis**. User tak perlu memilih COA manual tiap entry.

> **Konsep kontrol:** *kesalahan dicegah di depan, bukan dikoreksi berulang di belakang.* Dengan master
> item yang benar sejak awal, risiko salah akun/jurnal saat transaksi ditekan mendekati **nol** —
> pengetahuan akuntansi user operasional jadi ringan, kontrol tetap di master setup.

> **Perubahan mapping:** untuk item yang **sudah dipakai** bertransaksi, mengubah akun default harus
> dikontrol. Jika perubahannya **mengubah sifat akuntansi** item, **buat item baru** dengan mapping
> baru — supaya **histori transaksi lama tetap konsisten**.

> **Item saat dipakai di transaksi → jurnal otomatis** (per jenis item): lihat [Item di Transaksi: Mapping Akun & Auto-Jurnal](item-transaksi-auto-jurnal.md).
