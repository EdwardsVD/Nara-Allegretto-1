"""Uji latih cepat skala kecil (Point 7: ~500 per kategori, EPOCHS=2).

Melatih model bahasa kondisional ringan (SGD log-linear atas fitur konteks
bigram + kata kunci prompt user) selama EPOCHS=2 pada pilot dataset untuk
memastikan:
1. Format JSONL terbaca bersih tanpa error tokenisasi.
2. Loss latih & validasi turun sehat dari Epoch 0 -> Epoch 1 -> Epoch 2.
3. Generasi/prediksi sampel menjaga gaya `aku/kamu`, sapaan santai, blok kode
   pendek, dan kejujuran batas pengetahuan sebelum dataset digenerate penuh.
"""
from __future__ import annotations

import argparse
import json
import math
import random
import re
from collections import Counter, defaultdict

TOKEN_RE = re.compile(r"```[a-zA-Z0-9_+-]*|\n|[A-Za-zÀ-ÿ0-9_]+|[^\sA-Za-z0-9_]")


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text)[:180]


def load_pairs(path: str) -> list[tuple[list[str], list[str], str, str]]:
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            q = obj["messages"][0]["content"]
            a = obj["messages"][1]["content"]
            rows.append((tokenize(q.lower()), tokenize(a) + ["<eos>"], q, a))
    return rows


def run_pilot_training(path: str, epochs: int = 2, lr: float = 0.28, seed: int = 42) -> dict:
    rng = random.Random(seed)
    data = load_pairs(path)
    rng.shuffle(data)

    split = int(len(data) * 0.9)
    train_set = data[:split]
    val_set = data[split:]

    # Bangun kosakata kandidat per pasangan (prev2, prev1) + fallback prev1
    vocab_freq: Counter[str] = Counter()
    tri_candidates: dict[tuple[str, str], set[str]] = defaultdict(set)
    bi_candidates: dict[str, set[str]] = defaultdict(set)
    for _, a_toks, _, _ in train_set:
        p2, p1 = "<bos2>", "<bos>"
        for tok in a_toks:
            vocab_freq[tok] += 1
            tri_candidates[(p2, p1)].add(tok)
            bi_candidates[p1].add(tok)
            p2, p1 = p1, tok

    top_global = [w for w, _ in vocab_freq.most_common(48)]

    cand_cache: dict[tuple[str, str], list[str]] = {}

    def get_cands(p2: str, p1: str) -> list[str]:
        cached = cand_cache.get((p2, p1))
        if cached is not None:
            return cached
        base = list(tri_candidates.get((p2, p1), ()))
        if len(base) < 16:
            for b in bi_candidates.get(p1, ()):
                if b not in base:
                    base.append(b)
                if len(base) >= 24:
                    break
        for g in top_global[:24]:
            if g not in base and len(base) < 32:
                base.append(g)
        res = base[:36]
        cand_cache[(p2, p1)] = res
        return res

    # Bobot log-linear: unigram bias, transisi bigram, trigram, & kata kunci prompt
    bias_w: dict[str, float] = defaultdict(float)
    bi_w: dict[tuple[str, str], float] = defaultdict(float)
    tri_w: dict[tuple[str, str, str], float] = defaultdict(float)
    ctx_w: dict[tuple[str, str], float] = defaultdict(float)

    STOP_Q = {"di", "ke", "yang", "apa", "gimana", "dong", "ya", "itu", "ini", "untuk", "buat"}

    def q_features(q_toks: list[str]) -> list[str]:
        kws = [t for t in q_toks if len(t) > 1 and t not in STOP_Q]
        return (kws or q_toks)[:8]

    def eval_loss(dataset: list[tuple[list[str], list[str], str, str]]) -> float:
        total_nll = 0.0
        total_tok = 0
        for q_toks, a_toks, _, _ in dataset[:250]:
            q_keys = q_features(q_toks)
            p2, p1 = "<bos2>", "<bos>"
            for target in a_toks[:45]:
                cands = get_cands(p2, p1)
                if target not in cands:
                    cands = cands + [target]
                logits = []
                for c in cands:
                    s = bias_w[c] + bi_w[(p1, c)] + tri_w[(p2, p1, c)]
                    for qk in q_keys:
                        s += ctx_w[(qk, c)]
                    logits.append(s)
                m = max(logits)
                exps = [math.exp(x - m) for x in logits]
                z = sum(exps)
                t_idx = cands.index(target)
                total_nll += -(logits[t_idx] - m - math.log(z))
                total_tok += 1
                p2, p1 = p1, target
        return round(total_nll / max(total_tok, 1), 4)

    history = [{"epoch": 0, "train_loss": eval_loss(train_set[:250]), "val_loss": eval_loss(val_set)}]

    for ep in range(1, epochs + 1):
        rng.shuffle(train_set)
        step_lr = lr / (1.0 + 0.25 * (ep - 1))
        for q_toks, a_toks, _, _ in train_set:
            q_keys = q_features(q_toks)
            p2, p1 = "<bos2>", "<bos>"
            for target in a_toks[:45]:
                cands = get_cands(p2, p1)
                if target not in cands:
                    cands = cands + [target]
                logits = []
                for c in cands:
                    s = bias_w[c] + bi_w[(p1, c)] + tri_w[(p2, p1, c)]
                    for qk in q_keys:
                        s += ctx_w[(qk, c)]
                    logits.append(s)
                m = max(logits)
                exps = [math.exp(x - m) for x in logits]
                z = sum(exps)
                for idx, c in enumerate(cands):
                    prob = exps[idx] / z
                    grad = (1.0 if c == target else 0.0) - prob
                    if abs(grad) < 1e-4:
                        continue
                    delta = step_lr * grad
                    bias_w[c] += delta * 0.15
                    bi_w[(p1, c)] += delta * 0.7
                    tri_w[(p2, p1, c)] += delta * 1.1
                    for qk in q_keys:
                        ctx_w[(qk, c)] += delta * 0.45
                p2, p1 = p1, target
        history.append(
            {
                "epoch": ep,
                "train_loss": eval_loss(train_set[:250]),
                "val_loss": eval_loss(val_set),
            }
        )

    # Uji dekode dengan repetition penalty ringan
    def greedy_generate(prompt: str, max_tokens: int = 38) -> str:
        q_keys = q_features(tokenize(prompt.lower()))
        p2, p1 = "<bos2>", "<bos>"
        out: list[str] = []
        seen_counts: Counter[str] = Counter()
        for _ in range(max_tokens):
            cands = get_cands(p2, p1)
            best_tok = "<eos>"
            best_s = -1e9
            for c in cands:
                s = bias_w[c] + bi_w[(p1, c)] + tri_w[(p2, p1, c)]
                for qk in q_keys:
                    s += ctx_w[(qk, c)]
                if seen_counts[c] > 0 and c not in ("\n", ".", ","):
                    s -= 1.2 * seen_counts[c]
                if s > best_s:
                    best_s = s
                    best_tok = c
            if best_tok == "<eos>":
                break
            out.append(best_tok)
            seen_counts[best_tok] += 1
            p2, p1 = p1, best_tok
        return " ".join(out).replace(" ,", ",").replace(" .", ".").replace(" !", "!")

    test_prompts = [
        "halo nara",
        "siapa kamu sebenarnya?",
        "contoh kode Python menjumlahkan dua angka",
        "di kotaku sekarang hujan nggak?",
        "berapa hasil 24 + 18?",
    ]
    generations = {p: greedy_generate(p) for p in test_prompts}

    return {
        "pilot_file": path,
        "total_rows": len(data),
        "train_rows": len(train_set),
        "val_rows": len(val_set),
        "epochs": epochs,
        "loss_decreased": (
            history[-1]["train_loss"] < history[0]["train_loss"]
            and history[-1]["val_loss"] < history[0]["val_loss"]
        ),
        "history": history,
        "sample_generations": generations,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pilot_jsonl")
    parser.add_argument("--epochs", type=int, default=2)
    args = parser.parse_args()

    res = run_pilot_training(args.pilot_jsonl, epochs=args.epochs)
    print(json.dumps(res, ensure_ascii=False, indent=2))
    if not res["loss_decreased"]:
        raise SystemExit("Loss tidak turun pada pilot training check!")


if __name__ == "__main__":
    main()
