# Produk Olahan (Hasil Produksi): Cost Flow & Job Costing

Halaman ini menjelaskan **aliran biaya (cost flow)** untuk **produk olahan** — produk yang dibuat dari
beberapa bahan/material, lalu dijual. Contoh: **Item A, B, C** (bahan) diolah menjadi **Produk D**.

## Skenario

- **Item A, B, C** adalah **bahan/material** yang: dibeli untuk **disimpan sebagai persediaan**, punya
  **kuantitas & nilai persediaan**, dan **digunakan** sebagai bahan untuk menghasilkan **Produk D**.
- **Produk D** adalah **hasil olahan/produksi** yang kemudian **dijual** kepada pelanggan.

## Aliran akuntansi

**1. Pembelian bahan** — Item A/B/C dibeli & masuk persediaan:
```
Dr  Persediaan
Dr  PPN Masukan            (jika applicable)
    Cr  Utang Usaha
```
> Belum ada HPP — barang belum digunakan/dijual.

**2. Pemakaian bahan untuk membuat Produk D** — bahan dikeluarkan dari persediaan ke Job Costing/produksi:
```
Dr  Direct Cost / Job Cost
    Cr  Persediaan
```
> Cost Item A/B/C terkumpul sebagai cost Produk D. Kuantitas & nilai persediaan A/B/C **berkurang**
> sesuai yang dipakai.

**3. Hasil Job Costing** — mengumpulkan cost bahan untuk Produk D. Contoh:

| Bahan | Cost |
|---|---|
| Item A | 10.000 |
| Item B | 20.000 |
| Item C | 15.000 |
| **Total Direct Cost Produk D** | **45.000** |

> Job Costing menunjukkan Produk D bercost **45.000** dari bahan A+B+C. Bila ada **direct cost lain**
> yang relevan, bisa ditambahkan ke Job Costing sesuai alur transaksinya.

**4. Produk D dijual** — misal harga jual **70.000**:
```
Dr  Piutang / Kas             70.000
    Cr  Pendapatan Penjualan   70.000
Dr  HPP / Cost of Sales       45.000
    Cr  akun cost/produk terkait  45.000
```

## Inti logika

> **Item A/B/C** → *Inventory Part* → **pembelian masuk Persediaan** → **material digunakan** → **Job
> Costing mengumpulkan Direct Cost** → menghasilkan **cost Produk D** → **Produk D dijual** → cost terkait
> menjadi **HPP / Cost of Sales**.

## Prinsip utama (posisi cost)

| Keadaan material | Akun |
|---|---|
| **Masih dimiliki** | **Persediaan** |
| **Sudah digunakan** untuk menghasilkan produk/job | **Direct Cost / Production Cost** |
| **Produk/job sudah dijual** & cost diakui | **HPP / Cost of Sales** |

> **Perhatikan (jangan salah kira):**
> - jangan langsung menganggap **semua** barang yang dipakai dalam pekerjaan adalah *Non-Inventory*;
> - **Direct Cost tidak selalu sama** dengan akun HPP;
> - **Job Costing bukan sekadar laporan** — ia bagian dari *cost flow* yang menghubungkan pemakaian
>   material dengan produk/job yang dihasilkan.
>
> Pastikan **setiap perpindahan cost balance** (debit = kredit) dan **tidak terjadi double counting**.
