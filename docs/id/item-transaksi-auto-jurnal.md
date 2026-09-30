# Item di Transaksi: Mapping Akun & Auto-Jurnal (per Jenis Item)

Satu **Master Item** yang mapping akunnya benar bisa dipakai di **siklus pembelian dan penjualan**, dan
sistem membentuk **jurnal otomatis** sesuai **jenis item + akun yang dipetakan**. Prinsipnya:

> **Item benar → mapping benar → jurnal otomatis benar.** User operasional cukup memilih item; tidak
> memilih akun Persediaan/HPP/Beban secara manual tiap transaksi.

*(Nama akun di bawah **generik** — sesuaikan dengan COA perusahaan; yang penting fungsinya.)*

## 1. Inventory Part (barang stok)

Dibeli → masuk **Persediaan**; dijual → **Pendapatan** + pelepasan **HPP**. Satu item, dua siklus.

**Beli (Purchase Invoice):**
```
Dr  Persediaan
Dr  PPN Masukan            (jika ada)
    Cr  Utang Usaha
```
**Jual (Sales Invoice):**
```
Dr  Piutang Usaha
    Cr  Pendapatan
    Cr  PPN Keluaran        (jika ada)
Dr  HPP (COGS)
    Cr  Persediaan
```

## 2. Non-Inventory Part (bukan stok → langsung beban)

Non-Inventory Part **tidak** dicatat sebagai persediaan. Akun yang dipetakan = **akun Beban (Expense
Account)**. Saat dibeli, nilainya **langsung dibebankan**, bukan menjadi aset persediaan.

**Beli (Purchase Invoice):**
```
Dr  Beban (akun beban item)
Dr  PPN Masukan            (jika ada)
    Cr  Utang Usaha
```
> **Non-Inventory Part ≠ Inventory Part.** Jangan menerapkan jurnal persediaan ke non-inventory —
> pembeliannya **langsung ke beban**, tidak lewat aset persediaan.

## 3. Service (jasa → pendapatan)

Service Item = **penjualan jasa**, bukan persediaan. Akun yang dipetakan = **akun Pendapatan (Sales
Account)**.

**Jual (Sales Invoice):**
```
Dr  Piutang Usaha
    Cr  Pendapatan Jasa
    Cr  PPN Keluaran        (jika ada)
```
**Diskon** (bila dicatat terpisah) diperlakukan sebagai **pengurang pendapatan** (contra-revenue,
posisi **Debit**) sesuai **PSAK 72**. Jika harga transaksi sudah dicatat **net**, **tidak perlu**
jurnal diskon terpisah.

## Prinsip & pembedaan jenis kesalahan

Karena treatment sudah disiapkan di master item, transaksi rutin jadi aman. Bila hasil jurnal tampak
salah, bedakan **sumbernya**:

| Gejala | Sumber kesalahan |
|---|---|
| User memilih item yang salah | **Human input error** (bukan salah sistem) |
| Mapping item salah sejak setup | **Master-data / setup error** |
| Jurnal tidak sesuai mapping/aturan | **Accounting engine / system error** |

> **Intinya:** *jenis item menentukan akun yang dipetakan, dan akun itu menentukan jurnal otomatis di
> pembelian/penjualan.* Kontrol akuntansi ada di **master item** — bukan di layar transaksi.

> **Departemen:** bisa di-set di **master item** **atau** diisi langsung saat **Sales/Purchase Invoice**; nilainya **otomatis mengalir ke jurnal** (`journal_line` → Departemen) untuk laporan per departemen. Jadi tak wajib diisi di setup item — bisa ditentukan saat transaksi.
