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

*Detail field entry modul Sales dilengkapi berikutnya.*
