# Modul Penjualan (Sales) — Kerangka & Logika

> Kerangka siklus **Order-to-Cash** dan logika akuntansinya. Fokus **alur + logika + auto-jurnal**
> dulu; **detail field entry menyusul**. *(Dikurasi akuntan praktik.)*

---

## 0. Prasyarat Setup

**Item di-setting dengan harga jual** dan **terhubung ke COA Pendapatan Penjualan** (sisi pendapatan)
serta **COA Persediaan** (sisi HPP). **PPN dihitung otomatis oleh sistem** — pilih **Including PPN**
atau **Excluding PPN** saat entry.

---

## 1. Alur 6 Langkah (Order-to-Cash)

```
1. Sales Quotation (SQ)   — penawaran ke pelanggan
2. Sales Order (SO)       — pesanan pelanggan (approval sales)
3. Delivery Order (DO)    — pengiriman barang oleh gudang (tarik data SO)
4. Sales Invoice          — faktur penjualan (tarik data DO)
5. Sales Return           — retur penjualan (jika ada)
6. Sales Receipt          — penerimaan pembayaran (Penerimaan Penjualan)
```

---

## 2. Logika Menjurnal per Langkah

| Langkah | Menjurnal? | Auto-jurnal | Catatan |
|---|---|---|---|
| **1. Sales Quotation** | ❌ Tidak | — | Catatan & **approval** sales dept/manager. Belum ada dampak keuangan. |
| **2. Sales Order** | ❌ Tidak | — | Pesanan pelanggan (approval). Belum menjurnal. |
| **3. Delivery Order** | ⚪ Pencatatan gudang | — (jurnal di Sales Invoice) | Pengiriman barang oleh **gudang** dengan **menarik data SO**. Belum jurnal akuntansi. |
| **4. Sales Invoice** | ✅ Ya (2 jurnal) | **Pendapatan:** `Dr Piutang Usaha` \| `Cr Pendapatan Penjualan` (+ `Cr PPN Keluaran` bila ada faktur pajak). **HPP:** `Dr HPP` \| `Cr Persediaan` | **Menarik data DO** saat entry. Di sini jurnal terjadi — pengakuan pendapatan **dan** HPP sekaligus. |
| **5. Sales Return** | ✅ Ya | **Reversal otomatis oleh sistem** | Barang diterima kembali → sistem membalik jurnal penjualan (pendapatan, PPN, piutang, HPP, persediaan). |
| **6. Sales Receipt** | ✅ Ya | `Dr Kas/Bank` \| `Cr Piutang Usaha (AR)` | Saat entry input **diterima via bank/kas**; auto-jurnal melunasi piutang. |

> **Inti:** SQ & SO = catatan + approval (**tanpa jurnal**). DO = **pengiriman gudang** (tarik SO,
> belum jurnal). **Jurnal terjadi di Sales Invoice** — **dua jurnal** sekaligus: pengakuan
> **pendapatan** (`Dr Piutang | Cr Pendapatan (+PPN Keluaran)`) dan **HPP** (`Dr HPP | Cr Persediaan`).
> Ditutup di **Sales Receipt** (`Dr Kas/Bank | Cr Piutang`).

---

## 3. Prinsip Logika Penting

1. **Setup item → COA:** harga jual terhubung ke **Pendapatan Penjualan**; harga pokok terhubung ke
   **Persediaan** (untuk HPP). Ini dasar auto-jurnal.
2. **PPN otomatis:** sistem menghitung PPN Keluaran; pilih **Including / Excluding PPN** saat entry.
3. **Data mengalir:** SQ → SO → DO → Sales Invoice (menjaga kecocokan pesan ↔ kirim ↔ faktur).
4. **Titik jurnal = Sales Invoice**, mencatat **2 jurnal**: pendapatan + HPP.
5. **Retur = reversal otomatis** oleh sistem.
6. **Alur Piutang (AR):** Sales Invoice menaikkan AR → Sales Receipt menurunkan AR.

---

## 4. Cermin Purchase vs Sales

| | Pembelian (Purchase) | Penjualan (Sales) |
|---|---|---|
| Saat faktur | `Dr Persediaan \| Cr Utang Usaha (+PPN Masukan)` | `Dr Piutang \| Cr Pendapatan (+PPN Keluaran)` **&** `Dr HPP \| Cr Persediaan` |
| Saat kas | `Dr Utang Usaha \| Cr Kas/Bank` | `Dr Kas/Bank \| Cr Piutang Usaha` |

---

## 5. Ringkasan (satu tarikan napas)

`SQ & SO = approval (tanpa jurnal)` → `DO = kirim barang, tarik SO` →
`Sales Invoice = JURNAL: (Dr Piutang | Cr Pendapatan +PPN Keluaran) & (Dr HPP | Cr Persediaan)` →
`Sales Receipt = Dr Kas/Bank | Cr Piutang`. (Retur = reversal otomatis.)

---

## 6. Sales Invoice — Detail Field Data Entry

Layar entry dibuat agar **user cukup memilih data** (lewat **dropdown ▼** dan **kaca pembesar 🔍**
yang menautkan ke master data); sistem yang **menghitung Amount/VAT/Total dan membuat jurnal
otomatis**.

**a) Header — pihak & dokumen:**
- **Customer** ▼ — link ke **master customer**; otomatis menarik Bill To/Ship To, Terms, dan AR default.
- **Select DO / Select SO** 🔍 — link ke voucher **Delivery Order / Sales Order**. **Opsional:** bila
  DO diinput, item tertarik otomatis dari DO; bila tidak, bagian **Finance** input langsung di Sales
  Invoice untuk **pengakuan Piutang**.
- **Cust. is Taxable** ☑ dan **Inclusive Tax** ☑ — menentukan apakah pelanggan kena pajak & apakah
  harga sudah termasuk PPN.
- **Bill To / Ship To** — alamat tagih & kirim (▼).
- **PO No.**, **Invoice No.** (auto), **Invoice Date**, **Ship Date**, **FOB**, **Terms** ▼ (mis.
  C.O.D), **Ship Via** ▼.
- **Template** ▼ (A4 / A4 FULL / Sales Invoice) & **Preview** ▼ (Preview / Printer / VAT Invoice).

**b) Grid item** (tab **# Items** / **Down Payment**):
- **Item** ▼🔍 — link ke **master item**; menarik deskripsi, harga, dan COA (pendapatan/persediaan/HPP).
- **Item Description**, **Qty**, **Item Unit**, **Unit Price**, **Disc %**, **Tax** (T = kena pajak),
  **Amount** (auto = Qty × Unit Price − Disc), **Dept.** ▼ (cost/profit center), **SN** (serial/batch).

**c) Footer — pajak, akun & total:**
- **Inv. Tax No** + nomor faktur pajak + tanggal.
- **Description** — keterangan transaksi.
- **AR Account** ▼ — pilih akun **Piutang**: AR Trade, AR Nontrade, AR Affiliates, AR Employee,
  AR Officers, AR Others, atau Advance Payment.
- **Sub Total** (auto), **Discount** (nilai / %), **VAT** (auto), **Freight**, **Total Invoice** (auto).
- Status: Balance, Paid, Paid Disc, PPh Ps.23, Return.
- Tombol: **Pay**, **Print**, **Save & New**, **Save & Close**, **Cancel**.
- Toolbar: **Get from Memorize**, **Recurring**, **Sales Receipt**, dan **Show Journal** (lihat
  jurnal otomatis yang terbentuk).

**d) Auto-jurnal yang terbentuk** (contoh: *Inclusive Tax*, Total Invoice Rp450.000):

*Jurnal 1 — pengakuan pendapatan (dari header + total):*
```
Dr  Piutang Usaha (AR)              450.000
    Cr  PPN Keluaran (VAT Out)           44.594
    Cr  Pendapatan Penjualan           405.406
```
*Jurnal 2 — pengakuan HPP (dari item × harga pokok):*
```
Dr  HPP (COGS)                     234.000
    Cr  Persediaan (Inventory)         234.000
```
> Karena **Inclusive Tax**, VAT dikeluarkan dari total (450.000 − 44.594 = 405.406 pendapatan bersih).
> Satu Sales Invoice → **dua jurnal balance** sekaligus (pendapatan + HPP), tanpa user menjurnal manual.
> Tombol **Show Journal** menampilkan Transaction Journal ini untuk verifikasi.

---

## 7. Sales Receipt (Penerimaan Pembayaran) — Detail Field Data Entry

**Sales Receipt = mencatat uang masuk saat pelanggan membayar faktur.** Dibuka dari layar **Sales
Invoice → klik tombol "Sales Receipt"**, sehingga banyak field **terisi otomatis** dari faktur.
Layarnya disebut **Cust. Receipt**. Banyak field terisi sendiri; user cukup melengkapi sisanya.

**a) Bagian atas — dari siapa & kapan:**
- **Received From** — **otomatis terisi** nama pelanggan (data ditarik dari Sales Invoice).
- **Form No.** — nomor bukti terima (otomatis). **Payment Date** — tanggal uang diterima.

**b) Bagian akun penerima — ke mana uang masuk:**
- **Bank** — akun kas/bank yang **menerima** uang. Bisa rekening bank biasa, atau akun khusus
  **Cash in Transit (CIT)** — lihat catatan di bawah.
- **Cheque No. / Cheque Date** (bila bayar pakai cek), **Currency / Rate** (bila valas).
- **Cheque Amount** — jumlah yang diterima; **Distribute Amount** — jumlah yang dialokasikan ke
  faktur.

**c) Grid faktur yang dibayar:**
- **Invoice No., Date, Amount, Owing (sisa utang), Payment Amount (otomatis), Total Disc., Paid
  (centang lunas), Discount Date.** Kolom **Paid** dan **Payment Amount** ikut terisi otomatis
  mengikuti faktur yang dipilih.
- **Memo** — keterangan.
- Tombol: **Print, Save & New, Save & Close, Cancel.**

**d) Auto-jurnal yang terbentuk** (contoh pelunasan Rp15.300.000):
```
Dr  Kas/Bank penerima (mis. Cash in Transit)   15.300.000
    Cr  Piutang Usaha (AR)                          15.300.000
```
> Satu jurnal sederhana: **kas/bank bertambah, piutang berkurang.** Inilah penutup siklus penjualan
> — faktur yang tadinya "belum dibayar" kini lunas.

---

### Catatan khusus: akun **Cash in Transit (CIT)** untuk penjualan retail

Untuk **penjualan retail** yang jumlahnya banyak, penerimaan bisa diarahkan ke akun **penampungan
sementara** bernama **Cash in Transit (CIT)** — bukan langsung ke bank. Tujuannya **menggunggung**
(menggabungkan) penerimaan retail agar **tidak perlu entry satu per satu**, karena bagian marketing
sudah menerbitkan **OR (Official Receipt)** sendiri untuk tiap pelanggan retail. Nanti saldo CIT ini
"dibersihkan" ke bank saat setoran nyata masuk.

> **Catatan untuk Tere:** akan ada **file update tersendiri** soal mekanisme CIT / gunggung retail
> ini → dimasukkan ke halaman **tips akunting/jurnal**. *(Ditandai sebagai to-do.)*

---

*Alur & logika di atas melengkapi kerangka modul Sales.*
