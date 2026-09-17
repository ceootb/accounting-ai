# Tips Cepat Mencari Selisih (Rekonsiliasi & Jurnal) — Bahasa Sederhana

> Trik praktik akuntan untuk **menebak penyebab selisih** dengan cepat, tanpa harus mengecek semua
> transaksi satu per satu. Berguna saat **rekonsiliasi bank** atau saat angka tidak cocok.
> Ditulis untuk pengguna umum. *(Dikurasi akuntan praktik.)*

---

## Trik 1: Selisih habis dibagi 9 → kemungkinan **angka terbalik** (transposisi)

Kalau ada selisih dan angkanya **habis dibagi 9 (tidak bersisa)**, kemungkinan besar bukan ada
transaksi yang hilang — tapi ada **digit yang tertukar posisinya** saat menulis angka.

**Contoh:**
- Seharusnya `24.000`, tertulis `42.000` → selisih **18.000**. 18.000 ÷ 9 = 2.000 → habis dibagi 9. ✓
- Angka 2 dan 4 hanya **tertukar tempatnya**.

**Cara pakai:** begitu ketemu selisih, **bagi 9 dulu**. Kalau pas, jangan buang waktu mencari
transaksi yang hilang — cari angka yang **penulisannya kebalik** (mis. 1.360 vs 1.630, selisih 270,
juga habis dibagi 9).

**Bonus:** hasil bagi menunjukkan **beda antar digit yang tertukar**. Contoh 18.000 ÷ 9 = 2.000 →
digit yang tertukar bedanya 2 (yaitu 4 − 2). Jadi tinggal cari pasangan angka yang cocok.

---

## Trik 2: Selisih tepat **2 kali lipat** → kemungkinan **salah sisi debit/kredit**

Kalau selisihnya **persis dua kali** nilai suatu transaksi, kemungkinan angka **tercatat di sisi
yang salah** — harusnya di **debit**, malah masuk **kredit** (atau sebaliknya).

Kenapa jadi dua kali? Karena angka itu bukan cuma "hilang" dari sisi yang benar, tapi juga
"menambah" di sisi yang salah — efeknya dobel.

**Catatan penting dari praktik:** di **satu jurnal voucher**, hal ini biasanya **ketahuan langsung**
karena sistem **menolak menyimpan** voucher yang tidak seimbang (total debit ≠ total kredit). Jadi
salah sisi paling sering "lolos" bukan di dalam satu voucher, melainkan saat **membandingkan dengan
catatan lain** (mis. saldo buku vs rekening koran bank).

**Cara pakai:** kalau selisih genap, coba **bagi 2**. Kalau hasilnya sama dengan nilai sebuah
transaksi yang kamu kenal, periksa transaksi itu — mungkin debit dan kreditnya tertukar.

---

## Ringkasan cepat

| Selisih... | Kemungkinan penyebab | Langkah |
|---|---|---|
| **Habis dibagi 9** | Angka terbalik (digit tertukar) | Cari angka yang penulisannya kebalik |
| **Tepat 2× nilai transaksi** | Salah sisi debit/kredit | Bagi 2, cek transaksi yang nilainya sama |

> **Inti:** sebelum mengecek satu per satu, **lihat pola angka selisihnya dulu**. Habis dibagi 9 →
> angka terbalik. Dua kali lipat → salah sisi debit/kredit. Trik kecil ini menghemat banyak waktu
> saat rekonsiliasi.
