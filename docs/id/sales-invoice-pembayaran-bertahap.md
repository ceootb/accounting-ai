# Sales Invoice — Pembayaran Bertahap / Cicilan (Owing)

**Satu Sales Invoice dapat menerima lebih dari satu kali pembayaran** melalui beberapa **Sales
Receipt**, sesuai *payment terms* / SLA dengan pelanggan. Semua Sales Receipt itu **tetap mengacu ke
Sales Invoice yang sama** — **jangan membuat Sales Invoice baru untuk setiap pembayaran.** Sales
Invoice tetap menjadi **sumber piutangnya**; tiap Sales Receipt hanya **mengurangi saldo Piutang
Usaha** dari invoice yang sama sampai *outstanding* menjadi nol.

**Contoh** — Sales Invoice **Rp100 juta**, diterima 3 tahap:

| Langkah | Jurnal | Sisa Piutang (*Owing*) |
|---|---|---|
| Sales Invoice | `Dr Piutang Usaha 100jt \| Cr Pendapatan (+PPN) 100jt` | 100jt |
| Sales Receipt 1 (Rp30jt) | `Dr Kas/Bank 30jt \| Cr Piutang Usaha 30jt` | 70jt |
| Sales Receipt 2 (Rp40jt) | `Dr Kas/Bank 40jt \| Cr Piutang Usaha 40jt` | 30jt |
| Sales Receipt 3 (Rp30jt) | `Dr Kas/Bank 30jt \| Cr Piutang Usaha 30jt` | **0** |

## Monitor lewat kolom Owing

> **Owing = nilai Sales Invoice − total Sales Receipt yang sudah diterima.**

- **Owing = 0** → invoice **sudah lunas**.
- **Owing > 0** → masih ada **piutang yang belum diterima** (invoice sebagian terbayar).

Piutang untuk invoice itu **berkurang tiap penerimaan**; pokok piutang **tidak dicatat ulang** dan
tidak ada Sales Invoice baru.

## Konsisten dengan sisi Utang (AP)

Konsep ini adalah **cerminan** dari sisi pembelian. Lihat
[Purchase Invoice — Pembayaran Bertahap](purchase-invoice-verifikasi-vs-pembayaran.md#pembayaran-bertahap--cicilan-partial--installment-payment):

| | **Sales Invoice (AR)** | **Purchase Invoice (AP)** |
|---|---|---|
| Sumber | 1 Sales Invoice | 1 Purchase Invoice |
| Entry pembayaran | banyak **Sales Receipt** | banyak **Payment** |
| Yang berkurang | **Piutang Usaha** | **Utang Usaha** |
| Kolom pemantau | **Owing** (piutang tersisa) | **Owing** (utang tersisa) |
| Aturan | 1 invoice, banyak pembayaran; **bukan** invoice baru per bayar | sama |

> **Intinya:** satu invoice = satu sumber piutang/utang; pembayaran bertahap **mengurangi
> outstanding**-nya, dipantau lewat **Owing**, sampai nol (lunas).
