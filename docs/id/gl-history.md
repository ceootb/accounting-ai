# General Ledger History (GL History)

**GL History** adalah **kumpulan posting jurnal per akun GL** yang bisa **difilter per kolom**, dicetak
lewat **Print Preview**, dan **di-drill-down kembali ke transaksi sumber (voucher)**. GL History adalah
**detail pembentuk Account Balance**, dan Account Balance mengalir ke **Laporan Keuangan** sesuai
**Account Type**.

## 1. Akses & workflow

Menu **General Ledger** → **GL History / Account History** → tentukan **filter periode & akun** →
report menampilkan **seluruh transaksi jurnal yang mempengaruhi akun** itu → tersedia **Print Preview**
untuk report formal.

## 2. Filter per kolom

**Setiap kolom bisa dipakai sebagai filter** (bukan hanya periode), sehingga tracking bisa spesifik.
Kolom: **Date, Source Type, Source No., Account No., Account Name, Description, Debit, Credit,
Department.**

## 3. Drill-down / trace ke sumber

GL History **bukan report statis.** **Dobel-klik** sebuah baris → sistem **drill-down ke transaksi
sumber** yang menghasilkan jurnal itu.
```
GL History → pilih transaksi → double-click → Source Type (mis. Purchase Invoice) → buka vouchernya
```
**Source Type** bisa dari berbagai transaksi: Purchase Invoice, Purchase Payment, Sales Invoice, Sales
Receipt, Journal Voucher, transaksi kas/bank, dll. **Source No.** = referensi untuk menemukan voucher
sumber yang tepat.

## 4. Dimensi mengikuti fungsi akun

- **AR** → bisa ada info **Customer / sub-GL**.
- **AP** → bisa ada info **Vendor / sub-GL**.
- **Revenue / Expense** → bisa ada **Department**.
- **Akun GL lainnya** → posting GL biasa tanpa sub-GL/Department.

> Contoh (SS): GL History akun **Salaries & Wages Expense** menampilkan **Department** tiap transaksi —
> jadi bisa ditelusuri **per akun sekaligus per Department**.

## 5. Tujuan report

Tracking jurnal harian · mencari **sumber suatu angka** di GL · investigasi **selisih** · memastikan
transaksi masuk ke **akun yang benar** · menelusuri sampai **voucher sumber** · review per **Department**
/ per **Source Type** · **audit trail** sederhana GL → source.

## 6. Print Preview (format minimal)

```
Date | Source Type | Source No. | Account No. | Account Name | Description | Debit | Credit | Dept. Name
```
Report juga menampilkan **total Debit & Credit** di bagian akhir.

## 7. Hubungan ke Account Balance & Laporan Keuangan

GL History = **detail transaction-level**. Akumulasi seluruh posting membentuk **Account Balance**, lalu
mengalir ke Laporan Keuangan **sesuai Account Type**:
- **Aset, Liabilitas, Ekuitas** → **Neraca**
- **Pendapatan, Beban** → **Laba-Rugi**

```
Transaksi/Voucher → Journal Posting → GL History → Account Balance → Financial Statement
```
> **Account Balance** = ringkasan saldo akun dari posting GL (bisa tampil **per periode**), lalu menjadi
> bagian Laporan Keuangan sesuai klasifikasi Account Type.

## 8. Tiga level yang harus dipisah (untuk accounting engine)

| Level | Isi |
|---|---|
| **A. Transaction level** | **voucher/transaksi sumber** yang dibuat user |
| **B. GL transaction level** | **journal posting** di GL History, bisa **drill-down** ke source |
| **C. Account Balance / FS level** | **akumulasi** posting → Neraca / Laba-Rugi **by Account Type** |

> **Jangan mencampur ketiganya:** GL History = **detail transaksi & audit trail**; Account Balance =
> **ringkasan saldo**; Neraca / Laba-Rugi = **laporan keuangan** berdasarkan klasifikasi akun.

> **Inti:** GL History = **kumpulan posting jurnal per akun** — *filterable*, *printable* (Print
> Preview), & *drillable* ke source. Ia **detail pembentuk Account Balance**, dan Account Balance →
> **Neraca / Laba-Rugi** sesuai Account Type. Lihat juga [Riwayat & Laporan AR](laporan-riwayat-akun-ar.md).
