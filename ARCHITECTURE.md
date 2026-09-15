# Architecture / Arsitektur

**Accounting AI is a layered system, not "just an LLM".**
*Accounting AI adalah sistem berlapis, bukan sekadar "LLM".*

```
                 ┌─────────────────────────────────────────────┐
  user input →   │  LAYER 2 — AI model (small / edge)           │  ← language & judgment
  "beli bensin   │  understands language, maps accounts,        │    (ilmu adaptif ibu Tere)
   50rb"         │  handles ambiguity & real-world judgment     │
                 └──────────────────────┬──────────────────────┘
                                        │ proposes a journal
                                        ▼
                 ┌─────────────────────────────────────────────┐
                 │  LAYER 1 — core/ accounting ENGINE           │  ← MUST be correct
                 │  COA · double-entry rules · balance check ·  │    (aturan terstruktur ibu Tere)
                 │  tax (PPN) math · validation                 │
                 └──────────────────────┬──────────────────────┘
                                        │ locks correctness
                                        ▼
                              ✅ correct, balanced journal
```

## 🇬🇧 Why layered?
Accounting needs **precision** — an LLM alone can hallucinate numbers, which is dangerous for
financial data. A rules engine alone is rigid and can't understand messy human language.
So we combine both:

- **Layer 1 — `core/` engine (deterministic):** the math and rules that must be *exactly* right —
  chart of accounts, double-entry (debit = credit), tax (PPN), validation. This is **code**, not a
  prediction. Reusable across every product (edge AI, UMKM app, enterprise, SPI).
- **Layer 2 — AI model (small, on-device):** the fuzzy part — understanding "beli bensin 50rb",
  mapping to the right account, categorization, Q&A, and **real-world judgment** on ambiguous cases.

**The AI proposes; the engine locks correctness.** If the AI suggests an unbalanced journal, the
engine rejects it. That gives us AI's flexibility *with* accounting's precision.

## 🇮🇩 Kenapa berlapis?
Akuntansi butuh **presisi** — LLM sendirian bisa mengarang angka (bahaya untuk data keuangan).
Rule-engine sendirian kaku dan tak paham bahasa manusia. Maka kita gabungkan:

- **Lapis 1 — engine `core/` (deterministik):** matematika & aturan yang wajib *pasti* benar —
  COA, double-entry (debit = kredit), pajak (PPN), validasi. Ini **kode**, bukan tebakan. Reusable
  untuk semua produk (edge AI, app UMKM, enterprise, SPI).
- **Lapis 2 — model AI (kecil, di perangkat):** bagian "fuzzy" — memahami "beli bensin 50rb",
  memetakan akun, kategorisasi, tanya-jawab, dan **judgment** untuk kasus ambigu.

**AI mengusulkan; engine mengunci kebenaran.** Kalau AI mengusulkan jurnal tak balance, engine
menolaknya. Jadi kita dapat fleksibilitas AI *dengan* presisi akuntansi.

## How Ibu Tere's expertise maps to each layer / Peta ilmu ibu Tere
| Ilmu ibu Tere | Masuk ke |
|---|---|
| COA, aturan double-entry, tarif pajak, format laporan (terstruktur) | **Layer 1 — engine (`core/`)** sebagai kode/konfig |
| Interpretasi transaksi berantakan, gray area, judgment adaptif, kesalahan umum (tacit) | **Layer 2 — data latih AI** (`data/`, tipe `reasoning`) |

→ Keahlian 20 tahun ibu Tere menghidupkan **kedua lapis**.
