# Tips: Cash Clearing Account (CCA) untuk Gunggung Penjualan Retail

> **Trik hemat waktu** untuk usaha dengan **transaksi retail sangat banyak & nilai kecil** (mis.
> café & resto). Daripada entry penjualan satu per satu tiap hari (buang waktu, dan nilainya tidak
> material per transaksi), penerimaan harian **ditampung** di **akun perantara / Cash Clearing
> Account (CCA)**, lalu **digunggung** (digabung) menjadi **satu Sales Invoice** di akhir bulan untuk
> pelaporan pajak.
>
> ⚠️ **Catatan jujur:** teknik ini **murni tips cara kerja praktik untuk hemat waktu — bukan bagian
> dari teori akuntansi baku.** Tujuannya efisiensi entry, dengan tetap menjaga angka penjualan & PPN
> benar untuk fiskal.

---

## Catatan istilah: kenapa "CCA", bukan "CIT"?

Di beberapa software akun ini sering dilabeli **CIT (Cash in Transit)**, tetapi itu **kurang tepat**.
Makna baku **Cash in Transit** = **kas sudah diterima tapi belum disetor ke bank** (mis. terima tunai
malam hari saat bank tutup). Pada kasus retail ini, **uang sudah masuk ke bank** — jadi bukan "in
transit".

Yang lebih tepat adalah **akun perantara jenis _clearing account_**: akun sementara yang sengaja
dipakai untuk **menjembatani dua pencatatan** dan **wajib nol** setelah tuntas. Kami memakai istilah
**Cash Clearing Account (CCA)**.

| Istilah | Makna | Cocok di sini? |
|---|---|---|
| **Clearing account (CCA)** | Akun penjembatan sementara, sengaja di-nol-kan | ✅ Ya |
| **Suspense account** | Penampung saat **klasifikasi belum jelas** mau ke mana | ❌ (di sini klasifikasi jelas: penjualan retail) |
| **Sundry account** | Pos "rupa-rupa / lain-lain" | ❌ (bukan akun penjembatan) |

> **Soal PSAK:** PSAK **tidak mengatur penamaan akun internal** seperti ini — itu kebijakan akun
> internal perusahaan. Yang diatur PSAK adalah **pengakuan pendapatan** (PSAK 72) & **penyajian
> laporan** (PSAK 1 / PSAK 201). Syaratnya: akun CCA **temporary & nol di akhir periode**, dan
> pendapatan **tetap diakui di periode yang benar**.

---

## Setup akun & kontrolnya

- **Akun CCA didaftarkan di COA sebagai tipe Kas/Bank.** Alasan praktis: agar bisa dipilih sebagai
  "bank penerima" saat Sales Receipt. Presentasinya aman karena akhir bulan saldonya nol.
- **Boleh lebih dari satu CCA — dipisah per jenis retail** untuk kontrol per aliran penjualan. Contoh
  penamaan konsisten:
  - `CCA - Cafe`
  - `CCA - Merchandise`
  - `CCA - Food`
  Tiap CCA direkonsiliasi dengan laporan POS aliran masing-masing, jadi kalau ada selisih langsung
  ketahuan di stream mana.
- **Kontrol wajib: tiap akhir bulan saldo tiap CCA harus NOL (zero balance).** Kalau tidak nol,
  berarti ada penerimaan yang belum digunggung ke Sales Invoice atau ada selisih dengan laporan POS —
  harus ditelusuri sebelum tutup buku.

---

## Alurnya

**1. Harian — tampung penerimaan ke CCA (lewat Journal Voucher).**
Setiap hari, total penerimaan café/resto (gabungan semua transaksi hari itu) yang masuk ke bank
dicatat dengan JV:
```
Dr  Bank                         (total penerimaan hari itu)
    Cr  CCA - Cafe                   (total penerimaan hari itu)
```
Contoh 1 hari: `Dr Bank 72.562 | Cr CCA - Cafe 72.562`. Diulang tiap hari, sehingga **CCA menampung
akumulasi penerimaan** yang belum dibukukan sebagai penjualan resmi.

**2. Akhir bulan — cek & bandingkan.**
Total di **rekap CCA** dicocokkan dengan **laporan penjualan dari sistem operasional café** (POS):
*total penjualan versi ops café* vs *total penerimaan di CCA* — harus sama.

**3. Akhir bulan — gunggung jadi 1 Sales Invoice.**
Setelah cocok, seluruh transaksi sebulan dibuatkan **satu Sales Invoice** ke pelanggan umum
"CASH SALES", digabung. Karena harga sudah termasuk PPN, cukup centang **Inclusive Tax** → sistem
memisahkan penjualan bersih & PPN Keluaran. SI inilah dasar **laporan penjualan versi fiskal** yang
dilaporkan ke **Kantor Pajak**.

---

## Jurnal yang terbentuk (akhir bulan)

**Sales Invoice gunggung** (contoh Total Rp5.454.713 *incl* PPN, PPN Rp540.557):
```
Dr  Piutang Usaha                 5.454.713
    Cr  Penjualan (F&B)               4.914.156
    Cr  PPN Keluaran                    540.557
```
**Penerimaannya dibersihkan dari CCA** (Sales Receipt via akun CCA), sehingga saldo CCA yang tadi
menumpuk **kembali ke nol**:
```
Dr  CCA - Cafe                    (total yang tadi ditampung)
    Cr  Piutang Usaha                (pelunasan SI gunggung)
```

> **Hasil akhir:** kas sudah masuk bank tiap hari (real), penjualan & PPN diakui **sekali** lewat SI
> gunggung di akhir bulan, dan akun **CCA nett = nol** (masuk harian → keluar saat digunggung).

---

## Kenapa pakai cara ini?

- **Hemat waktu:** entry SI per pelanggan retail tiap hari sangat memakan waktu; retail bervolume
  besar tapi **tidak material** per transaksi.
- **Tetap benar untuk pajak:** total penjualan & PPN akhirnya tetap terekam lewat SI gunggung.
- **Ada kontrol:** wajib **rekonsiliasi** rekap CCA vs laporan POS café, dan **saldo CCA nol** tiap
  akhir bulan.

> **Ingat:** ini **tips praktik**, bukan aturan akuntansi. Pastikan angka gunggung **cocok** dengan
> laporan operasional, PPN dihitung benar (*Inclusive Tax* bila harga sudah termasuk PPN), dan tiap
> CCA **nol** di akhir bulan.
