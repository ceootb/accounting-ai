# Other Deposit (Penerimaan Kas/Bank Non-Customer / di Luar AR)

**Other Deposit** adalah transaksi untuk mencatat **uang masuk ke Kas/Bank** yang **bukan** berasal dari
**Customer/AR** dan **bukan** penerimaan dari siklus penjualan.

**Bentuk jurnalnya:**
```
Dr  Kas / Bank
    Cr  Akun Lawan
```
> **Akun lawan ditentukan berdasarkan SUBSTANSI transaksi**, bukan berdasarkan nama modul. **Other
> Deposit ≠ selalu Other Income.**

## Fungsi & batasan

- Dipakai untuk **penerimaan Kas/Bank di luar Customer Receipt / AR**.
- **Jangan** dipakai untuk **pelunasan piutang Customer.** Jika uang masuk = pembayaran Sales Invoice/AR
  (`Dr Kas/Bank | Cr Piutang Customer`), **harus** lewat **Customer Receipt** agar *linkage* Customer &
  Invoice/AR tetap terbentuk.
- **Juga bukan** untuk **transfer antar Kas/Bank** — pakai mekanisme transfer yang sesuai.

## Akun lawan mengikuti substansi (bukan otomatis pendapatan)

```
Penerimaan bunga bank   : Dr Bank | Cr Pendapatan Bunga
Substansinya aset       : Dr Bank | Cr Akun Aset yang sesuai
Substansinya kewajiban  : Dr Bank | Cr Akun Kewajiban yang sesuai
```

## Field (referensi UI)

- **Deposit To** = akun **Kas/Bank** yang **menerima** uang.
- **Account No** = **akun lawan** dari COA. **Akun AR tidak digunakan**; **jangan** membuat *linkage*
  AR/Customer.
- **Detail:** Account No, Account Name, **Amount** (nilai akun lawan), **Department** (dimensi pelaporan,
  tidak mengubah fungsi), **Memo**.
- **Total Deposit** harus **seimbang** dengan total detail.

## Contoh

```
1. Penerimaan bunga bank Rp500.000:
   Deposit To = Bank ; Account No = Pendapatan Bunga
   Dr Bank 500.000 | Cr Pendapatan Bunga 500.000

2. Penerimaan yang substansinya aset:
   Dr Bank xxx | Cr Akun Aset xxx
```
> **Jangan** otomatis mengklasifikasikan semua Other Deposit sebagai *revenue*.

## Hubungan dengan Other Payment

Pasangan transaksi Kas/Bank **di luar siklus AR/AP**:

| | Kas/Bank | Akun lawan |
|---|---|---|
| **[Other Deposit](other-deposit-cash-bank.md)** | **masuk** (Debit) | **dikredit** |
| **[Other Payment](other-payment-cash-bank.md)** | **keluar** (Kredit) | **didebit** |

> Akun lawan **tetap** ditentukan berdasarkan **substansi** transaksi.

## Prinsip

> Pahami Other Deposit sebagai **"form uang masuk non-Customer / non-AR"** — **bukan** *"form khusus
> Other Income"*. Jangan berasumsi semua penerimaan = pendapatan. **Selalu identifikasi substansi** &
> pilih akun lawan yang tepat. **Jangan** membuat Customer/Invoice/AR *linkage* bila transaksi memang
> bukan dari Customer/AR.

> **Catatan:** *screenshot* = referensi **UI** untuk memperkuat konsep — jangan mengarang field/behaviour
> yang tak terlihat. Pisahkan **(1) konsep akuntansi, (2) behaviour software, (3) restriction UI**; jangan
> mengubah konsep akuntansi hanya karena keterbatasan UI. Tujuannya memahami **logic** & menghasilkan
> **jurnal yang benar berdasarkan substansi**, bukan meniru tampilan software.
