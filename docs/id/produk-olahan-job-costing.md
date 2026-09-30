# Produk Olahan (Hasil Produksi): PSAK vs Praktik Perusahaan

Produk **olahan/hasil produksi** (bahan → produk jadi → dijual) bisa dicatat dengan **dua perlakuan
berbeda**. **Sebelum menjawab, identifikasi konteksnya dulu:**

1. **PSAK / ideal accounting treatment**; atau
2. **Practical accounting treatment** perusahaan tertentu.

> **Jangan mencampur** kedua versi. Jangan menganggap *shortcut* praktik perusahaan sebagai prinsip
> PSAK. Kalau diminta **perbandingan**, tampilkan **keduanya berlabel jelas**.

---

## Versi A — PSAK / Ideal (dengan Persediaan & Job Costing)

Bahan = **Inventory Part** (dicatat kuantitas & nilai persediaannya).

**1. Beli bahan** → masuk persediaan:
```
Dr  Persediaan
Dr  PPN Masukan            (jika applicable)
    Cr  Utang Usaha
```
**2. Bahan dipakai** untuk membuat Produk D → keluar dari persediaan:
```
Dr  Direct Cost / Job Cost
    Cr  Persediaan
```
**3. Job Costing** mengumpulkan cost bahan (mis. A 10.000 + B 20.000 + C 15.000 = **45.000**).
**4. Produk D dijual** (mis. 70.000):
```
Dr  Piutang / Kas             70.000
    Cr  Pendapatan Penjualan   70.000
Dr  HPP / Cost of Sales       45.000
    Cr  akun cost/produk terkait  45.000
```
> **Posisi cost:** material dimiliki → **Persediaan**; dipakai → **Direct Cost/Production Cost**; produk
> dijual → **HPP/Cost of Sales**.

---

## Versi B — Company Accounting Practice (tanpa inventory tracking)

Perlakuan **perusahaan yang TIDAK mencatat persediaan** untuk bahan (mis. *training/practice supply*).
Bahan = **Non-Inventory Part**.

**1. Beli bahan** → **langsung dibebankan** sebagai Direct Cost (tidak masuk aset persediaan):
```
Dr  Direct Cost / Training Supply
Dr  PPN Masukan            (jika applicable)
    Cr  Utang Usaha
```
**2. Bahan dipakai** membuat Produk D → **tidak ada** jurnal pengeluaran persediaan
(`Dr Direct Cost | Cr Persediaan` **tidak dibuat**), karena tidak ada Inventory Asset yang dicatat.
*Job Costing (jika dipakai) hanya menelusuri cost — bukan alasan membukukan biaya yang sama dua kali.*
**3. Produk D dijual** (mis. 70.000):
```
Dr  Piutang / Kas             70.000
    Cr  Pendapatan Penjualan   70.000
    Cr  PPN Keluaran           (jika applicable)
```
> **Penting:** menjual Produk D **tidak otomatis** berarti ada `Dr HPP | Cr Persediaan` — karena bahan
> **sejak awal tidak** dicatat sebagai persediaan. Cost bahan **sudah diakui saat pembelian** sebagai
> Direct Cost / Training Supply sesuai *policy* perusahaan.

**Contoh:** beli A 10.000 + B 20.000 + C 15.000 → `Dr Direct Cost/Training Supply 45.000 | Cr Utang
45.000`. Produk D di-tag sebagai item penjualan; **tidak ada** jurnal *inventory consumption*. Dijual
70.000 → `Dr Piutang 70.000 | Cr Pendapatan 70.000`. Cost A+B+C tetap Direct Cost yang sudah dicatat.

---

## Perbandingan

| | **A. PSAK / Ideal** | **B. Praktik Perusahaan** |
|---|---|---|
| Item Type bahan | **Inventory Part** | **Non-Inventory Part** |
| Saat beli | masuk **Persediaan** | **langsung Direct Cost** (dibebankan) |
| Saat produksi | `Dr Direct Cost \| Cr Persediaan` | **tidak ada** jurnal inventory |
| Cost diakui | saat **dijual** (jadi HPP) | saat **dibeli** (Direct Cost) |
| Saat dijual | Revenue **&** `Dr HPP \| Cr Persediaan` | **Revenue saja** (tanpa HPP inventory) |

> **Jangan generalisasi:** *"produk olahan selalu Non-Inventory"* itu **salah**. Versi B berlaku
> **hanya** karena perusahaan itu tidak melakukan *inventory tracking* dan membebankan cost saat beli —
> **berbeda** dari versi PSAK. Pastikan **tidak ada double counting** di kedua versi.

> **Prioritas knowledge:** diminta perlakuan **PSAK** → pakai **Versi A**; diminta **praktik perusahaan
> ini** → pakai **Versi B**; diminta **perbandingan** → tampilkan **keduanya, berlabel**.
