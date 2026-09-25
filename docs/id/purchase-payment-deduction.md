# Purchase Payment dengan Potongan (Deduction)

Saat **membayar vendor** lewat **Purchase Payment**, perusahaan (sebagai **pemotong pajak**) memotong
PPh dari pembayaran. Potongan dicatat di **kolom potongan / *deduction*** (di software berlabel
*Discount / Write-off*); kas yang keluar = tagihan − potongan.

> **Kunci — kebalikan dari sisi Sales Receipt:** di sini semua potongan pajak masuk ke **Utang Pajak
> (Tax Payable)**, karena perusahaan **menahan pajak** dari vendor untuk **disetor ke negara**. Bukan
> aset dan bukan beban — melainkan **kewajiban**.

## Akun: semua ke Utang Pajak (per jenis PPh)

| Jenis potongan | Akun tujuan | Sifat |
|---|---|---|
| **PPh 23** (jasa) | **Utang PPh 23** *(Tax Payable – W/H ps.23)* | Kewajiban |
| **PPh 21** (mis. jasa orang pribadi) | **Utang PPh 21** *(Tax Payable – W/H ps.21)* | Kewajiban |
| **PPh final sewa** (Pasal 4 ayat 2) | **Utang PPh Final Ps.4(2)** *(Tax Payable – W/H ps.4(2))* | Kewajiban |

## Contoh jurnal (konsep)

**a) PPh 23** — tagihan Rp5jt, dipotong PPh 23 Rp90rb:
```
Dr  Utang Usaha                    5.000.000
    Cr  Utang PPh 23                  90.000
    Cr  Kas/Bank                   4.910.000
```

**b) PPh 21** — jasa (retainer) Rp10jt, dipotong PPh 21 Rp250rb (2,5%):
```
Dr  Utang Usaha                   10.000.000
    Cr  Utang PPh 21                 250.000
    Cr  Kas/Bank                   9.750.000
```

**c) PPh final sewa gedung** (Pasal 4 ayat 2) — sewa Rp149,85jt, dipotong final 10% Rp14.985.000:
```
Dr  Utang Usaha                  149.850.000
    Cr  Utang PPh Final Ps.4(2)     14.985.000
    Cr  Kas/Bank                  134.865.000
```

Perusahaan lalu **menyetor** pajak yang ditahan ke negara dan **menerbitkan bukti potong** untuk vendor.

## Kontras dengan sisi penerimaan (Sales Receipt)

| Potongan PPh | **Purchase Payment** (kita **memotong**) | **Sales Receipt** (kita **dipotong**) |
|---|---|---|
| PPh 23 | **Utang PPh 23** (kewajiban) | **PPh 23 Dibayar Dimuka** (aset/kredit pajak) |
| PPh final (sewa) | **Utang PPh Final** (kewajiban) | **Beban Pajak Final** (beban) |

> **Intinya:** yang **memotong** mencatat **Utang Pajak** (menahan → setor ke negara); yang **dipotong**
> mencatat **kredit pajak / beban**. Lihat dua sisi lengkapnya di
> [Tips: Jurnal Potongan PPh 23](tips-pph23-jurnal.md) dan sisi penerimaan di
> [Sales Receipt dengan Potongan](sales-receipt-deduction.md).
