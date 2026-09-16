# Struktur COA: Tipe Akun, Parent & Child Account

> Cara menata Bagan Akun (COA) yang benar: setiap akun punya **Tipe Akun**, dan bisa berupa
> **parent** (induk) atau **child** (rincian / *sub-account of*). Tipe akun menentukan **saldo normal**
> & **laporan tujuan** — lihat [bentuk-laporan-keuangan.md](bentuk-laporan-keuangan.md).

---

## 1. Tipe Akun (Account Type) — 16 tipe standar

Setiap akun **wajib** diberi satu tipe. Tipe menentukan saldo normal (Debit/Kredit) dan di laporan
mana akun muncul (Neraca / Laba Rugi).

| Tipe (Indonesia) | Account Type (EN) | Saldo Normal | Laporan |
|---|---|---|---|
| Kas/Bank | Cash/Bank | Debit | Neraca |
| Piutang Usaha | Account Receivable | Debit | Neraca |
| Persediaan | Inventory | Debit | Neraca |
| Aset Lancar Lainnya | Other Current Asset | Debit | Neraca |
| Aset Tetap | Fixed Asset | Debit | Neraca |
| Akumulasi Penyusutan | Accumulated Depreciation | Kredit | Neraca (kontra-aset) |
| Aset Lainnya | Other Asset | Debit | Neraca |
| Utang Usaha | Account Payable | Kredit | Neraca |
| Utang Lancar Lainnya | Other Current Liability | Kredit | Neraca |
| Utang Jangka Panjang | Long Term Liability | Kredit | Neraca |
| Ekuitas | Equity | Kredit | Neraca / Perubahan Modal |
| Pendapatan | Revenue | Kredit | Laba Rugi |
| Beban Pokok Penjualan (HPP) | Cost of Goods Sold | Debit | Laba Rugi |
| Beban | Expense | Debit | Laba Rugi |
| Beban Lain-lain | Other Expense | Debit | Laba Rugi |
| Pendapatan Lain-lain | Other Income | Kredit | Laba Rugi |

---

## 2. Parent Account vs Child Account

- **Parent account** = akun induk/header (mis. **Cash/Bank**).
- **Child account** = rincian di bawah parent, ditandai **"Sub Account of"** parent tersebut.
- **Child mewarisi tipe** dari parent-nya; **saldo parent = jumlah semua child**-nya.
- **Transaksi diposting ke child** (akun paling rinci); parent dipakai untuk **ringkasan di laporan**.

**Contoh:**
```
Cash/Bank                      (PARENT — tipe Kas/Bank)
 ├─ Kas Besar                  (child / sub-account of Cash/Bank)
 ├─ Kas Kecil                  (child)
 ├─ Bank BCA                   (child)
 ├─ Bank CIMB                  (child)
 └─ Bank Mega                  (child)
```
Begitu pula akun lain yang perlu rincian.

---

## 3. Contoh COA berjenjang (perusahaan properti / dagang — ilustrasi)

```
Piutang Usaha                  (PARENT — Account Receivable)
 ├─ Piutang Dagang
 ├─ Piutang KPR / Bank
 └─ Piutang Retensi

Persediaan                     (PARENT — Inventory)
 ├─ Persediaan Barang
 ├─ Barang Dalam Proses (WIP)
 └─ Unit Jadi

Utang Usaha                    (PARENT — Account Payable)
 ├─ Utang Dagang
 └─ Utang Biaya

Beban                          (PARENT — Expense)
 ├─ Beban Gaji
 ├─ Beban Listrik & Air
 ├─ Beban Sewa
 └─ Beban Pemeliharaan
```
*(Ini pola yang sama dipakai saat menyusun draft COA awal sebuah perusahaan properti sebelum
klien mengirim versi final mereka — parent sebagai kerangka, child sesuai kebutuhan riil.)*

---

## 4. Kenapa struktur ini penting

- **Laporan rapi & bertingkat:** parent untuk ringkasan, child untuk detail.
- **Auto-jurnal & mapping tepat:** transaksi diarahkan ke child yang benar; sistem tahu tipe & saldo
  normalnya, sehingga jurnal otomatis mendarat di laporan yang tepat.
- **Konsistensi:** tipe akun menjaga saldo normal & klasifikasi laporan tetap benar untuk semua akun.
