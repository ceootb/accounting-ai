# Purchase Invoice — Verifikasi Dokumen & Kontrol Pembayaran

Ada satu batas yang sering kabur di praktik: **"boleh dicatat sebagai utang"** tidak sama dengan
**"boleh dibayar"**. Keduanya adalah **dua gerbang (gate) yang terpisah**. Mencampurnya membuat
pencatatan akuntansi salah — entah utang jadi telat diakui, atau kontrol pembayaran bocor.

## Dua gerbang yang berbeda

### 1. Gerbang Accounting — *boleh dicatat sebagai utang?*
Fokusnya **kebenaran pencatatan** utang dan **auto-journal**. Yang diverifikasi:
- **Supplier**, **nomor & tanggal invoice**, **item**, **qty**, **harga**, **pajak**, **akun**, dan
- **validasi Debit/Kredit** (jurnal harus balance).

Kalau semua ini benar, Purchase Invoice **sudah boleh diakui sebagai Utang Usaha (A/P)** — karena
kewajiban memang **sudah timbul** saat barang/jasa diterima (prinsip *accrual* & *matching*).

### 2. Gerbang Finance / AP — *boleh dibayar?*
Fokusnya **kelengkapan dokumen & approval** sebagai **syarat pembayaran**. Yang diverifikasi antara
lain: **PO**, **bukti penerimaan barang**, **invoice**, **dokumen pajak**, **approval**, dan
**payment terms**. Ini gerbang untuk **mencegah pembayaran yang tidak sah** (dobel bayar, tanpa PO,
tanpa barang diterima).

## Prinsip batasnya

- **Jangan mencampur kontrol pembayaran ke dalam logika jurnal akuntansi.** Jurnal mengikuti
  substansi ekonomi (utang sudah timbul), bukan status kelengkapan dokumen bayar.
- **Invoice yang sudah valid secara accounting tetap dicatat sebagai Utang Usaha**, walaupun dokumen
  pembayaran belum lengkap. Menunda pengakuan utang hanya karena dokumen bayar belum siap =
  **understated liabilities** (laporan salah saji).
- **Jika syarat pembayaran belum terpenuhi → statusnya *payment hold*, bukan pembatalan transaksi
  akuntansi.** Utang tetap tercatat; yang ditahan hanyalah **haknya untuk dibayar** sampai gerbang
  finance terpenuhi.

## Ringkasan

| Dimensi | Gerbang **Accounting** | Gerbang **Finance / AP** |
|---|---|---|
| Pertanyaan | Boleh **dicatat** sebagai utang? | Boleh **dibayar**? |
| Yang dicek | Supplier, invoice, tgl, item, qty, harga, pajak, akun, Dr/Cr balance | PO, bukti terima barang, invoice, dok pajak, approval, payment terms |
| Hasil | Diakui sebagai **Utang Usaha** (auto-journal) | **Boleh bayar** / **payment hold** |
| Kalau belum lengkap | Tetap **tercatat** sebagai utang | Pembayaran **ditahan**, transaksi accounting **tidak dibatalkan** |

> **Intinya:** akuntansi mencatat **kewajiban yang sudah timbul**; finance/AP mengontrol **kapan boleh
> dibayar**. Pisahkan keduanya — ini juga bentuk **pemisahan tugas (segregation of duties)**. Sistem
> akuntansi cukup mencatat utang & jurnalnya; alur approval pembayaran adalah **lapisan kontrol
> terpisah**, bukan perluasan logika jurnal.
