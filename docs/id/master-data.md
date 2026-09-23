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
