# Other Payment (Pengeluaran Kas/Bank Langsung ke GL)

**Other Payment** adalah transaksi **pengeluaran Cash/Bank langsung ke akun GL**, yang **TIDAK** dipakai
untuk *settlement* **Sales Invoice (AR)** atau **Purchase Invoice (AP)**.

**Bentuk jurnalnya:**
```
Dr  Akun tujuan (Beban / Aset / Liabilitas)
    Cr  Kas / Bank
```

## Kapan dipakai (typical use)

- Pembayaran biaya/beban **langsung**; **biaya administrasi bank**;
- Pembelian **perlengkapan** yang langsung dibebankan; **beli Fixed Asset tunai**; **prepaid expense**;
- Pembayaran **kewajiban non-trade / Other Liability**;
- Pengeluaran Kas/Bank lain yang **tidak berhubungan** dengan AR/AP vendor.

## Pemisahan AR / AP wajib

Ada **tiga jalur** pengeluaran/penerimaan yang **tidak boleh tertukar**:

| Jalur | Alur |
|---|---|
| **AR** (customer invoice) | Customer → **Sales Receipt** → AR **Customer Sub-GL** → Kas/Bank |
| **AP** (vendor invoice) | Vendor → **Purchase Payment** → AP **Vendor Sub-GL** → Kas/Bank |
| **Other Payment** | **Direct** → **akun GL** → Kas/Bank |

**Other Payment TIDAK:** memakai Customer/Vendor Sub-GL; memilih Sales/Purchase Invoice untuk
*settlement*; melakukan alokasi AR/AP; mengubah saldo **piutang customer**; atau mengubah saldo **utang
usaha/vendor**.

## "Bayar hutang" ≠ selalu Purchase Payment

Yang menentukan **bukan** kata "bayar hutang", melainkan **jenis liability & subledger-nya**:
- **Hutang Usaha / AP** yang **linked ke Vendor** → **Purchase Payment**.
- **Other Liability** yang **tidak** linked ke Vendor/AP → boleh dilunasi lewat **Other Payment**.

```
Melunasi Other Liability (non-vendor):
Dr  Other Liability
    Cr  Bank
```
> Ini mengurangi saldo **Other Liability** di GL, tetapi **tidak** mengurangi saldo **AP Vendor** dan
> **tidak** memerlukan Vendor.

## Contoh jurnal

```
A. Bayar listrik        : Dr Beban Listrik            | Cr Bank
B. Beli Fixed Asset tunai: Dr Aset Tetap              | Cr Bank
C. Bayar admin bank     : Dr Beban Administrasi Bank  | Cr Bank
D. Lunasi Other Liability: Dr Other Liability         | Cr Bank
```

## Field (referensi UI)

- **Header:** Paid From / akun **Kas-Bank**, Voucher No., Cheque No. (jika ada), Date, Memo, Payee, Amount.
- **Detail:** Account No., Account Name, Amount, **Department**, Memo.
  - **Account No.** = **semua akun kecuali AP yang ber-Sub-GL** → karena itu **tidak ada kolom Sub GL**
    di layar Other Payment.
  - **Department** hanya **dimensi tracking** bila diperlukan — **bukan** indikator bahwa transaksi itu
    AR/AP.

## Aturan inti

> **Other Payment = pengeluaran Kas/Bank langsung ke GL, tanpa AR/AP subledger.** Jangan berasumsi
> *"bayar hutang = AP Vendor"*. Cek dulu: liability itu **Hutang Usaha (linked Vendor)** → Purchase
> Payment; atau **Other Liability (tanpa Vendor/AP)** → Other Payment.

> **Cerminannya — Other Deposit:** penerimaan Kas/Bank **langsung ke GL** (bukan *settlement* AR):
> `Dr Kas/Bank | Cr akun GL`. *(Detail Other Deposit menyusul.)*
