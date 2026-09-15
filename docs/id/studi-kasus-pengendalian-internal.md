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

---

## Kasus 2 — Beban Disembunyikan sebagai "Biaya Dibayar Dimuka" (Laba Semu)

**Konteks:** PT yang sama. Baru **diambil alih manajemen baru** dari owner lama yang sedang
**kesulitan likuiditas** — namun anehnya laporan keuangan (*FS*) disajikan dalam keadaan **LABA**.
Auditor manajemen baru (sebelum *accounting head* bergabung) pun belum menemukan letak kekeliruannya.

**Temuan:** Ada akun **Biaya Dibayar Dimuka** senilai **ratusan juta** yang isinya sebenarnya =
**Biaya THR karyawan** — beban yang sudah menjadi kewajiban, **bukan** aset/manfaat masa depan.

**Prinsip yang dilanggar:** THR adalah **beban periode berjalan** (diakui saat kewajiban timbul/
dibayar), **bukan** "dibayar dimuka". Menaruhnya di *prepaid* = **menunda/menyembunyikan beban**
→ **laba overstated (laba semu)**.

**Koreksi / reklas:**
```
Dr  Biaya THR Karyawan
    Cr  Biaya Dibayar Dimuka
```
**Dampak:** Laporan Laba Rugi **otomatis turun** — dalam kasus ini berubah jadi **rugi besar**.
BOD kantor pusat akhirnya paham mereka membeli **perusahaan yang sebenarnya sedang rugi besar**,
bukan perusahaan laba.

**Red flag:**
1. Perusahaan **kesulitan likuiditas** tapi FS **menunjukkan laba** — inkonsistensi (laba sehat
   mestinya diiringi arus kas sehat).
2. Akun **Biaya Dibayar Dimuka / aset ditangguhkan membengkak** tidak wajar.
3. Isi akun *prepaid* ternyata **beban yang sudah terjadi** (THR), bukan manfaat masa depan.

**Pelajaran:**
- **Buka rincian akun *prepaid* / *deferred*** — pastikan benar-benar manfaat masa depan, bukan
  beban yang disembunyikan.
- **Rekonsiliasi Laba vs Arus Kas:** laba besar tapi kas ketat = sinyal manipulasi.
- **Due diligence akuisisi** wajib membedah rincian akun, bukan hanya melihat FS ringkas.

---

## Kasus 3 — Piutang (AR) Macet karena Customer Mengulur Bayar (Krisis Likuiditas)

**Konteks:** PT jasa kebersihan menempatkan *crew* di beberapa **outlet** (mall besar &
perkantoran); mall besar menyerap *man power* terbanyak. *(Nama outlet/mall dianonimkan.)*

**Temuan:** Piutang (**AR**) ke customer mall besar **menunggak sampai ~8 bulan**, padahal
**TOP (termin) 60 hari** sejak invoice diterima & *complete*. Total **AR overdue ~Rp8 miliar**.

**Modus customer mengulur bayar:**
- Proses meng-*complete*-kan invoice **dipersulit**; invoice **ditolak berulang** dengan berbagai
  alasan — mis. absensi crew dianggap tidak lengkap, atau baru mau terima faktur pajak kalau
  **bukti setor pajak ke kas negara** sudah ada dulu — alasan yang **dibuat-buat** untuk lambat bayar.

**Dampak:**
- Likuiditas tergerus; **tiap mau gajian tidak ada dana → harus pinjam ke pusat/owner**.
- Revenue sudah **diakui (akrual)** tetapi **kas tidak masuk** → di atas kertas seolah jalan,
  tetapi **arus kas negatif** (menyambung tema Kasus #2: **laba ≠ kas**).

**Keputusan / saran ke BOD:**
- **Putus kontrak & tarik semua crew** dari outlet bermasalah. Menyuplai jasa tanpa dibayar =
  perusahaan menanggung gaji sementara customer menikmati jasa → **subsidi likuiditas** yang merugikan.

**Red flag & pelajaran (manajemen AR / modal kerja):**
1. **AR aging** jauh melewati TOP (8 bulan vs 60 hari) → sinyal **gagal tagih**.
2. Customer **mempersenjatai proses penerimaan invoice** (menolak via teknikalitas) untuk mengulur.
3. Kontrol: **SOP kelengkapan invoice disepakati di muka** dalam kontrak (absensi, berita acara,
   dokumen faktur pajak) agar customer tak bisa mengarang alasan; **monitoring aging rutin**;
   **stop-supply trigger** bila overdue melewati ambang; bentuk **cadangan kerugian piutang** untuk yang macet.
4. Prinsip: jangan subsidi customer dengan likuiditas sendiri — **collection sama pentingnya dengan penjualan**.

**Accounting treatment:**
Cadangan kerugian piutang (bila diragukan tertagih):
```
Dr  Beban Kerugian Piutang
    Cr  Cadangan Kerugian Piutang
```
Penghapusan piutang tak tertagih (memakai cadangan):
```
Dr  Cadangan Kerugian Piutang
    Cr  Piutang Usaha
```

---

## Kasus 4 — Salah Hitung Harga Jual: Overhead Tidak Diperhitungkan (Rugi Struktural)

**Konteks:** *(Auditor mengaudit model penetapan harga.)* Manajer operasional menyusun proposal
harga sebagai penyedia *crew* cleaning ke mall. Saat di-*recheck*, cara menghitungnya hanya
memasukkan **direct cost di outlet** dari *manpower*.

**Temuan — komponen yang dihitung (hanya direct cost):**
- Gaji crew
- BPJS Ketenagakerjaan (TK)
- BPJS Kesehatan
- **Management fee 10%** dari total biaya *manpower* (dianggap sebagai margin)

**Yang TERLUPA (indirect / overhead kantor):**
- Biaya operasional kantor
- Gaji **staff, manajer, dan direktur** (biaya tidak langsung)

**Akibat:** di ringkasan Laba Rugi, **total biaya > pendapatan**. Management fee 10% **tidak cukup**
menutup overhead → **rugi struktural** (bukan rugi karena satu transaksi, tapi karena modelnya salah).

**Prinsip yang dilanggar (costing / pricing):**
- Harga jual harus menutup **full cost** = **direct cost** (manpower) + **overhead teralokasi**
  (opex kantor, gaji admin/manajemen/direksi) + **margin laba**.
- **Contribution margin** (harga − direct cost) bisa positif, tetapi jika tidak menutup overhead →
  **net margin negatif**.
- Persentase *management fee* harus **dikalibrasi** untuk menutup overhead + laba, bukan sekadar
  *markup* di atas direct cost.

**Ilustrasi angka (per unit kontrak):**
```
Direct cost (manpower)          100
Management fee 10%               10   -> harga jual = 110
Overhead teralokasi              20
Laba/(Rugi) = 110 - 100 - 20 = (10)   -> RUGI
Seharusnya: harga >= full cost (120) + margin
```

**Red flag:**
1. Proposal/tender dihargai = *direct cost + markup*, **tanpa alokasi overhead**.
2. Outlet "kelihatan untung" (per direct cost) padahal **perusahaan rugi** di level konsolidasi.

**Pelajaran:**
- Bangun **model costing lengkap**: direct labor per outlet + **alokasi overhead** (per kepala /
  per pendapatan) + target margin.
- **Kalibrasi management fee** agar menutup overhead + laba.
- Finance/auditor harus **mereview model penetapan harga**, bukan hanya pencatatan transaksi.
- Struktur L/R: `Pendapatan − Beban Pokok (crew) = Laba Kotor; − Beban Operasional (overhead) = Laba Bersih`.
  Jika overhead tidak dimasukkan ke harga, Laba Bersih negatif.
