# Pelepasan Aset Tetap (Fixed Asset Disposal)

Disposal **bukan sekadar menghapus aset dari daftar**. Ini **satu workflow** yang: mengubah **status**
aset, memindahkan **catatan historis**, dan **otomatis menghasilkan jurnal** sampai perhitungan
**laba/rugi pelepasan** — **tanpa user membuat jurnal manual**.

## 1. Cara kerja (workflow)

- Disposal dilakukan **langsung dari aset** yang akan dijual (tombol **Dispose** pada aset tersebut).
- User cukup mengisi **nilai jual (proceeds)**.
- User **tidak** membuat jurnal disposal manual — **sistem otomatis** membuatnya. Jurnal ini bersifat
  *auto-generated* dan **tersembunyi (hidden)** dari user.

## 2. Perubahan status & catatan historis

- Setelah diproses, aset **tidak lagi muncul** di daftar **Fixed Asset aktif**.
- **Data aset tidak hilang** — berpindah ke menu **Fixed Assets Disposal** sebagai **historical
  disposal record**, sehingga transaksi **tetap dapat ditelusuri**.

## 3. Perlakuan akuntansi (dilakukan sistem otomatis)

Saat aset dijual, sistem otomatis:
1. **Mengeluarkan cost / harga perolehan** aset dari Aset Tetap.
2. **Me-reversal Akumulasi Penyusutan** yang sudah terbentuk **sampai periode sebelum disposal**.
3. **Mencatat proceeds / nilai jual**.
4. **Menghitung selisihnya** sebagai **Gain or Loss on Fixed Asset Disposal**.

**Bentuk jurnalnya (konsep):**
```
Dr  Kas/Bank                         (proceeds / nilai jual)
Dr  Akumulasi Penyusutan             (saldo s/d periode sebelum disposal)
    Cr  Aset Tetap (harga perolehan)   (cost)
    Cr  Laba Pelepasan Aset Tetap      (jika untung)   ── atau ──
Dr  Rugi Pelepasan Aset Tetap        (jika rugi)
```

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

```
Dr  Kas/Bank                         40jt
Dr  Akumulasi Penyusutan             90jt
    Cr  Aset Tetap (harga perolehan)  120jt
    Cr  Laba Pelepasan Aset Tetap      10jt      (Other Income)
```
*(Bila dijual Rp25jt → Rugi Rp5jt: `Dr Rugi Pelepasan Aset Tetap 5jt` menggantikan baris laba, sisi
debit-kredit tetap balance.)*

> **Intinya:** disposal = workflow yang **mengubah status aset + memindahkan historical record +
> otomatis menjurnal** (keluarkan cost, reversal akumulasi penyusutan s/d sebelum disposal, catat
> proceeds, hitung laba/rugi) — **tanpa jurnal manual**. Lihat juga [Modul Aset Tetap](modul-fixed-asset.md).
