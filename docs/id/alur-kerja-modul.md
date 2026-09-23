# Alur Kerja Modul (Workflow)

Di praktik akuntansi, tiap modul punya **alur baku** dari awal transaksi sampai jurnal terbentuk.
Memahami alurnya membuat kita tahu **di langkah mana jurnal otomatis dibuat** dan bagaimana satu modul
mengalir ke Buku Besar lalu ke Laporan Keuangan. Diagram di bawah adalah **penyajian ulang generik**
dari alur yang umum dipakai (bukan tampilan software tertentu).

> **Cara baca:** kotak **bergaris tebal** = langkah tempat **jurnal otomatis terbentuk**. Langkah lain
> bersifat administratif (belum menjurnal) atau opsional.

---

## 1. Pembelian (Procure-to-Pay)

```mermaid
flowchart LR
  PR[Purchase Requisition<br/>permintaan pembelian] --> PO[Purchase Order<br/>pesanan ke vendor]
  PO --> RI[Receive Item<br/>terima barang]
  RI --> PI[Purchase Invoice<br/>faktur pembelian]
  PI --> PP[Purchase Payment<br/>bayar vendor]
  PI -. retur .-> PRet[Purchase Return<br/>retur pembelian]
  classDef jurnal stroke-width:3px,stroke:#1f6feb,fill:#eaf2ff;
  class PI,PP,PRet jurnal;
```

- **Requisition → Order → Receive Item** = tahap administratif (belum menjurnal).
- **Purchase Invoice** = titik **jurnal utama** (`Dr Persediaan/Beban | Cr Utang Usaha`).
- **Purchase Payment** = pelunasan (`Dr Utang Usaha | Cr Kas/Bank`).
- **Purchase Return** = kebalikan faktur (reversal). Detail: [Modul Pembelian](modul-purchase-kerangka.md).

---

## 2. Penjualan (Order-to-Cash)

```mermaid
flowchart LR
  SQ[Sales Quotation<br/>penawaran] --> SO[Sales Order<br/>pesanan pelanggan]
  SO --> DO[Delivery Order<br/>surat jalan/kirim]
  DO --> SI[Sales Invoice<br/>faktur penjualan]
  SI --> SR[Sales Receipt<br/>terima pembayaran]
  SI -. retur .-> SRet[Sales Return<br/>retur penjualan]
  classDef jurnal stroke-width:3px,stroke:#1f6feb,fill:#eaf2ff;
  class SI,SR,SRet jurnal;
```

- **Quotation → Order → Delivery Order** = tahap administratif (belum menjurnal).
- **Sales Invoice** = titik **jurnal utama** (`Dr Piutang | Cr Pendapatan + PPN` **dan** `Dr HPP | Cr
  Persediaan`).
- **Sales Receipt** = penerimaan (`Dr Kas/Bank | Cr Piutang`); di sinilah **potongan pajak** dicatat
  bila pelanggan memotong PPh. Detail: [Modul Penjualan](modul-sales-kerangka.md).
- **Sales Return** = kebalikan faktur (reversal).

---

## 3. Kas & Bank

```mermaid
flowchart LR
  BB[Bank Book<br/>buku kas/bank] --> DEP[Deposit<br/>setoran masuk]
  BB --> PAY[Payment<br/>pembayaran keluar]
  DEP --> REC[Bank Reconcile<br/>rekonsiliasi bank]
  PAY --> REC
  classDef jurnal stroke-width:3px,stroke:#1f6feb,fill:#eaf2ff;
  class DEP,PAY jurnal;
```

- **Deposit / Payment** = mutasi kas-bank yang menjurnal (masuk/keluar) di luar siklus AR/AP, mis.
  biaya bank, setoran modal, transfer antar-kas.
- **Bank Reconcile** = mencocokkan buku dengan rekening koran bank — bukan menjurnal, tapi **kontrol**
  agar saldo buku = saldo bank.

---

## 4. Buku Besar sampai Laporan Keuangan

```mermaid
flowchart LR
  subgraph Setup [Data acuan]
    COA[Chart of Account] 
    CI[Company Info]
    CUR[Currency]
  end
  Setup --> TRX[Transaksi modul<br/>Pembelian/Penjualan/Kas]
  TRX --> GL[(Buku Besar<br/>General Ledger)]
  JV[Journal Voucher<br/>jurnal manual/adjustment] --> GL
  GL --> PE[Period End<br/>tutup periode]
  PE --> FS[Financial Statement<br/>Laporan Keuangan]
  classDef jurnal stroke-width:3px,stroke:#1f6feb,fill:#eaf2ff;
  class JV,PE jurnal;
```

- **COA, Company Info, Currency** = data acuan (setup) yang dipakai semua transaksi.
- Semua **transaksi modul** otomatis mengalir ke **Buku Besar**.
- **Journal Voucher** = jurnal **manual** untuk penyesuaian/koreksi yang tak lewat modul (amortisasi,
  reklas, dll). Detail: [Modul General Ledger — JV](modul-general-ledger-jv.md).
- **Period End** = tutup periode; menjalankan auto-jurnal penutup (mis. penyusutan, selisih kurs).
  Detail: [Proses Tutup Periode](proses-tutup-periode-period-end.md).
- **Financial Statement** = hasil akhir — tarikan saldo Buku Besar menjadi Neraca, Laba-Rugi, dll.

> **Benang merahnya:** setup benar → transaksi menjurnal otomatis di titik yang tepat → Buku Besar →
> Period End → Laporan Keuangan. Siklus yang sama berulang tiap periode.
