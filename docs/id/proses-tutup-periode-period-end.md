# Proses Tutup Periode (Period End)

> **Period End** adalah proses yang dijalankan **saat menutup buku tiap bulan/periode**. Sistem
> otomatis **membuat jurnal-jurnal penutup rutin** — terutama **penyusutan aset** dan
> **penyesuaian selisih kurs** — sehingga user tidak menghitung manual.

---

## Di mana & bagaimana menjalankannya

Menu: **Activities → Periodic → Period End**. Lalu:
1. Pilih **Period** (bulan) dan **Year** (tahun) yang mau ditutup. Sistem menampilkan **Last Period
   End** (periode terakhir yang sudah ditutup) supaya urut, tidak melompat.
2. Isi **kurs penutup (Exchange Rate)** untuk tiap mata uang asing (mis. USD, AUD, EUR); IDR = 1.
3. Klik **OK** → sistem otomatis membuat **Journal Voucher penutup**.

> Hasilnya muncul sebagai Journal Voucher bertipe **Period End** dan **Depreciation Asset**
> (mis. "Period End Process for Jun 2026") — bisa dilihat & diverifikasi di daftar Journal Voucher.

---

## Apa yang di-auto-jurnal oleh Period End

**1. Penyusutan aset tetap (Depreciation Asset).**
Sistem menghitung penyusutan **semua aset sekaligus** untuk periode itu, dirinci per aset & per
departemen:
```
Dr  Beban Penyusutan (per kategori aset)
    Cr  Akumulasi Penyusutan (per kategori aset)
```
*(Ini penyusutan bulanan dari [Modul Aset Tetap](modul-fixed-asset.md) — tidak perlu JV manual.)*

**2. Penyesuaian selisih kurs (revaluasi mata uang asing).**
Saldo akun yang dalam **mata uang asing** (kas, bank, piutang, utang dalam USD/AUD/EUR) **dinilai
ulang ke kurs penutup** yang tadi diinput. Selisihnya dicatat sebagai **keuntungan/kerugian kurs**:
- **Realized** (sudah terealisasi) dan **Unrealized** (belum terealisasi) — masuk ke akun
  *Gain/Loss* yang sudah dipetakan di **Preferences → Currency Default Account**.

Contoh sederhana: perusahaan punya kas **USD 1.000**. Nilai lama dicatat pada kurs Rp15.000
(= Rp15.000.000). Kurs penutup akhir bulan Rp15.200 (= Rp15.200.000). Sistem **menilai ulang** akun
kas itu: mencatat nilai baru di sisi debit dan mengeluarkan nilai lama di sisi kredit, lalu selisihnya
ke akun laba/rugi kurs:
```
Dr  Kas USD (1.000 × 15.200)          15.200.000
    Cr  Kas USD (1.000 × 15.000)          15.000.000
    Cr  Laba Selisih Kurs (Unrealized)      200.000
```
> Karena kurs **naik**, hasilnya **keuntungan** (Cr Laba Selisih Kurs). Bila kurs **turun**, polanya
> terbalik dan selisih dicatat sebagai **Rugi Selisih Kurs (Dr)**. Untuk saldo yang masih ada di
> perusahaan, selisihnya **Unrealized** (belum terealisasi).

*(Tipe proses lain yang bisa muncul: Roll Over Goods dan Project Expense Payment — sesuai modul yang
dipakai perusahaan.)*

---

## Kapan Period End dijalankan (kaitan dengan tutup buku)

Period End dijalankan **setelah**:
1. **Semua transaksi periode berjalan sudah terinput lengkap**, dan
2. **Rekonsiliasi bank & kas sudah nol** (lihat [Tips: syarat closing FS](tips-cari-selisih.md#syarat-utama-sebelum-tutup-buku-closing-fs)).

Barulah Period End dijalankan untuk membukukan penyusutan & selisih kurs, sehingga **Laporan Keuangan
periode itu siap ditutup** dan periode berikutnya bisa dibuka.

---

## Intinya

> **Period End = satu tombol untuk membukukan penyusutan & selisih kurs saat tutup bulan.** Sistem
> yang menghitung dan menjurnal semuanya (dirinci per aset/mata uang), lalu hasilnya bisa diperiksa
> sebagai Journal Voucher. User cukup memastikan transaksi lengkap & kas/bank sudah balance sebelum
> menjalankannya.
