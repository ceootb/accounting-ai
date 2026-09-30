# Revaluasi Aset Tetap — Model Revaluasi (PSAK 16)

> **Versi PSAK / ideal accounting** (untuk direview). Perlakuan **pajak/fiskal** dibahas **terpisah**
> (lihat catatan di bawah). Langkah UI/UX di software & perbandingannya menyusul (simulasi Tere).

Setelah pengakuan awal, aset tetap dapat diukur dengan **dua model**:
- **Model biaya (cost model)** — dicatat sebesar **harga perolehan − akumulasi penyusutan − penurunan
  nilai**.
- **Model revaluasi (revaluation model)** — dicatat sebesar **nilai wajar pada tanggal revaluasi**,
  dikurangi **akumulasi penyusutan & penurunan nilai** setelahnya (syarat: nilai wajar dapat diukur
  andal).

## Prinsip

- Revaluasi dilakukan **cukup teratur** agar *carrying amount* **tidak berbeda material** dari nilai
  wajar.
- **Satu kelas aset direvaluasi seluruhnya** (mis. seluruh Tanah, atau seluruh Bangunan) — **bukan**
  memilih satu aset saja.

## Perlakuan akumulasi penyusutan saat revaluasi (dua metode)

1. **Proporsional (gross-up)** — harga perolehan bruto & akumulasi penyusutan **di-restate proporsional**
   sehingga nilai buku = nilai revaluasi.
2. **Eliminasi (net)** — akumulasi penyusutan **dieliminasi** dulu ke harga perolehan bruto, lalu nilai
   buku neto disesuaikan ke nilai wajar.

## Jurnal saat revaluasi

**Kenaikan (revaluation surplus):** dicatat di **Penghasilan Komprehensif Lain (OCI)** dan diakumulasi
di ekuitas sebagai **Surplus Revaluasi** — **kecuali** membalik penurunan revaluasi aset yang sama yang
sebelumnya diakui di **Laba-Rugi**, maka kenaikan diakui di **Laba-Rugi** sebesar pembalikan itu.

**Contoh (metode eliminasi):** harga perolehan **Rp100jt**, akumulasi penyusutan **Rp40jt** → nilai buku
**Rp60jt**; nilai wajar **Rp90jt** → **surplus Rp30jt**:
```
Dr  Akumulasi Penyusutan        40jt
    Cr  Aset Tetap               40jt      (eliminasi → nilai buku 60jt)
Dr  Aset Tetap                  30jt
    Cr  Surplus Revaluasi (OCI)  30jt      (naikkan ke nilai wajar 90jt)
```

**Penurunan (revaluation decrease):** diakui sebagai **beban di Laba-Rugi** — **kecuali** ada **saldo
Surplus Revaluasi** untuk aset itu, maka penurunan **mengurangi surplus dulu** (lewat OCI), sisanya baru
ke Laba-Rugi.

## Setelah revaluasi

- **Penyusutan berikutnya** dihitung atas **nilai revaluasi** selama **sisa umur manfaat**.
- **Surplus Revaluasi** dapat **dipindahkan ke Saldo Laba (retained earnings)** — saat aset **dilepas**,
  atau **sejalan pemakaian** aset (selisih penyusutan berbasis nilai revaluasi vs berbasis biaya awal).
  Perpindahan ini **tidak** melalui Laba-Rugi.

## Catatan pajak (TERPISAH)

> Revaluasi **komersial (PSAK)** **≠ otomatis** revaluasi **fiskal**. Revaluasi untuk tujuan pajak punya
> **ketentuan tersendiri** (mis. PMK terkait) dengan syarat & tarif PPh final tersendiri. **Jangan
> mencampur** keduanya — selisih perlakuan diselesaikan di **tax reconciliation**, bukan dengan mengubah
> jurnal komersial. (Lihat [Strategi Pajak & Koreksi Fiskal](strategi-pajak-koreksi-fiskal.md).)

---

*Catatan: halaman ini **konsep PSAK (umum/ideal)** untuk acuan & review, bukan pengganti standar/
ketentuan resmi. Angka hanya ilustrasi. Perlakuan pajak & langkah di software spesifik dikonfirmasi
terpisah.*
