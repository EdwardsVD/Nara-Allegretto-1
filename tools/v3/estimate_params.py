"""Perkiraan token & kesesuaian dataset untuk model +-50 juta parameter.

Menghitung dari berkas JSONL yang nyata:
- jumlah baris/byte, karakter & kata pada konten user+assistant saja,
- token regex gaya `pilot_train_check.py` (kata + tanda baca),
- rentang perkiraan token subword (BPE) bahasa Indonesia: karakter konten
  dibagi 3,2 s.d. 4,2 karakter per token (rentang kasar yang dinyatakan
  TERBUKA sebagai asumsi, bukan angka pasti),
- rasio token per parameter per epoch untuk target 50 juta parameter,
- satu contoh arsitektur decoder-only yang jumlah parameternya dihitung
  persis dengan rumus dan hasilnya +-50 juta (embedding terikat/tied).
"""
from __future__ import annotations

import argparse
import json
import os
import re

TOKEN_RE = re.compile(r"```[a-zA-Z0-9_+-]*|\n|[A-Za-zÀ-ÿ0-9_]+|[^\sA-Za-z0-9_]")


def count_params(vocab: int, ctx: int, d_model: int, n_layer: int, d_ff: int) -> dict:
    """Hitung parameter transformer decoder dengan embedding output terikat."""
    token_emb = vocab * d_model
    pos_emb = ctx * d_model
    per_layer_weights = 12 * d_model * d_model if d_ff == 4 * d_model else (
        4 * d_model * d_model + 2 * d_model * d_ff
    )
    # bias: qkv 3d + proj d + mlp (d_ff + d) dan 2 LayerNorm (masing-masing 2d)
    per_layer_bias_ln = (3 * d_model + d_model) + (d_ff + d_model) + 4 * d_model
    per_layer = per_layer_weights + per_layer_bias_ln
    final_ln = 2 * d_model
    total = token_emb + pos_emb + n_layer * per_layer + final_ln
    return {
        "vocab": vocab,
        "context": ctx,
        "d_model": d_model,
        "n_layer": n_layer,
        "d_ff": d_ff,
        "token_embedding": token_emb,
        "position_embedding": pos_emb,
        "per_layer_total": per_layer,
        "total_params": total,
        "total_params_million": round(total / 1_000_000, 2),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default="Nara-Allegretto-3.jsonl")
    parser.add_argument("--target-params", type=int, default=50_000_000)
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    rows = 0
    content_chars = 0
    words = 0
    regex_tokens = 0
    with open(args.path, encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            rows += 1
            for msg in rec["messages"]:
                text = msg["content"]
                content_chars += len(text)
                words += len(text.split())
                regex_tokens += len(TOKEN_RE.findall(text))
    size = os.path.getsize(args.path)
    bpe_low = round(content_chars / 4.2)
    bpe_high = round(content_chars / 3.2)
    bpe_mid = round((bpe_low + bpe_high) / 2)
    arch = count_params(vocab=8192, ctx=512, d_model=560, n_layer=12, d_ff=2240)

    report = {
        "file": args.path,
        "rows": rows,
        "size_bytes": size,
        "size_mib": round(size / (1024 * 1024), 2),
        "size_mb_decimal": round(size / 1_000_000, 2),
        "content_chars_user_assistant": content_chars,
        "content_words": words,
        "regex_tokens_word_punct": regex_tokens,
        "estimated_subword_tokens": {
            "assumption_chars_per_token": "3.2-4.2 (rentang kasar bahasa Indonesia)",
            "low": bpe_low,
            "mid": bpe_mid,
            "high": bpe_high,
        },
        "target_params": args.target_params,
        "tokens_per_param_per_epoch_mid": round(bpe_mid / args.target_params, 3),
        "note": (
            "Dataset 100 MB-class ini cocok untuk model +-50 juta parameter yang "
            "dilatih BANYAK epoch (multi-epoch) sambil dipantau validation loss-nya; "
            "ia bukan porsi satu epoch ala Chinchilla (20 token/parameter akan butuh "
            "+-1 miliar token unik). Angka token subword adalah perkiraan rentang, "
            "bukan hasil tokenizer tertentu."
        ),
        "example_architecture_tied_embedding": arch,
        "example_weight_file_size": {
            "fp16_mb_decimal": round(arch["total_params"] * 2 / 1_000_000, 1),
            "int8_mb_decimal": round(arch["total_params"] * 1 / 1_000_000, 1),
            "note": "perkiraan kasar ukuran bobot saja, belum termasuk metadata/format berkas",
        },
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
