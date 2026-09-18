# Modul Pembelian (Purchase) — Kerangka & Logika

> Kerangka siklus **Procure-to-Pay (P2P)** dan logika akuntansinya. Fokus di **alur + logika +
> auto-jurnal per langkah** dulu; **detail field** menyusul.
> *(Dikurasi akuntan praktik.)*

---

## 0. Prasyarat Setup

**Item barang di-setting di awal**, dan **setiap item terhubung ke COA** (mis. akun Persediaan /
Inventory). Mapping item → COA inilah yang membuat **auto-jurnal** tahu akun mana yang dipakai saat
transaksi berjalan.

---

## 1. Alur 6 Langkah (Procure-to-Pay)

```
1. Purchase Requisition (PR)   — permintaan pembelian internal
2. Purchase Order (PO)         — pesanan resmi ke vendor
3. Receive Items (Penerimaan)  — barang diterima gudang (tarik data PO)
4. Purchase Invoice (Faktur)   — faktur/tagihan vendor (tarik data Received Item)
5. Purchase Return (Retur)     — pengembalian barang (jika ada)
6. Purchase Payment (Bayar)    — pembayaran ke vendor
```

---

## 2. Logika Menjurnal per Langkah

| Langkah | Menjurnal? | Auto-jurnal | Catatan |
|---|---|---|---|
| **1. Purchase Requisition** | ❌ Tidak | — | Hanya catatan & **approval** user/manager. Belum ada dampak keuangan. |
| **2. Purchase Order** | ❌ Tidak | — | Pesanan resmi ke vendor (komitmen). Belum menjurnal. |
| **3. Receive Items** | ⚪ Pencatatan gudang | — (jurnal di Purchase Invoice) | Penerimaan barang oleh **gudang** dengan **menarik data voucher PO**. Belum jurnal akuntansi. |
| **4. Purchase Invoice** | ✅ Ya | `Dr Persediaan / Inventory` \| `Cr Utang Usaha (AP)`  *(+ `Dr PPN Masukan` bila ada faktur pajak)* | **Menarik data Received Item** saat entry. **Di sinilah jurnal akuntansi terjadi** — akui persediaan & Utang Usaha. |
| **5. Purchase Return** | ✅ Ya | **Reversal otomatis oleh sistem** | Barang dikembalikan → sistem membalik jurnal pembelian (mengurangi persediaan & utang). |
| **6. Purchase Payment** | ✅ Ya | `Dr Utang Usaha (AP)` \| `Cr Kas/Bank` | Saat entry cukup input **dibayar via bank/kas**; auto-jurnal melunasi utang. |

> **Inti:** PR & PO = catatan + approval (**tanpa jurnal**). Receive Items = **penerimaan gudang**
> (tarik PO, belum jurnal). **Jurnal akuntansi baru terjadi di Purchase Invoice** (`Dr Persediaan |
> Cr Utang Usaha`), dan ditutup di **Purchase Payment** (`Dr Utang Usaha | Cr Kas/Bank`).

---

## 3. Prinsip Logika Penting

1. **Setup item → COA:** tiap item terhubung ke akun Persediaan/Inventory di awal → dasar auto-jurnal.
2. **Data mengalir antar dokumen:** PO → ditarik oleh Receive Items → ditarik oleh Purchase Invoice.
   Ini otomatis menjaga **3-way match** (pesan ↔ terima ↔ faktur) & mencegah salah jumlah/harga.
3. **Titik jurnal = Purchase Invoice** (bukan saat terima barang, pada model ini).
4. **PPN Masukan** diakui saat Purchase Invoice (bila ada faktur pajak).
5. **Retur = reversal otomatis** oleh sistem (tak perlu jurnal manual).
6. **Alur Utang (AP):** Purchase Invoice menaikkan AP → Purchase Payment menurunkan AP.

**Kenapa jurnal di Purchase Invoice (bukan saat Receive Items)?** Karena **umumnya vendor mengirim
barang sekaligus dengan invoice/tagihan** — begitu barang diterima, tagihan sudah ada, jadi utang
sudah pasti walau **tempo pembayaran** belakangan. Maka cukup **satu jurnal di Purchase Invoice**.
*(Sebagian sistem menyediакan auto-jurnal "barang diterima belum ditagih/GRNI" saat Receive Items;
itu baru relevan bila ada **jeda waktu signifikan** antara penerimaan barang dan terbitnya invoice.)*

---

## 4. Ringkasan (satu tarikan napas)

`PR & PO = catatan + approval (tanpa jurnal)` → `Receive Items = penerimaan gudang, tarik PO` →
`Purchase Invoice = JURNAL: Dr Persediaan | Cr Utang Usaha (+PPN Masukan)` →
`Purchase Payment = Dr Utang Usaha | Cr Kas/Bank`. (Retur = reversal otomatis.)

---

## 5. Purchase Invoice — Detail Field Data Entry

**Purchase Invoice = faktur pembelian dari vendor.** Seperti di penjualan, user **memilih data** lewat
**dropdown ▼** dan **opsi search**; sistem menghitung pajak & total, lalu membuat jurnal otomatis.

### Field yang diisi

**a) Bagian atas (vendor & dokumen):**
- **Vendor** ▼ — pilih dari master vendor (otomatis menarik alamat & termin).
- **Select PO** ▼ — tarik data dari **Purchase Order** bila ada (item langsung terisi).
- **Vendor is Taxable** ☑ dan **Inclusive Tax** ☑ — apakah kena PPN & apakah harga sudah termasuk PPN.
- **Form No.** (otomatis), **Invoice No.**, **Invoice Date**, **Ship Date**, **Terms** ▼ (mis. Net 14),
  **A/P Account** ▼ (akun **Utang** yang dipakai).

**b) Isi transaksi — bisa lewat 3 cara:**

1. **Lewat Item** (tab *Items*) — untuk **beli barang/persediaan**. Pilih **Item** (search) dari master
   (menarik harga & COA), isi **Qty**, **Unit Price**, **Tax**, dan **Dept.** (search). Amount dihitung
   otomatis. Cocok untuk stok yang masuk gudang.
2. **Lewat Akun COA** (tab *Expense*) — untuk **beli jasa/biaya** (mis. internet, biaya bank). Pilih
   **Account No.** (search) dari daftar COA, isi **Amount**, **Notes**, dan **Department** (search).
3. **Kombinasi** — item **dan** biaya tambahan sekaligus (mis. beli barang + ongkos/biaya admin).

> **Insight penting:** sebuah "item" bisa **disetel setara akun biaya di COA** (item-for-expense).
> Kalau begitu, **hasil jurnalnya sama persis** apakah biaya diinput lewat **Item** atau lewat tab
> **Expense** — jadi user boleh pakai cara yang paling nyaman.

### PPN: Exclusive vs Inclusive
- **Exclusive (tidak termasuk):** PPN **ditambahkan** di atas harga. Contoh Rp3.000.000 → PPN
  Rp330.000 → total Rp3.330.000.
- **Inclusive (sudah termasuk):** PPN **dikeluarkan** dari harga. Contoh Rp3.000.000 sudah termasuk
  PPN → beban bersih Rp2.702.702 + PPN Rp297.298.

### Auto-jurnal yang terbentuk

**Contoh 1 — beli persediaan (Exclusive PPN):** 50 unit × Rp110.000 = Rp5.500.000, PPN Rp605.000.
```
Dr  Persediaan            5.500.000
Dr  PPN Masukan             605.000
    Cr  Utang Usaha             6.105.000
```

**Contoh 2 — beli biaya, kombinasi item + biaya bank (Inclusive PPN):** internet Rp3.000.000
(termasuk PPN) + biaya bank Rp5.000 (tidak kena pajak).
```
Dr  Beban Internet        2.702.702
Dr  Beban Bank                5.000
Dr  PPN Masukan             297.298
    Cr  Utang Usaha             3.005.000
```
> Pola umum pembelian: **Dr Persediaan/Beban + Dr PPN Masukan | Cr Utang Usaha.** Bila ada pemotongan
> **PPh Pasal 23** (mis. atas jasa), nilainya muncul di bagian bawah dan mengurangi kas yang dibayar
> saat pelunasan. Tombol **Show Journal** menampilkan jurnal ini untuk verifikasi.

---

## 6. Purchase Payment (Pembayaran ke Vendor) — Detail Field Data Entry

**Purchase Payment = membayar utang (faktur) ke vendor.** Dibuka dari layar **Purchase Invoice →
klik tombol "Purchase Payment"**, sehingga banyak field **terisi otomatis** dan faktur yang dibayar
langsung **tercentang lunas (Paid)**.

### Field yang diisi
- **Vendor / Payee** — **otomatis terisi** dari Purchase Invoice.
- **Form No.** (otomatis) & **Payment Date** — tanggal bayar.
- **Bank** — **akun kas/bank pembayar** (user tinggal pilih dari mana uang keluar). Saldo bank
  ditampilkan sebagai info.
- **Memo**, dan (bila pakai cek) **Cheque No./Date/Amount**.
- **Grid faktur:** Invoice No., Date, **Due (jatuh tempo)**, Amount, **Owing (sisa)**,
  **Payment Amount**, **Disc./W-H Amount**, **Paid** (tercentang otomatis untuk faktur yang dibuka).

> **Intinya user cukup memilih bank pembayar dan jumlahnya — tidak perlu memikirkan jurnalnya,
> karena jurnal terbentuk otomatis.**

### Auto-jurnal yang terbentuk (contoh)
Faktur Rp3.890.000 dibayar, dengan potongan **PPh Pasal 23 Rp70.000** (jasa), kas keluar Rp3.820.000:
```
Dr  Utang Usaha (A/P)                 3.890.000
    Cr  Kas/Bank                          3.820.000
    Cr  Utang Pajak — PPh 23 (dipotong)      70.000
```
> **Utang lunas penuh (3.890.000), tapi kas keluar lebih kecil** karena Rp70.000 ditahan sebagai
> **PPh 23** yang nanti disetor ke negara. Ini penutup siklus pembelian.

### Dua catatan penting
1. **Akun utang harus cocok.** Akun **A/P** yang dipilih di Purchase Invoice akan **otomatis
   didebit** saat Purchase Payment (mis. pilih "A/P Others" di faktur → Purchase Payment mendebit
   "A/P Others" juga). Buku Besar Utang (**dan Sub-Buku Besar per vendor**) ter-update otomatis.
2. **Faktur "Owing" yang belum jatuh tempo = kemungkinan recurring.** Yaitu **biaya berulang tiap
   bulan** yang fakturnya **dientry di muka**. Manfaatnya: biaya bulan berjalan sudah tercatat
   walau vendor belum menagih, sekaligus jadi **estimasi kebutuhan kas (cash flow)** ke depan.

> **Catatan untuk Tere (to-do):** dua topik ini akan ada **file update tersendiri** →
> **(a) mekanisme Recurring** (transaksi berulang), dan **(b) Buku Besar Utang (GL A/P) + Sub-GL per
> vendor**. Keduanya saya masukkan ke daftar tunggu. *(Ditandai.)*

---

*Alur & logika di atas melengkapi kerangka modul Purchase.*
