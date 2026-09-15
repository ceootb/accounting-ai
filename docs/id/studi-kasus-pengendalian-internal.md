# Studi Kasus — Pengendalian Internal (Temuan Nyata)

> Kumpulan **kasus nyata** (dianonimkan) dari praktik seorang *accounting head*.
> Tujuannya: melatih model mengenali **red flag**, memahami **kontrol**, dan tahu **treatment**
> akuntansi yang benar — bukan hanya teori. Semua nama/entitas dihilangkan.

---

## Kasus 1 — Kas Kecil Membengkak (Metode Dana Tetap / Imprest)

**Konteks:** Sebuah PT jasa kebersihan (*cleaning service*). Temuan pada minggu pertama
seorang *accounting head* baru bergabung.

**Temuan:**
- Ledger **Kas Kecil** menunjukkan saldo sekitar **Rp100 juta**.
- Padahal kebijakan direktur: kas kecil memakai **metode Dana Tetap (imprest)** sebesar **Rp10 juta**.
- **Cash opname** fisik: uang yang ada **tidak sampai Rp10 juta** (jauh di bawah).
- Banyak **bon gantung** — uang diambil di muka (*advance*) **tanpa settlement/receipt**
  (tidak dipertanggungjawabkan).
- Audit sebelumnya **tidak menemukan** pelanggaran di bagian finance/accounting.

**Prinsip yang dilanggar:**
- Pada metode **imprest**, saldo Kas Kecil di ledger **harus SELALU = dana tetap (Rp10 juta)**.
  Yang berubah hanya **komposisinya**: `uang fisik + bukti pengeluaran (bon berbukti)` = Rp10 juta.
  Pengisian kembali (*replenishment*) hanya **sebesar yang sudah dibelanjakan & berbukti**.
- Kalau saldo ledger membengkak jadi Rp100 juta → **replenishment dilakukan tanpa menutup bon**,
  artinya metode imprest tidak dijalankan (indikasi kelalaian atau penyalahgunaan).
- **Bon gantung** tanpa pertanggungjawaban seharusnya **direklas ke Uang Muka / Piutang Karyawan**,
  bukan dibiarkan menumpuk di Kas Kecil.

**Red flag (yang wajib dicek):**
1. Saldo ledger Kas Kecil **≠** jumlah dana tetap yang ditetapkan.
2. **Cash opname fisik** tidak cocok dengan rumus imprest.
3. **Bon/advance menggantung lama** tanpa receipt/settlement.

**Cara verifikasi (rekonsiliasi imprest):**
```
Uang fisik (opname) + Bon berbukti (belum di-replenish) + Advance belum settle = Dana Tetap
```
Kalau tidak seimbang → ada selisih yang harus ditelusuri.

**Treatment akuntansi (reklas bon gantung):**
```
Dr  Uang Muka / Piutang Karyawan
    Cr  Kas Kecil
```

**Pelajaran:**
- **Audit dokumen saja tidak cukup** — dokumen bisa terlihat rapi. Wajib **cash opname mendadak**
  + rekonsiliasi imprest untuk menemukan selisih fisik.
- **Kontrol yang benar:** dana imprest tetap; replenishment harus berbukti; ada **batas waktu
  settlement** advance; pisahkan uang muka ke akun Piutang/Uang Muka.
