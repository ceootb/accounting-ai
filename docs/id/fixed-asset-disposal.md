# Pelepasan Aset Tetap (Fixed Asset Disposal)

Disposal **bukan sekadar menghapus aset dari daftar**. Ini **satu workflow** yang: mengubah **status**
aset, memindahkan **catatan historis**, dan **otomatis menghasilkan jurnal** sampai perhitungan
**laba/rugi pelepasan** — **tanpa user membuat jurnal manual**.

## 1. Cara kerja (workflow)

- Disposal dilakukan **langsung dari aset** yang akan dijual (tombol **Dispose** pada aset tersebut).
- User cukup mengisi **nilai jual (proceeds)**; akun yang dipakai = **Fixed Asset Transaction** (akun
  **perantara/clearing**, sama seperti saat pembelian aset — **bukan** akun pendapatan).
- User **tidak** membuat jurnal disposal manual — **sistem otomatis** membuatnya. Jurnal ini bersifat
  *auto-generated* dan **tersembunyi (hidden)** dari user. Setelah diproses, aset diberi stamp
  **DISPOSED**, dan masih ada tombol **Undo Dispose** selama **Period End** belum dijalankan.

## 2. Perubahan status & catatan historis

- Setelah diproses, aset **tidak lagi muncul** di daftar **Fixed Asset aktif**.
- **Data aset tidak hilang** — berpindah ke menu **Fixed Assets Disposal** sebagai **historical
  disposal record**, sehingga transaksi **tetap dapat ditelusuri**.

## 3. Perlakuan akuntansi (dilakukan sistem otomatis)

Pelepasan berjalan **dua langkah** lewat akun perantara **Fixed Asset Transaction**:

**a) Saat dana penjualan diterima** (transaksi penerimaan biasa):
```
Dr  Kas/Bank
    Cr  Fixed Asset Transaction        (nilai jual / proceeds)
```

**b) Saat disposal dieksekusi** (auto-jurnal), sistem otomatis:
1. **Mengeluarkan cost / harga perolehan** aset dari Aset Tetap.
2. **Me-reversal Akumulasi Penyusutan** yang terbentuk **sampai periode sebelum disposal**.
3. **Meng-offset** akun **Fixed Asset Transaction** (proceeds yang tadi masuk).
4. **Menghitung selisihnya** sebagai **Gain or Loss on Fixed Asset Disposal**.
```
Dr  Fixed Asset Transaction          (proceeds — meng-offset penerimaan di langkah a)
Dr  Akumulasi Penyusutan             (saldo s/d periode sebelum disposal)
    Cr  Aset Tetap (harga perolehan)   (cost)
    Cr  Laba Pelepasan Aset Tetap      (jika untung)   ── atau ──
Dr  Rugi Pelepasan Aset Tetap        (jika rugi)
```
> Akun **Fixed Asset Transaction** jadi **nol (off-set)** setelah kedua langkah: di-**kredit** saat
> terima dana, lalu di-**debit** saat disposal. Kas **tidak** langsung masuk ke jurnal disposal —
> disposal hanya lewat akun perantara. *(Pola sama dengan pembelian aset: transaksi → Fixed Asset
> Transaction → Aset Tetap.)*

## 4. Batas reversal Akumulasi Penyusutan

Reversal akumulasi penyusutan **hanya sampai YTD periode sebelum aset dijual** — **bukan** penyusutan
untuk periode setelah disposal.

> **Contoh:** aset dijual pada **September** → akumulasi penyusutan yang direversal = **YTD sampai
> Agustus**. Penyusutan **September dan periode setelahnya tidak ikut terbentuk / reversed**, karena
> aset sudah didispose.

## 5. Akun Gain / Loss

Selisih antara **carrying amount / nilai buku (NBV)** aset dengan **nilai jual** masuk ke akun
**Gain or Loss on Fixed Asset Disposal**, dengan **parent account Other Income**.

- **NBV = harga perolehan − akumulasi penyusutan** (s/d periode sebelum disposal).
- **Proceeds > NBV → Laba**; **Proceeds < NBV → Rugi**.

## Contoh angka

Aset: harga perolehan **Rp120jt**, akumulasi penyusutan s/d Agustus **Rp90jt** → **NBV Rp30jt**.
Dijual September seharga **Rp40jt** → **Laba Rp10jt** (40 − 30).

**a) Terima dana:**
```
Dr  Kas/Bank                         40jt
    Cr  Fixed Asset Transaction       40jt
```
**b) Disposal dieksekusi:**
```
Dr  Fixed Asset Transaction          40jt      (off-set proceeds)
Dr  Akumulasi Penyusutan             90jt
    Cr  Aset Tetap (harga perolehan)  120jt
    Cr  Laba Pelepasan Aset Tetap      10jt      (Other Income)
```
> Fixed Asset Transaction: Cr 40jt (langkah a) + Dr 40jt (langkah b) = **nol**. Net Laba Rp10jt.
> *(Bila dijual Rp25jt → Rugi Rp5jt: `Dr Rugi Pelepasan Aset Tetap 5jt` menggantikan baris laba, sisi
> debit-kredit tetap balance.)*

> **Intinya:** disposal = workflow yang **mengubah status aset + memindahkan historical record +
> otomatis menjurnal** (keluarkan cost, reversal akumulasi penyusutan s/d sebelum disposal, **proceeds
> lewat akun perantara Fixed Asset Transaction**, hitung laba/rugi) — **tanpa jurnal manual**. Lihat juga
> [Modul Aset Tetap](modul-fixed-asset.md).
