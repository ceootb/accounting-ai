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

---

## Pembayaran Bertahap / Cicilan (Partial / Installment Payment)

**Satu Purchase Invoice dapat dibayar lebih dari satu kali** sesuai SLA / *payment terms* yang
disepakati dengan supplier. Yang penting: **jangan membuat Purchase Invoice baru untuk setiap
pembayaran.** Purchase Invoice tetap menjadi **sumber utangnya**; setiap *payment entry* hanya
**mengurangi saldo Utang Usaha dari invoice yang sama** sampai *outstanding* menjadi nol.

**Contoh** — Purchase Invoice **Rp100 juta**, dibayar 3 tahap:

| Langkah | Jurnal | Sisa Utang (*outstanding*) |
|---|---|---|
| Purchase Invoice | `Dr Persediaan/Beban 100jt \| Cr Utang Usaha 100jt` | 100jt |
| Payment 1 (Rp30jt) | `Dr Utang Usaha 30jt \| Cr Kas/Bank 30jt` | 70jt |
| Payment 2 (Rp40jt) | `Dr Utang Usaha 40jt \| Cr Kas/Bank 40jt` | 30jt |
| Payment 3 (Rp30jt) | `Dr Utang Usaha 30jt \| Cr Kas/Bank 30jt` | **0** |

- **Utang Usaha untuk invoice itu berkurang tiap pembayaran**; pokok utang tidak dicatat ulang.
- Sistem dapat menampilkan **total invoice, total sudah dibayar, dan outstanding balance** — biasanya
  di kolom **owing** pada Purchase Invoice. Kolom *owing* inilah "sisa yang masih terutang".
- Selama *owing* belum nol, invoice berstatus **belum lunas** (sebagian terbayar).

> **Paralel di sisi Piutang (AR):** konsep yang sama berlaku terbalik — satu **Sales Invoice** bisa
> diterima pembayarannya bertahap; tiap **Sales Receipt** mengurangi **Piutang Usaha** dari invoice
> yang sama sampai *outstanding*-nya nol. Tidak membuat Sales Invoice baru per penerimaan. Detail:
> [Sales Invoice — Pembayaran Bertahap (Owing)](sales-invoice-pembayaran-bertahap.md).
