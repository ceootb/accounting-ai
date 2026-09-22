# Training

Turn a small, permissive base model into the accounting SLM by fine-tuning it on the
examples in [`../data`](../data) with LoRA/QLoRA.

The model is only one half of the system. It **proposes** journal entries, COA mappings
and answers; the deterministic engine in [`../core`](../core) **locks correctness** —
rejecting anything that does not balance or references an unknown account
(see [`../ARCHITECTURE.md`](../ARCHITECTURE.md)). Fine-tuning makes the proposals better;
it never removes the engine check.

## Recipe

- **Base model:** `Qwen/Qwen2.5-1.5B-Instruct` — Apache-2.0, multilingual (includes
  Indonesian), strong for its size. Small on purpose: cheap, private, on-device friendly.
  Bump to `Qwen2.5-3B-Instruct` for more quality. Configured in [`config.yaml`](config.yaml).
- **Method:** QLoRA (4-bit) SFT over the chat-formatted dataset.
- **Data:** every `../data/*.jsonl` record `{task,instruction,input,output,lang,standard}`
  becomes a system/user/assistant turn. The system prompt states the balance rule.

## Steps

```bash
pip install -r requirements.txt

# 1) build build/train.jsonl + build/val.jsonl from ../data
python prepare_data.py --data ../data --out build --val 0.1

# 2) fine-tune (needs a CUDA GPU for 4-bit; ~one 24GB card is enough for 1.5B)
python train_lora.py --config config.yaml
# -> adapter in out/accounting-slm-qlora
```

On CPU / Apple Silicon set `train.quant: none` in `config.yaml` (slow — this recipe
targets a small rented GPU). Trained adapters/weights are published separately on
Hugging Face; this folder holds the code + config only.

## Contributing

The fastest way to improve the model is **more and better data**, not bigger models.
Add examples to `../data/*.jsonl` (anonymised, following the schema) and open a PR.
Scripts and config improvements are welcome too.
