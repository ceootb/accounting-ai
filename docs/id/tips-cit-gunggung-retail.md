# Tips: Cash in Transit (CIT) untuk Gunggung Penjualan Retail

> **Trik hemat waktu** untuk usaha dengan **transaksi retail sangat banyak & nilai kecil** (mis.
> café & resto). Daripada entry penjualan satu per satu tiap hari (buang waktu, dan nilainya tidak
> material per transaksi), penerimaan harian **ditampung** di akun **Cash in Transit (CIT)**, lalu
> **digunggung** (digabung) menjadi **satu Sales Invoice** di akhir bulan untuk pelaporan pajak.
>
> ⚠️ **Catatan jujur:** teknik CIT ini **murni tips cara kerja praktik untuk hemat waktu — bukan
> bagian dari teori akuntansi baku.** Tujuannya efisiensi entry, dengan tetap menjaga angka penjualan
> & PPN benar untuk fiskal.

---

## Setup akun & kontrolnya

- **Akun CIT didaftarkan di COA setara dengan Kas/Bank** (tipe akun *Kas/Bank*). Jadi ia menampung
  uang "yang sedang dalam perjalanan" dari penerimaan retail sebelum resmi jadi penjualan.
- **Kontrol wajib: setiap akhir bulan saldo CIT harus NOL (zero balance).** Kalau tidak nol, berarti
  ada penerimaan yang belum digunggung ke Sales Invoice, atau ada selisih dengan laporan POS — harus
  ditelusuri sebelum tutup buku. Saldo CIT = 0 di akhir bulan adalah **tanda semua penerimaan retail
  sudah dibukukan dengan benar**.

---

## Alurnya

**1. Harian — tampung penerimaan ke CIT (lewat Journal Voucher).**
Setiap hari, total penerimaan café/resto (gabungan semua transaksi hari itu) yang masuk ke bank
dicatat dengan JV:
```
Dr  Bank                         (total penerimaan hari itu)
    Cr  CIT - Cafe/Resto             (total penerimaan hari itu)
```
Contoh 1 hari: `Dr Bank 72.562 | Cr CIT - Cafe/Resto 72.562`. Diulang tiap hari, sehingga **CIT
menampung akumulasi penerimaan** yang belum dibukukan sebagai penjualan resmi.

**2. Akhir bulan — cek & bandingkan.**
Total penerimaan yang terkumpul di **rekap CIT** dicocokkan dengan **laporan penjualan dari sistem
operasional café** (POS). Jadi pemeriksaannya: *total penjualan versi ops café* vs *total penerimaan
di CIT* — harus sama/rekonsiliasi.

**3. Akhir bulan — gunggung jadi 1 Sales Invoice.**
Setelah cocok, seluruh transaksi sebulan dibuatkan **satu Sales Invoice** ke pelanggan umum
"CASH SALES", digabung (gunggung). Karena harga sudah termasuk PPN, cukup centang **Inclusive Tax** →
sistem memisahkan penjualan bersih & PPN Keluaran. SI inilah yang jadi dasar **laporan penjualan
versi fiskal** dan dilaporkan ke **Kantor Pajak**.

---

## Jurnal yang terbentuk (akhir bulan)

**Sales Invoice gunggung** (contoh Total Rp5.454.713 *incl* PPN, PPN Rp540.557):
```
Dr  Piutang Usaha                 5.454.713
    Cr  Penjualan (F&B)               4.914.156
    Cr  PPN Keluaran                    540.557
```
**Penerimaannya dibersihkan dari CIT** (Sales Receipt via akun CIT), sehingga saldo CIT yang tadi
menumpuk **kembali ke nol**:
```
Dr  CIT - Cafe/Resto              (total yang tadi ditampung)
    Cr  Piutang Usaha                (pelunasan SI gunggung)
```

> **Hasil akhir:** kas sudah masuk bank tiap hari (real), penjualan & PPN diakui **sekali** lewat SI
> gunggung di akhir bulan, dan akun **CIT nett = nol** (masuk harian → keluar saat digunggung).

---

## Kenapa pakai cara ini?

- **Hemat waktu:** entry SI per pelanggan retail tiap hari sangat memakan waktu; retail bervolume
  besar tapi **tidak material** per transaksi.
- **Tetap benar untuk pajak:** total penjualan & PPN akhirnya tetap terekam lewat SI gunggung.
- **Ada kontrol:** wajib **rekonsiliasi** rekap CIT vs laporan POS café sebelum digunggung.

> **Ingat:** ini **tips praktik**, bukan aturan akuntansi. Pastikan angka gunggung **cocok** dengan
> laporan operasional, dan PPN dihitung benar (klik *Inclusive Tax* bila harga sudah termasuk PPN).
