#!/usr/bin/env python3
"""QLoRA supervised fine-tune for the accounting SLM.

Reads config.yaml, trains a LoRA adapter on build/{train,val}.jsonl (produced by
prepare_data.py), and saves the adapter to output_dir.

    python prepare_data.py           # build the dataset first
    python train_lora.py --config config.yaml

Needs a CUDA GPU for 4-bit QLoRA. On CPU/Apple Silicon set train.quant: none and
expect it to be slow — this recipe targets a small rented GPU (e.g. one 24GB card).

The model only PROPOSES entries. Correctness is locked by the deterministic engine
in ../core (JournalEntry.assert_valid): reject anything that does not balance or
references an unknown account. See ../ARCHITECTURE.md.
"""
import json, argparse
import yaml


def load_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.yaml")
    a = ap.parse_args()
    cfg = yaml.safe_load(open(a.config))

    import torch
    from datasets import Dataset
    from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
    from peft import LoraConfig
    from trl import SFTTrainer, SFTConfig

    tok = AutoTokenizer.from_pretrained(cfg["base_model"])
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token

    def fmt(ex):
        return {"text": tok.apply_chat_template(ex["messages"], tokenize=False)}

    train_ds = Dataset.from_list(load_jsonl(cfg["data"]["train"])).map(fmt)
    val_ds = Dataset.from_list(load_jsonl(cfg["data"]["val"])).map(fmt)

    qcfg = None
    if str(cfg["train"].get("quant")) == "4bit":
        qcfg = BitsAndBytesConfig(
            load_in_4bit=True, bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16, bnb_4bit_use_double_quant=True)

    model = AutoModelForCausalLM.from_pretrained(
        cfg["base_model"], quantization_config=qcfg,
        torch_dtype=torch.bfloat16, device_map="auto")

    lora = LoraConfig(
        r=cfg["lora"]["r"], lora_alpha=cfg["lora"]["alpha"],
        lora_dropout=cfg["lora"]["dropout"],
        target_modules=cfg["lora"]["target_modules"], task_type="CAUSAL_LM")

    args = SFTConfig(
        output_dir=cfg["output_dir"],
        num_train_epochs=cfg["train"]["epochs"],
        learning_rate=float(cfg["train"]["lr"]),
        per_device_train_batch_size=cfg["train"]["batch_size"],
        gradient_accumulation_steps=cfg["train"]["grad_accum"],
        max_seq_length=cfg["train"]["max_seq_len"],
        warmup_ratio=cfg["train"]["warmup_ratio"],
        bf16=cfg["train"].get("bf16", True),
        logging_steps=10, save_strategy="epoch", eval_strategy="epoch",
        dataset_text_field="text")

    trainer = SFTTrainer(
        model=model, args=args, train_dataset=train_ds, eval_dataset=val_ds,
        peft_config=lora, processing_class=tok)
    trainer.train()
    trainer.save_model(cfg["output_dir"])
    print("adapter saved ->", cfg["output_dir"])


if __name__ == "__main__":
    main()
