# Tips: Jurnal Potongan PPh Pasal 23 (Dua Sisi)

> **PPh Pasal 23** = pajak yang dipotong atas **jasa** (dan sewa, royalti, dll). Ada **dua sisi** yang
> sering membingungkan: saat perusahaan **memotong** (beli jasa) vs saat perusahaan **dipotong**
> (jual jasa). Kuncinya: yang memotong mencatat **Utang PPh 23**, yang dipotong mencatat **PPh 23
> Dibayar Dimuka (Prepaid)**. Contoh tarif memakai **2%** dari nilai jasa (DPP).

---

## Sisi 1 — Perusahaan sebagai PEMOTONG (beli jasa dari vendor)

Saat membeli **jasa**, perusahaan **wajib memotong** PPh 23 dari vendor, lalu **menyetorkannya ke
negara**. Artinya yang dibayar ke vendor **berkurang** sebesar PPh yang dipotong.

**Cara di Purchase Invoice:** isi bagian **PPh 23** pada faktur (pilih akun & tarifnya) → sistem
menghitung potongannya otomatis dan membentuk **Utang PPh 23**.

**Contoh:** jasa konsultan DPP Rp10.000.000 + PPN Masukan Rp1.100.000; PPh 23 2% = Rp200.000.
```
Dr  Beban Jasa Konsultan          10.000.000
Dr  PPN Masukan                    1.100.000
    Cr  Utang Usaha (ke vendor)        10.900.000
    Cr  Utang PPh 23 (setor ke negara)    200.000
```
> Tagihan vendor Rp11.100.000, tapi yang dibayar hanya **Rp10.900.000**; sisanya **Rp200.000**
> ditahan sebagai **Utang PPh 23** untuk disetor ke negara. Perusahaan lalu membuat **bukti potong**
> untuk vendor. *(Ini juga muncul di [Purchase Payment](modul-purchase-kerangka.md#6-purchase-payment-pembayaran-ke-vendor--detail-field-data-entry) — kas keluar lebih kecil dari utang.)*

---

## Sisi 2 — Perusahaan sebagai PIHAK DIPOTONG (jual jasa ke pelanggan)

Saat **menjual jasa**, pelanggan (jika pemotong pajak) akan **memotong** PPh 23 dari pembayarannya.
Akibatnya **uang yang diterima kurang** dari nilai faktur. Selisih "kurang bayar" itu **bukan
kerugian** — melainkan **PPh 23 Dibayar Dimuka (Prepaid)**, yaitu **kredit pajak** yang nanti
mengurangi PPh Badan perusahaan di akhir tahun.

**Saat Sales Invoice** (mengakui pendapatan jasa) — nilai penuh:
```
Dr  Piutang Usaha                 11.100.000
    Cr  Pendapatan Jasa               10.000.000
    Cr  PPN Keluaran                   1.100.000
```

**Saat pembayaran diterima** (pelanggan memotong PPh 23 Rp200.000) — inilah kunci yang diminta:
```
Dr  Kas/Bank                      10.900.000
Dr  PPh 23 Dibayar Dimuka (Prepaid)   200.000
    Cr  Piutang Usaha                 11.100.000
```
> Piutang **lunas penuh Rp11.100.000**, tapi kas masuk hanya **Rp10.900.000**. Selisih **Rp200.000**
> **tidak boleh** dibiarkan menggantung di piutang — harus **dijurnal ke PPh 23 Dibayar Dimuka**
> (akun **Aset**). Dasarnya adalah **bukti potong** yang diberikan pelanggan; simpan bukti itu karena
> menjadi **pengurang PPh Badan** di SPT Tahunan.

---

## Ringkasan

| Posisi | Peran | Akun PPh 23 | Sifat |
|---|---|---|---|
| **Beli jasa** | Pemotong | **Utang PPh 23** | Kewajiban (disetor ke negara) |
| **Jual jasa** | Dipotong | **PPh 23 Dibayar Dimuka** | Aset (kredit pajak) |

> **Inti:** DPP PPh 23 = nilai **jasa** (di luar PPN). Yang memotong → **Utang PPh 23**; yang dipotong →
> **Prepaid PPh 23**. Untuk penjual, "kurang bayar" akibat pemotongan **wajib** dipindahkan ke Prepaid
> PPh 23 agar piutang tetap lunas dan kredit pajak tercatat.
