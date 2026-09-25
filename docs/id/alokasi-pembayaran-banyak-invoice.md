# Alokasi Satu Pembayaran/Penerimaan ke Beberapa Invoice (1-to-many)

Hubungan antara **pembayaran** dan **invoice** tidak selalu satu lawan satu. Selain satu invoice yang
bisa dibayar **bertahap** (banyak pembayaran → 1 invoice), sebuah transaksi kas/bank juga bisa
**melunasi beberapa invoice sekaligus** (1 pembayaran → banyak invoice). Halaman ini membahas arah yang
kedua.

## Purchase Payment → beberapa Purchase Invoice

- Satu transaksi **Purchase Payment** dapat membayar **beberapa Purchase Invoice** dari **vendor yang
  sama**.
- User memilih beberapa Purchase Invoice yang masih **owing** (bersaldo terutang), lalu
  **mengalokasikan** nilai pembayaran ke masing-masing invoice.
- **Total alokasi tidak boleh melebihi** nilai Purchase Payment.
- Sistem **mencatat alokasi** ke tiap invoice; **status tiap invoice diperbarui** — bisa jadi **lunas**
  atau **dibayar sebagian**.
- Purchase Payment tetap **satu transaksi**, walau dialokasikan ke beberapa invoice.

## Sales Receipt → beberapa Sales Invoice

Cerminannya di sisi penerimaan:
- Satu **Sales Receipt** dapat menerima pembayaran atas **beberapa Sales Invoice** dari **customer yang
  sama**.
- User memilih beberapa Sales Invoice yang masih owing, lalu **mengalokasikan** nilai penerimaan ke
  masing-masing.
- **Total alokasi ≤ nilai Sales Receipt**; status tiap invoice jadi **lunas** atau **diterima
  sebagian**; Sales Receipt tetap **satu transaksi**.

## Konsep akuntansi penting

- Relasinya **1-to-many**: **1 Purchase Payment → beberapa Purchase Invoice**; **1 Sales Receipt →
  beberapa Sales Invoice**.
- Sistem **tidak boleh memaksa** user membuat satu transaksi pembayaran/penerimaan **per invoice**
  apabila satu transaksi bank/kas memang dipakai untuk melunasi beberapa invoice sekaligus.
- **Detail alokasi harus dapat ditelusuri** — user bisa tahu invoice mana saja yang dibayar/diterima
  lewat suatu Purchase Payment atau Sales Receipt tertentu.

## Bentuk jurnal (konsep)

Satu Purchase Payment **Rp100jt** untuk 3 Purchase Invoice (alokasi Rp40jt + Rp35jt + Rp25jt):
```
Dr  Utang Usaha                  100.000.000   (teralokasi: PI-A 40jt, PI-B 35jt, PI-C 25jt)
    Cr  Kas/Bank                  100.000.000
```
> Satu kredit kas/bank; **Utang Usaha berkurang per invoice** sesuai alokasinya. Sisi Sales tinggal
> dibalik: `Dr Kas/Bank | Cr Piutang Usaha`, teralokasi ke beberapa Sales Invoice.

## Hubungan dengan pembayaran bertahap

Digabung dengan konsep **[pembayaran bertahap (Owing)](sales-invoice-pembayaran-bertahap.md)** —
banyak pembayaran → 1 invoice — maka relasi pembayaran↔invoice sebetulnya **banyak ke banyak**. Yang
menjadi acuan tetap **Owing tiap invoice** (nilai invoice − yang sudah dialokasikan), sampai nol.

> **Intinya:** satu transaksi bank bisa **dialokasikan ke beberapa invoice**; tiap invoice diperbarui
> statusnya (lunas / sebagian), dan **alokasinya tetap tertelusur** — tanpa memaksa satu pembayaran per
> invoice.
