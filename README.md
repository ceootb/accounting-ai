<div align="center">

# Accounting AI — a small, open language model for accounting

**A compact, open-source AI model specialized for accounting & bookkeeping.**
*Model AI kecil sumber-terbuka yang dikhususkan untuk akuntansi & pembukuan.*

[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)
[![Status](https://img.shields.io/badge/status-early--stage-orange)](#roadmap--peta-jalan)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

</div>

---

## 🇬🇧 English

### What is this?
**Accounting AI** is a community effort to build a *small* language model (SLM) that is genuinely good at accounting tasks — small enough to run cheaply (CPU / a single modest GPU / on-device), open enough that anyone can use, inspect, and improve it.

It is **not** a general chatbot. It is focused on a narrow, high-value domain so a small model can beat much larger general models on the tasks that matter.

### Target capabilities
- **Journal entries** — turn a plain-language transaction into a correct double-entry journal (debit/credit).
- **Chart of Accounts (COA) mapping** — classify a transaction to the right account.
- **Transaction categorization** — bulk-label bank/e-wallet/POS lines.
- **Bookkeeping Q&A** — answer practical questions (accruals, VAT/PPN, depreciation, closing).
- **Statement helpers** — assist building trial balance, P&L, balance sheet.
- **Localization** — first-class support for **Indonesian accounting practice (PSAK, PPN, faktur)** alongside general/IFRS concepts.

### Why small & open?
- **Cheap to run** → usable by UMKM, students, and developers without paying per token.
- **Private** → can run offline / on-prem for sensitive financial data.
- **Improvable by everyone** → open data + open training recipe means the community keeps it current.

### 🛰️ Edge AI — runs on-device
A core design goal: the model is small enough to run **at the edge / on-device** — phone, laptop, mini-PC, or even in the browser — with **no internet and no cloud**. Financial data never leaves the device.
- Quantized to **GGUF (4-bit)** ≈ 0.7–2 GB, runs on CPU.
- Deploy via **llama.cpp**, **Ollama**, **MLC-LLM** (Android/iOS), or **WebLLM** (browser).
- Private by default → ideal for sensitive accounting data.

### Repository structure
```
accounting-ai/
├── data/         # Open datasets (instruction → response) for accounting tasks
├── training/     # Fine-tuning recipes & configs (base model → accounting SLM)
├── inference/    # Example scripts to run the model
├── eval/         # Benchmarks & evaluation harness (how we measure "good")
├── docs/         # Documentation (en/ + id/)
└── MODEL_CARD.md # What the model is, data, limits, intended use
```

### Status
Early-stage / foundation. We are assembling datasets and the training recipe first. Model weights will be published on **Hugging Face** once a first version passes evaluation. See the [roadmap](#roadmap--peta-jalan).

### How to help
Anyone can contribute — see **[CONTRIBUTING.md](CONTRIBUTING.md)**. Especially wanted: real (anonymized) accounting examples, COA templates, PSAK-based test cases, and eval tasks.

---

## 🇮🇩 Bahasa Indonesia

### Apa ini?
**Accounting AI** adalah proyek komunitas untuk membangun *model bahasa kecil* (SLM) yang benar-benar jago tugas akuntansi — cukup kecil untuk jalan murah (CPU / 1 GPU sederhana / di perangkat), cukup terbuka sehingga siapa pun bisa memakai, memeriksa, dan menyempurnakannya.

Ini **bukan** chatbot serba bisa. Fokusnya sempit tapi bernilai tinggi, supaya model kecil bisa mengalahkan model umum yang jauh lebih besar pada tugas yang penting.

### Kemampuan yang dituju
- **Jurnal** — ubah transaksi bahasa sehari-hari jadi jurnal double-entry yang benar (debit/kredit).
- **Pemetaan COA (Bagan Akun)** — klasifikasikan transaksi ke akun yang tepat.
- **Kategorisasi transaksi** — melabeli baris mutasi bank/e-wallet/POS secara massal.
- **Tanya-jawab pembukuan** — menjawab pertanyaan praktis (akrual, PPN, penyusutan, tutup buku).
- **Bantu laporan** — membantu menyusun neraca saldo, laba-rugi, neraca.
- **Lokalisasi** — dukungan utama untuk **praktik akuntansi Indonesia (PSAK, PPN, faktur)** di samping konsep umum/IFRS.

### Kenapa kecil & terbuka?
- **Murah dijalankan** → bisa dipakai UMKM, pelajar, dan developer tanpa bayar per token.
- **Privat** → bisa jalan offline / on-premise untuk data keuangan sensitif.
- **Bisa disempurnakan siapa saja** → data & resep training terbuka, jadi komunitas menjaganya tetap relevan.

### 🛰️ Edge AI — jalan di perangkat
Tujuan desain inti: model cukup kecil untuk jalan **di edge / di perangkat** — HP, laptop, mini-PC, bahkan di browser — **tanpa internet, tanpa cloud**. Data keuangan tidak pernah keluar dari perangkat.
- Di-quantize ke **GGUF (4-bit)** ≈ 0,7–2 GB, jalan di CPU.
- Deploy via **llama.cpp**, **Ollama**, **MLC-LLM** (Android/iOS), atau **WebLLM** (browser).
- Privat secara bawaan → ideal untuk data akuntansi sensitif.

### Struktur repo
Lihat diagram di bagian English di atas (`data/`, `training/`, `inference/`, `eval/`, `docs/`, `MODEL_CARD.md`).

### Status
Tahap awal / fondasi. Kami menyusun dataset dan resep training dulu. Bobot model akan dirilis di **Hugging Face** begitu versi pertama lulus evaluasi.

### Cara bantu
Siapa pun boleh berkontribusi — baca **[CONTRIBUTING.md](CONTRIBUTING.md)**. Yang sangat dibutuhkan: contoh akuntansi nyata (dianonimkan), template COA, kasus uji berbasis PSAK, dan tugas evaluasi.

---

## Roadmap / Peta Jalan
- [ ] **v0 — Foundation:** dataset schema, seed data (jurnal, COA, Q&A), eval harness.
- [ ] **v0.1 — First model:** fine-tune a small base (e.g. Qwen/Llama/Phi 1–3B) on seed data, publish to Hugging Face.
- [ ] **v0.2 — Indonesian focus:** PSAK/PPN datasets + benchmark.
- [ ] **v1 — Usable:** inference API + evaluation report + docs.
- [ ] **v1 — Edge builds:** GGUF (4-bit) + Ollama modelfile + on-device demo (mobile/browser).

## License / Lisensi
[Apache-2.0](LICENSE) — free to use, including commercially. *Bebas dipakai, termasuk komersial.*

## Maintainers
- Tere — lead maintainer
- ceootb — org

> Built openly so it can be used by everyone and improved forever. / Dibangun terbuka supaya bisa dipakai semua orang dan terus disempurnakan.
