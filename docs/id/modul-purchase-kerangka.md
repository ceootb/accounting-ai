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

*(Catatan opsional: sebagian setup mengakui "barang diterima belum ditagih/GRNI" saat Receive Items.
Pada model ini jurnal disatukan di Purchase Invoice sesuai praktik yang dipakai.)*

---

## 4. Ringkasan (satu tarikan napas)

`PR & PO = catatan + approval (tanpa jurnal)` → `Receive Items = penerimaan gudang, tarik PO` →
`Purchase Invoice = JURNAL: Dr Persediaan | Cr Utang Usaha (+PPN Masukan)` →
`Purchase Payment = Dr Utang Usaha | Cr Kas/Bank`. (Retur = reversal otomatis.)

*Detail field tiap dokumen (vendor, item, qty, harga, pajak, termin, dsb) dilengkapi di dokumen berikutnya.*
