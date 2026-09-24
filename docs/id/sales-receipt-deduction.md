# Sales Receipt dengan Potongan (Deduction)

Saat menerima pembayaran lewat **Sales Receipt**, kadang uang yang diterima **lebih kecil dari
tagihan** karena ada **potongan (deduction)** — misalnya pelanggan **memotong pajak**, atau dana
**terpotong biaya bank**. Potongan ini dicatat di **kolom potongan / *deduction*** (di software field-nya
berlabel *Discount / Write-off*).

> **Ini *deduction* (pengurang pembayaran), bukan *sales discount* (potongan harga).** Potongan harga
> mengurangi **pendapatan**; sedangkan deduction di sini **tidak** mengurangi pendapatan — nilainya
> diarahkan ke **akun pajak/beban** sesuai jenis potongannya. Piutang tetap dianggap **lunas penuh**.

## Akun mengikuti jenis potongan

| Jenis potongan | Akun tujuan | Sifat |
|---|---|---|
| **PPh 23** (dapat dikreditkan) | **PPh 23 Dibayar Dimuka / Prepaid Tax** | Aset (kredit pajak) |
| **PPh final** (mis. atas sewa) | **Beban Pajak Final** | Beban (final, tak bisa dikreditkan) |
| **Non-pajak** (mis. biaya bank / adm fee) | **akun Beban** terkait (mis. Biaya Bank) | Beban |

## Contoh jurnal (konsep)

**a) Potongan PPh 23** — tagihan Rp350jt, dipotong PPh 23 Rp6.306.306:
```
Dr  Kas/Bank                     343.693.694
Dr  PPh 23 Dibayar Dimuka          6.306.306
    Cr  Piutang Usaha              350.000.000
```

**b) Potongan PPh final sewa** — satu Sales Receipt melunasi **3 faktur sewa** @Rp11,1jt (DPP Rp10jt +
PPN Rp1,1jt); tiap faktur dipotong final 10% × Rp10jt = Rp1jt:
```
Dr  Kas/Bank                      30.300.000
Dr  Beban Pajak Final              3.000.000
    Cr  Piutang Usaha              33.300.000
```

**c) Potongan biaya bank** — dana yang masuk sudah dipotong biaya bank:
```
Dr  Kas/Bank                      (nilai bersih diterima)
Dr  Beban Bank                    (biaya bank)
    Cr  Piutang Usaha             (nilai tagihan)
```
*(Untuk penerimaan dalam valuta asing bisa muncul baris tambahan selisih kurs; untuk Rupiah tidak.)*

## Satu Sales Receipt, beberapa Sales Invoice

Satu Sales Receipt bisa **melunasi beberapa Sales Invoice sekaligus**, masing-masing dengan potongannya
sendiri (lihat contoh sewa di atas). Pemantauan sisa tagihan tetap lewat **Owing** — lihat
[Sales Invoice — Pembayaran Bertahap (Owing)](sales-invoice-pembayaran-bertahap.md).

> **Intinya:** deduction pada Sales Receipt = **pengurang pembayaran**, bukan potongan harga. Kas yang
> diterima = tagihan − potongan; selisihnya masuk ke **akun pajak/beban sesuai jenisnya**, dan piutang
> tetap tercatat lunas. Terkait pajak: lihat [Tips: Jurnal Potongan PPh 23](tips-pph23-jurnal.md).
