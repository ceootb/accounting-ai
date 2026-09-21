# Riwayat Transaksi per Akun & Laporan Piutang (AR / Customer)

Setelah transaksi dicatat, dua hal yang paling sering dibutuhkan adalah: **melihat kembali riwayat
transaksi tiap akun**, dan **menarik laporan** (khususnya piutang/AR). Halaman ini menjelaskan
keduanya beserta konsep **Sub Ledger** yang membuat kontrol piutang/utang jadi rapi.

## 1. Account History — rekap transaksi per akun

Setiap akun di COA punya **Account History**: daftar semua transaksi yang pernah menyentuh akun
tersebut. Bentuknya **tabel (data grid) yang bisa disaring** — misalnya berdasarkan tanggal — dengan
kolom informasi dan panel filter di sisinya.

Gunanya: kalau ingin melihat **rekap transaksi untuk satu akun tertentu**, di sinilah tempatnya —
tidak perlu membuka voucher satu per satu. Tampilan ini **berlaku sama untuk semua akun COA**, dan
bisa menampilkan rincian **Sub Ledger** (lihat bagian 4).

## 2. Dari riwayat ke laporan

Dari riwayat buku besar, sistem mengarahkan ke kumpulan **laporan** yang tersusun dua tingkat:
**Report Category** (kelompok laporan) dan **Report Detail** (laporan spesifik di dalamnya). Jadi tiap
kelompok transaksi punya laporannya sendiri, siap dibuka per kategori dan per detail.

## 3. Laporan Piutang (AR) & Customer yang sering dipakai

- **Outstanding Invoices** — daftar **faktur penjualan (Sales Invoice) yang masih belum lunas
  (*unpaid*) saja**. Isinya sisa tagihan per faktur — cepat untuk melihat siapa yang belum bayar.
- **Aging Receivable Summary** — ringkasan **umur piutang** per pelanggan (dikelompokkan berdasar
  lama menunggak), tampil ringkas.
- **Aging Receivable Detail** — rincian umur piutang yang sama, sampai ke tiap transaksinya.
- **AR Sub Ledger Detail** — rekap **pergerakan piutang lengkap per pelanggan**, yaitu:

  > **Saldo awal (open balance) + Sales Invoice − Sales Receipt − Sales Return − Down Payment
  > + Journal Voucher = Saldo akhir (Balance).**

  Bedanya dengan *Outstanding Invoices*: Sub Ledger Detail menampilkan **seluruh** mutasi yang
  membentuk saldo piutang, sedangkan Outstanding Invoices **hanya faktur yang belum dibayar**.

Semua laporan ini bisa **diekspor ke PDF atau Excel**. Dari tampilan laporan, sebuah baris bisa
**ditelusuri ke sumbernya** — dari ringkasan turun ke detail, lalu ke voucher aslinya (misalnya baris
yang berasal dari Sales Invoice akan membuka detail Sales Invoice tersebut).

## 4. Sub Ledger (Sub GL) pada AR & AP — kenapa penting

**Sub Ledger** adalah **buku pembantu per pelanggan / pemasok** di bawah satu akun kontrol. Manfaatnya
besar: cukup punya **satu akun Piutang Usaha (AR)** dan **satu akun Utang Usaha (AP)**, sementara
rincian tagihan per pihak dipegang oleh Sub Ledger-nya.

Tanpa Sub Ledger, orang tergoda membuat banyak akun terpisah — *AR Toko ABC*, *AR Toko XYZ*, dan
seterusnya — yang membuat COA membengkak. Dengan Sub Ledger, **cukup 1 akun AR**, tetapi kontrol per
pelanggan tetap detail. Konsep yang sama berlaku di sisi **AP (per pemasok)**.

> **Intinya:** satu akun kontrol + Sub Ledger yang detail = COA tetap ramping, kontrol tagihan per
> pihak tetap jelas.
