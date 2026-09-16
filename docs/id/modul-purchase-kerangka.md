# Modul Pembelian (Purchase) — Kerangka & Logika

> Kerangka siklus **Procure-to-Pay (P2P)** dan logika akuntansinya. Fokus di **alur + logika +
> auto-jurnal per langkah** dulu; **detail field** menyusul.
> *(Draft — dikurasi akuntan praktik.)*

---

## 1. Alur 6 Langkah (Procure-to-Pay)

```
1. Purchase Requisition (PR)   — permintaan pembelian internal
2. Purchase Order (PO)         — pesanan resmi ke vendor
3. Receive Items (Penerimaan)  — barang/jasa diterima (GRN)
4. Purchase Invoice (Faktur)   — faktur/tagihan dari vendor
5. Purchase Return (Retur)     — pengembalian barang (jika ada)
6. Purchase Payment (Bayar)    — pembayaran ke vendor
```

---

## 2. Logika Menjurnal per Langkah

| Langkah | Menjurnal? | Auto-jurnal | Catatan |
|---|---|---|---|
| **1. Purchase Requisition** | ❌ Tidak | — | Dokumen internal (permintaan/approval). Belum ada dampak keuangan. |
| **2. Purchase Order** | ❌ Tidak | — | Komitmen ke vendor (off-balance). Belum mengubah posisi keuangan. |
| **3. Receive Items** | ✅ Ya | `Dr Persediaan` \| `Cr Utang Belum Ditagih` | Barang diterima → aset (persediaan) bertambah, muncul kewajiban sementara (*received not invoiced*). |
| **4. Purchase Invoice** | ✅ Ya | `Dr Utang Belum Ditagih` (atau Persediaan/Beban) + `Dr PPN Masukan` \| `Cr Utang Usaha (AP)` | Faktur vendor → akui **Utang Usaha** & **PPN Masukan**; tutup "utang belum ditagih". |
| **5. Purchase Return** | ✅ Ya | `Dr Utang Usaha` \| `Cr Persediaan` (+ balik PPN Masukan) | Kebalikan pembelian; mengurangi utang & persediaan. |
| **6. Purchase Payment** | ✅ Ya | `Dr Utang Usaha (AP)` \| `Cr Kas/Bank` | Melunasi utang; kas/bank berkurang. |

> **Inti:** Langkah **1-2 tidak menjurnal** (dokumen komitmen). Jurnal mulai dari **Receive Items**,
> lalu **Purchase Invoice** (akui utang + PPN), dan ditutup di **Purchase Payment**.

---

## 3. Prinsip Logika Penting

1. **3-Way Match** (kontrol utama): sebelum membayar, cocokkan **PO ↔ Penerimaan Barang ↔ Faktur**
   (jumlah & harga). Mencegah bayar barang yang tidak dipesan / tidak diterima / beda harga.
2. **Tipe item menentukan akun debit:**
   - *Inventory part* → **Persediaan** (aset).
   - *Non-inventory / service / expense* → langsung **Beban** (bisa lewati langkah "Receive Items").
3. **PPN Masukan** diakui saat **Purchase Invoice** (faktur pajak terbit), **bukan** saat barang diterima.
4. **Received-not-invoiced:** jika barang diterima sebelum faktur, pakai akun sementara "Utang Belum
   Ditagih" (accrued), lalu dipindahkan ke Utang Usaha saat faktur masuk.
5. **Alur utang (AP):** Faktur menaikkan AP → Pembayaran menurunkan AP. Saldo AP = tagihan belum dibayar.

---

## 4. Ringkasan (satu tarikan napas)

`PR & PO = komitmen (tanpa jurnal)` → `Receive = aset masuk + utang sementara` →
`Invoice = Utang Usaha + PPN Masukan` → `Payment = Utang Usaha lunas, kas keluar`.
(Retur = pembalik bila ada pengembalian.)

*Detail field tiap dokumen (vendor, item, qty, harga, pajak, termin, dsb) dilengkapi di dokumen berikutnya.*
