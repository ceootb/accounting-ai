#!/usr/bin/env python3
"""Merge every data/*.jsonl example into a chat-format SFT dataset.

Each source record has the shape:
    {"task","instruction","input","output","lang","standard"}
and is turned into a system/user/assistant message triple. The system prompt
reminds the model of the core rule the deterministic engine (../core) enforces:
every journal entry must balance.

Usage:
    python prepare_data.py --data ../data --out build --val 0.1
"""
import json, glob, os, argparse

SYSTEM = (
    "You are an accounting assistant for Indonesian and general (IFRS) bookkeeping. "
    "Produce correct double-entry journal entries, chart-of-accounts mappings, and "
    "bookkeeping answers. Follow PSAK for Indonesian (lang=id) items and general/IFRS "
    "otherwise. Every journal entry MUST balance: total debit = total credit."
)


def to_chat(r):
    user = r["instruction"] + (("\n\n" + r["input"]) if r.get("input") else "")
    return {"messages": [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": user},
        {"role": "assistant", "content": r["output"]},
    ]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="../data")
    ap.add_argument("--out", default="build")
    ap.add_argument("--val", type=float, default=0.1, help="validation fraction")
    a = ap.parse_args()

    rows = []
    for f in sorted(glob.glob(os.path.join(a.data, "*.jsonl"))):
        for ln in open(f, encoding="utf-8"):
            ln = ln.strip()
            if not ln:
                continue
            try:
                r = json.loads(ln)
            except Exception:
                continue
            if r.get("instruction") and r.get("output"):
                rows.append(to_chat(r))

    # deterministic split (no random seed drift across runs)
    n = len(rows)
    k = max(1, int(n * a.val)) if n else 0
    val, train = rows[:k], rows[k:]

    os.makedirs(a.out, exist_ok=True)
    for name, part in (("train", train), ("val", val)):
        with open(os.path.join(a.out, f"{name}.jsonl"), "w", encoding="utf-8") as w:
            for r in part:
                w.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"total={n} train={len(train)} val={len(val)} -> {a.out}/")


if __name__ == "__main__":
    main()
