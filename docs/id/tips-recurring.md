# Tips: Recurring (Transaksi Berulang Otomatis)

> **Recurring** = fitur untuk membuat **voucher rutin/berulang** secara periodik (bulanan, kuartalan)
> tanpa mengetik ulang tiap periode. **Bagian dari tips hemat waktu** — daripada entry satu per satu.
> Bisa dipakai untuk **Sales Invoice, Purchase Invoice, dan Journal Voucher**.

**Contoh pemakaian:**
- **Sales Invoice** → tagihan **komisi bulanan** ke pelanggan.
- **Purchase Invoice** → tagihan rutin: **PAM, PLN, Telepon**, sewa, dll.
- **Journal Voucher** → penyesuaian rutin, mis. **tax allowance atas PPh 21 karyawan**.

---

## Prasyarat: perpanjang Accounting Period dulu

Recurring akan **membuat jurnal ke periode masa depan**. Jadi **sebelum** mulai, buka
**Company Info → Accounting Period** dan **perpanjang batas periode minimal 12 bulan setelah periode
berjalan** (kolom *Warn if* / *Error if*). Kalau tidak, sistem akan menolak (error) karena entry di
luar rentang periode yang diizinkan.

---

## Cara membuatnya (mulai dari voucher master)

> Recurring **dimulai dari voucher-nya**, bukan dari menu List Recurring (tombol **New** di list itu
> non-aktif).

1. **Entry voucher master** (mis. satu Sales Invoice biasa) lalu **Save**.
2. Klik tombol **Recurring** di voucher itu → layar otomatis pindah ke **New Recurring**.
3. Isi field:
   - **Recurring Periode** → pilih dari dropdown: **Monthly / Quarterly**.
   - **Number of Times** → berapa kali dibuat (mis. `4` → membuat 4 voucher ke depan).
   - **Reference** & **Description**.
   - Sistem **otomatis mengisi grid** tanggal per periode (baris 1, 2, 3, …).
4. Centang **Assign Form/Invoice Number**, lalu klik kolom **Start from** (cukup taruh kursor) →
   nomor faktur **terisi otomatis mengikuti urutan** dari voucher master.
5. Klik **Save** → otomatis masuk ke **List Recurring**.

**Kolom Executed:** tanda **centang** artinya voucher itu **sudah benar-benar di-entry & di-save**.
Voucher **pertama** (dari master tadi) otomatis ter-*execute*. Voucher periode masa depan yang belum
jatuh tempo masih bersifat **accrual** (di layar sering tampil dengan nilai *placeholder* kecil
sampai benar-benar dibuat menjadi voucher aktual).

---

## Cara mengeksekusi voucher berikutnya

Voucher ke-2 dan seterusnya dibuat satu per satu saat periodenya tiba:

1. Di **List Recurring**, **dobel-klik** baris recurring (yang tersorot biru).
2. **Klik kanan** pada baris yang **belum** ter-*execute* → pilih **Create Invoice**.
3. Layar otomatis pindah ke **Sales Invoice** (data sudah terisi dari master) → cek → **Save**.
4. Kembali ke layar recurring → klik **Refresh** → muncul **centang** di kolom **Executed** (tanda
   voucher berhasil dibuat & disimpan).
5. **Ulangi** untuk voucher periode berikutnya (Create Invoice → Save → Refresh) sampai **semua**
   ter-*execute* → **Save & Close**.

---

## Intinya

> **Recurring = "cetak ulang otomatis" voucher rutin.** Buat master sekali → tentukan periode &
> jumlahnya → sistem menyiapkan voucher untuk tiap periode; tinggal *Create Invoice* saat waktunya
> tiba. Hemat waktu untuk tagihan/biaya/penyesuaian yang **sama tiap bulan**, sekaligus membantu
> **kontrol biaya & estimasi cash flow** ke depan. *(Ini tips efisiensi, bukan aturan akuntansi baru —
> jurnal yang dihasilkan tetap sama seperti voucher biasa.)*
