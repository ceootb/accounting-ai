# Menyiapkan Data Setup Sebelum Transaksi — Penjelasan Sederhana

> Ditulis dengan bahasa sehari-hari untuk **pengguna yang tidak harus mahir akuntansi**. Intinya:
> **semua data dasar disiapkan lebih dulu**, supaya begitu transaksi diinput, sistem langsung tahu
> harus mencatat ke mana — dan laporan keuangan terbentuk sendiri.
>
> *(Daftar field lengkap yang lebih teknis ada di [modul-setup-persiapan.md](modul-setup-persiapan.md),
> dipakai saat membangun software.)*

---

## Kenapa harus disiapkan dulu?

Bayangkan **memasak di dapur**. Sebelum mulai masak, bahan, bumbu, dan resep harus sudah tersedia
dan tertata. Kalau garam ada di tempatnya dan resep sudah jelas, memasak jadi cepat dan hasilnya
konsisten. Begitu juga akuntansi: kalau **data setup sudah rapi di depan**, maka saat transaksi
masuk, sistem tidak bingung — ia langsung tahu harus mencatat ke akun mana, dan laporan di ujung
belakang jadi otomatis dan benar.

Ada **3 hal yang disiapkan** sebelum transaksi pertama:

```
1. Company Info   → identitas & periode perusahaan
2. Preferences    → aturan main + "peta akun" (kunci auto-jurnal)
3. User Profile   → siapa boleh melakukan apa (keamanan)
```

---

## 1. Company Info — mengisi jati diri perusahaan

Ini seperti mengisi **KTP perusahaan**. Yang diisi:

- **Identitas:** nama, alamat, telepon, dan **mata uang** utama (mis. Rupiah).
- **Periode pembukuan:** kapan tahun buku mulai, dan **periode berjalan** saat ini.
- **Data pajak:** NPWP, status PKP, dan kode terkait pajak.

Bagian periode ini penting sebagai **pengaman**: sistem bisa memberi **peringatan** atau bahkan
**menolak** bila ada yang mencoba mencatat transaksi di bulan yang sudah ditutup atau di tanggal yang
tidak wajar. Jadi tidak ada orang yang bisa diam-diam mengubah angka periode lama.

---

## 2. Preferences — aturan main dan "peta akun"

Ini bagian **paling menentukan**. Di sini kita memberi tahu sistem **dua hal**:

**a) Aturan main umum** — misalnya metode penilaian stok (FIFO), format tanggal, cara hitung pajak,
dan pengingat jatuh tempo.

**b) "Peta akun" (default account)** — ini kuncinya. Setiap jenis transaksi **dikaitkan lebih dulu**
ke akun yang tepat. Contohnya:

- Kalau nanti ada **penjualan** → catat ke akun **Piutang** dan **Pendapatan**.
- Kalau ada **pembelian** → catat ke akun **Persediaan** dan **Utang**.
- Kalau ada **pajak** → masuk ke akun **PPN**.

Karena "peta" ini sudah dibuat di awal, pengguna nanti **tidak perlu memilih akun satu per satu**
saat input. Cukup isi transaksinya, dan sistem otomatis mencatat ke akun yang benar. **Inilah yang
membuat jurnal terbentuk otomatis** — dan kenapa laporan keuangan bisa langsung rapi.

---

## 3. User Profile — siapa boleh melakukan apa

Ini soal **keamanan dan kepercayaan**. Tiap staf diberi **akun login sendiri**, lalu diatur **hak
aksesnya**: boleh membuat, mengubah, menghapus, atau hanya melihat — per bagian (penjualan,
pembelian, buku besar, dan seterusnya).

Prinsipnya, **jangan satu orang boleh melakukan semuanya**. Yang menginput, yang menyetujui, dan yang
memegang uang sebaiknya **orang berbeda**. Hak yang paling berisiko — seperti **menghapus data** atau
**mengubah harga jual** — dibatasi ketat. Ini melindungi perusahaan dari kesalahan maupun kecurangan.

---

## Intinya (satu tarikan napas)

> **Semua data setup — jati diri perusahaan, aturan main + peta akun, dan hak akses — disiapkan
> sebelum transaksi pertama.** Karena persiapan ini rapi, saat pengguna menginput transaksi, sistem
> sudah tahu harus mencatat ke mana. Hasilnya: jurnal otomatis, buku besar rapi, dan **laporan
> keuangan terbentuk sendiri** — tanpa pengguna harus mahir akuntansi.
