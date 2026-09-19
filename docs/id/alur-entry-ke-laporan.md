# Dari Input Transaksi sampai Laporan Keuangan — Penjelasan Sederhana

> Untuk **pengguna yang tidak harus mahir akuntansi**. Tujuannya:
> memahami *bagaimana* satu kali input transaksi bisa berubah sendiri menjadi laporan keuangan.
> Contoh memakai **Sales Invoice (faktur penjualan)** senilai Rp450.000.
>
> *(Istilah/logika teknis untuk membangun software disimpan terpisah — dipakai saat membuat program.)*

---

## Gambaran besar

Bayangkan sebuah "ban berjalan". Pengguna hanya menaruh **data penjualan** di ujung depan; di
ujung belakang keluar **laporan keuangan** yang rapi. Di tengahnya ada 3 mesin otomatis: **jurnal**,
**buku besar**, lalu **laporan**. Pengguna tidak perlu tahu isi mesinnya — cukup memasukkan data
yang benar.

```
Input transaksi  →  Jurnal otomatis  →  Buku Besar  →  Laporan Keuangan
   (user isi)         (sistem)          (sistem)         (sistem)
```

---

## 1. Yang dilakukan pengguna: cukup mengisi data

Di layar Sales Invoice, pengguna **hanya memilih dan mengisi**, bukan menghitung:

- Pilih **Customer** (pelanggan) dari daftar.
- Tarik **Delivery Order** (surat jalan) bila ada, atau langsung isi barangnya.
- Pilih **barang**, isi **jumlah** dan **harga**.
- Pilih **akun piutang** (mau dicatat sebagai piutang jenis apa).

Selesai. Total, pajak, dan potongan dihitung otomatis, karena setiap barang sudah "dikaitkan" ke
akun yang benar saat setup awal. **Pengguna fokus pada kebenaran data, bukan pada hitungan.**

---

## 2. Mesin pertama: data berubah jadi jurnal

Begitu faktur disimpan, sistem langsung menuliskan **catatan akuntansi** secara otomatis. Aturannya
sederhana: **setiap pencatatan selalu punya dua sisi yang jumlahnya sama** (masuk = keluar). Untuk
faktur Rp450.000 tadi, sistem mencatat dua hal:

**a) Perusahaan berhak menagih uang (mengakui penjualan):**
- **Piutang** (uang yang akan diterima) bertambah **Rp450.000**.
- Sebagai lawannya: **Penjualan** diakui **Rp405.406** dan **Pajak (PPN)** yang harus disetor
  **Rp44.594**. (Karena harga sudah termasuk pajak, pajaknya "dikeluarkan" dari total.)

**b) Barang keluar dari gudang (mengakui biaya barang):**
- **Biaya pokok barang** yang terjual dicatat **Rp234.000**.
- **Persediaan** (nilai stok) berkurang **Rp234.000**.

Inilah jembatannya: *aktivitas jualan* langsung menjadi *catatan keuangan yang selalu seimbang*,
tanpa pengguna menghitung atau menulis apa pun.

---

## 3. Mesin kedua: jurnal masuk ke Buku Besar

Semua catatan tadi lalu "dirapikan per akun" di **Buku Besar**. Kalau jurnal itu seperti *struk
harian*, Buku Besar itu seperti *rekening koran per pos*: ada halaman khusus Piutang, halaman
Penjualan, halaman Persediaan, dan seterusnya. Setiap kali ada transaksi baru menyentuh sebuah
akun, saldonya diperbarui di sini.

Jadi Buku Besar menjawab pertanyaan: *"Total penjualan bulan ini berapa? Total piutang sekarang
berapa?"* — bukan per faktur lagi, tapi total per pos.

---

## 4. Mesin ketiga: Buku Besar diringkas jadi Laporan Keuangan

Saldo akhir tiap akun ditarik ke laporan yang bisa dibaca manajemen:

- **Penjualan** dan **Biaya pokok barang** naik ke **Laporan Laba Rugi** → selisihnya = **laba**.
- **Piutang** dan **Persediaan** masuk sebagai **harta** di **Neraca**; **Pajak yang belum disetor**
  masuk sebagai **kewajiban**.
- **Laba** dari Laba Rugi kemudian menambah **modal** perusahaan di Neraca.

Semua ini terjadi otomatis. Manajer tinggal membaca hasilnya untuk mengambil keputusan.

---

## Intinya (satu tarikan napas)

> **Pengguna cukup memasukkan data penjualan yang benar. Sistem yang menjurnal, meringkas ke Buku
> Besar, lalu menyusun Laporan Keuangan.** Karena itu, staf tidak harus mahir akuntansi — cukup
> teliti mengisi data. Yang **wajib paham akuntansi adalah manajer/pengawas**, supaya bisa membaca
> laporan, menilai kewajaran angka, dan mengambil keputusan.
