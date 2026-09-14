# Contributing / Panduan Kontribusi

Thanks for helping build an open accounting model! / Terima kasih sudah membantu membangun model akuntansi terbuka!

## 🇬🇧 English

### Ways to contribute
1. **Data** — the most valuable. Add examples under `data/` following the schema below. Real cases must be **anonymized** (no real names, tax IDs, or account numbers).
2. **Eval tasks** — add test cases under `eval/` so we can measure quality objectively.
3. **Training/inference code** — recipes, configs, scripts.
4. **Docs** — improve `docs/en` and `docs/id`.
5. **Issues** — report gaps, wrong outputs, or propose capabilities.

### Data schema (JSONL)
Each line is one example:
```json
{"task": "journal_entry", "instruction": "Record: paid office rent 5,000,000 by bank transfer", "input": "", "output": "Dr Rent Expense 5,000,000 / Cr Bank 5,000,000", "lang": "en", "standard": "general"}
```
Fields: `task` (journal_entry | coa_mapping | categorization | qa | statement), `instruction`, `input` (optional context), `output`, `lang` (en|id), `standard` (general|ifrs|psak).

### Workflow
1. Fork → branch → add your changes.
2. Keep data anonymized and correct (double-entry must balance).
3. Open a Pull Request describing what you added and the source/basis.
4. A maintainer reviews for correctness before merge.

### Rules
- **No proprietary or confidential data.** Only data you have the right to share openly.
- Double-entry examples **must balance** (total debit = total credit).
- Cite the standard where relevant (PSAK article / IFRS / general principle).

## 🇮🇩 Bahasa Indonesia

### Cara berkontribusi
1. **Data** — paling berharga. Tambahkan contoh di `data/` mengikuti skema di atas. Kasus nyata **wajib dianonimkan** (tanpa nama asli, NPWP, atau nomor rekening).
2. **Tugas evaluasi** — tambah kasus uji di `eval/` agar kualitas bisa diukur objektif.
3. **Kode training/inference** — resep, konfigurasi, skrip.
4. **Dokumentasi** — perbaiki `docs/id` dan `docs/en`.
5. **Issue** — laporkan kekurangan, output salah, atau usul kemampuan baru.

### Alur
1. Fork → branch → tambahkan perubahan.
2. Data harus anonim & benar (jurnal double-entry harus balance).
3. Buka Pull Request, jelaskan apa yang ditambahkan dan sumber/dasarnya.
4. Maintainer memeriksa kebenaran sebelum merge.

### Aturan
- **Tidak boleh data rahasia/proprietary.** Hanya data yang berhak kamu bagikan terbuka.
- Contoh double-entry **harus balance** (total debit = total kredit).
- Sebutkan standar bila relevan (pasal PSAK / IFRS / prinsip umum).

---
By contributing, you agree your contributions are licensed under **Apache-2.0**. / Dengan berkontribusi, kamu setuju kontribusimu berlisensi **Apache-2.0**.
