# Format 3 Laporan Keuangan Inti

> Ini **bentuk/format** tiga laporan keuangan utama — susunan baris demi baris. Semua angka di sini
> hanya **contoh ilustrasi**. Laporan **bukan** transaksi baru: ia hanya **menarik & merapikan saldo
> akhir akun dari Buku Besar**, jadi hanya bisa dicetak bila datanya sudah ada. Acuan susunan
> mengikuti **PSAK** (penyajian laporan keuangan) dan praktik laporan yang biasa dipublikasikan.
>
> Konsep & keterkaitan antar-laporan ada di [Bentuk Laporan Keuangan (Fondasi)](bentuk-laporan-keuangan.md).

---

## 1. Laporan Laba Rugi (L/R) — periode berjalan

Mengukur **kinerja** selama satu periode: pendapatan dikurangi beban = laba/rugi.

```
LAPORAN LABA RUGI
Untuk periode yang berakhir 31 Desember 20XX
─────────────────────────────────────────────
Pendapatan Penjualan                 1.000.000.000
(-) Retur & Potongan Penjualan          (20.000.000)
                                     ───────────────
Pendapatan Bersih                      980.000.000
(-) Beban Pokok Penjualan (HPP)       (600.000.000)
                                     ───────────────
LABA KOTOR                             380.000.000

Beban Operasional:
   Beban Penjualan                     (90.000.000)
   Beban Umum & Administrasi          (150.000.000)
                                     ───────────────
LABA USAHA                             140.000.000

Pendapatan / (Beban) Lain-lain:
   Pendapatan bunga                       5.000.000
   (Beban bunga)                         (8.000.000)
   Laba/(rugi) selisih kurs               2.000.000
                                     ───────────────
LABA SEBELUM PAJAK                     139.000.000
(-) Beban Pajak Penghasilan            (30.580.000)
                                     ═══════════════
LABA BERSIH                            108.420.000
```

---

## 2. Laporan Perubahan Modal (Ekuitas)

Menjelaskan **perubahan modal** dari awal ke akhir periode. **Laba bersih** dari L/R masuk ke sini.

**Bentuk perusahaan perorangan / CV:**
```
LAPORAN PERUBAHAN MODAL
Untuk periode yang berakhir 31 Desember 20XX
─────────────────────────────────────────────
Modal awal periode                     500.000.000
(+) Laba bersih periode                108.420.000
(-) Prive (pengambilan pemilik)        (30.000.000)
                                     ═══════════════
Modal akhir periode                    578.420.000
```

**Bentuk Perseroan Terbatas (PT):**
```
Modal Saham (disetor)                  400.000.000
Saldo Laba (Laba Ditahan) awal         100.000.000
(+) Laba bersih periode                108.420.000
(-) Dividen                             (30.000.000)
                                     ═══════════════
Total Ekuitas akhir                    578.420.000
```

---

## 3. Laporan Posisi Keuangan (Neraca)

Memotret **posisi keuangan** pada satu tanggal: apa yang **dimiliki** (Aset) = apa yang **menjadi
sumbernya** (Liabilitas + Ekuitas). **Modal akhir** dari laporan Perubahan Modal masuk ke sini.

```
LAPORAN POSISI KEUANGAN (NERACA)
Per 31 Desember 20XX
─────────────────────────────────────────────
ASET
 Aset Lancar:
   Kas & Bank                          150.000.000
   Piutang Usaha                        200.000.000
   Persediaan                           250.000.000
   Biaya Dibayar Dimuka                  20.000.000
                                     ───────────────
   Jumlah Aset Lancar                   620.000.000
 Aset Tidak Lancar:
   Aset Tetap                           500.000.000
   (Akumulasi Penyusutan)               (90.000.000)
                                     ───────────────
   Jumlah Aset Tidak Lancar             410.000.000
                                     ═══════════════
 TOTAL ASET                          1.030.000.000

LIABILITAS & EKUITAS
 Liabilitas Jangka Pendek:
   Utang Usaha                          280.000.000
   Utang Pajak                           31.580.000
   Utang Beban                           40.000.000
                                     ───────────────
   Jumlah Liabilitas Jk Pendek          351.580.000
 Liabilitas Jangka Panjang:
   Utang Bank Jangka Panjang            100.000.000
                                     ───────────────
 Jumlah Liabilitas                      451.580.000

 Ekuitas:
   Modal Saham / Modal disetor          400.000.000
   Saldo Laba (Laba Ditahan)            178.420.000
                                     ───────────────
   Jumlah Ekuitas                       578.420.000
                                     ═══════════════
 TOTAL LIABILITAS & EKUITAS          1.030.000.000
```

> **TOTAL ASET = TOTAL LIABILITAS & EKUITAS** (1.030.000.000 = 1.030.000.000). Bila tidak sama,
> ada pencatatan yang belum imbang.

---

## Bagaimana ketiganya tersambung

```
L/R  →  Laba Bersih  →  masuk ke Perubahan Modal
Perubahan Modal  →  Modal Akhir  →  masuk ke Neraca (Ekuitas)
Neraca  →  Aset = Liabilitas + Ekuitas (selalu imbang)
```

> **Urutan penyusunan:** buat **L/R** dulu (dapat laba bersih) → masukkan ke **Perubahan Modal**
> (dapat modal akhir) → masukkan ke **Neraca**. Ketiganya konsisten karena sama-sama menarik dari
> **saldo Buku Besar** yang dihasilkan auto-jurnal. Laporan hanya bisa terisi bila transaksi sudah
> diinput dan (untuk laporan akhir periode) proses tutup periode sudah dijalankan.
