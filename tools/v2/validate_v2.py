"""Validator wajib sebelum training untuk dataset Nara-Allegretto-2 (Point 6).

Pemeriksaan ketat per baris:
1. UTF-8 murni & diakhiri newline `\n`.
2. JSON valid, key tepat `{"messages"}`, 2 item dengan role `["user", "assistant"]`.
3. Isi `user` & `assistant` bertipe string, tidak kosong, tanpa spasi awal/akhir,
   tanpa `\r` atau `\t`.
4. Bebas karakter rusak / mojibake (seperti `Ã©`, `â€™`, `Â `, `\ufffd`, control char).
5. Bebas duplikat pertanyaan setelah `lowercase + trim` maupun `norm_key`.
6. Bebas duplikat jawaban setelah `lowercase + trim` maupun `norm_key`.
7. Panjang pertanyaan & jawaban berada dalam batas wajar model kecil.
8. Konsistensi gaya bahasa (`aku/kamu`, tanpa `saya/anda`, tanpa nama lama
   `Nara Ai`/`Nara N1` atau pengakuan diri sebagai `Nara-Allegretto-1`).
9. Semua persamaan aritmetika pada jawaban dihitung ulang dan diverifikasi.
10. Semua blok kode berpagar (```lang ... ```) dicek maksimal 8 baris dan diuji
    sintaksnya (`ast.parse`, `node --check`, TypeScript strip, HTML, CSS, SQL, Bash, JSON).
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS_DIR = os.path.dirname(HERE)
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

from v2.code_verifier import MAX_CODE_LINES, CodeVerifier  # noqa: E402
from v2.core_v2 import (  # noqa: E402
    BAD_STYLE_RE,
    OLD_NAME_RE,
    OLD_V1_SELF_RE,
    has_mojibake,
    is_mostly_english_prose,
    norm_key,
    strip_code_blocks,
    trim_lower_key,
)

EQ_RE = re.compile(r"([0-9][0-9. /]*(?:[x:+\-]\s*[0-9][0-9. /]*)+)=\s*([0-9][0-9.]*)")
FENCE_RE = re.compile(r"```([a-zA-Z0-9_+-]+)\n(.*?)\n```", re.DOTALL)


def _to_int(text: str) -> int:
    return int(text.replace(".", ""))


def validate_file(
    path: str,
    *,
    max_q_len: int = 300,
    min_a_len: int = 30,
    max_a_len: int = 720,
    check_code: bool = True,
) -> dict:
    errors: list[str] = []
    seen_q_trim: dict[str, int] = {}
    seen_q_norm: dict[str, int] = {}
    seen_a_trim: dict[str, int] = {}
    seen_a_norm: dict[str, int] = {}

    total_rows = 0
    line_bytes: list[int] = []
    a_lengths: list[int] = []
    q_lengths: list[int] = []
    eq_checked = 0
    eq_bad = 0
    code_blocks_checked = 0
    code_blocks_bad = 0

    verifier = CodeVerifier(max_lines=MAX_CODE_LINES)
    try:
        with open(path, "rb") as raw:
            for lineno, raw_line in enumerate(raw, start=1):
                total_rows += 1
                line_bytes.append(len(raw_line))
                if not raw_line.endswith(b"\n"):
                    errors.append(f"baris {lineno}: tidak diakhiri newline")
                try:
                    line = raw_line.decode("utf-8")
                except UnicodeDecodeError as exc:
                    errors.append(f"baris {lineno}: bukan UTF-8 valid ({exc})")
                    continue
                if not line.strip():
                    errors.append(f"baris {lineno}: baris kosong")
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError as exc:
                    errors.append(f"baris {lineno}: JSON invalid ({exc})")
                    continue

                if set(obj.keys()) != {"messages"}:
                    errors.append(f"baris {lineno}: key objek salah {list(obj.keys())}")
                    continue
                msgs = obj["messages"]
                if not isinstance(msgs, list) or len(msgs) != 2:
                    errors.append(f"baris {lineno}: messages harus berisi 2 item")
                    continue
                if [m.get("role") for m in msgs] != ["user", "assistant"]:
                    errors.append(f"baris {lineno}: urutan role harus ['user', 'assistant']")
                    continue

                q = msgs[0].get("content")
                a = msgs[1].get("content")
                if not isinstance(q, str) or not isinstance(a, str):
                    errors.append(f"baris {lineno}: content bukan string")
                    continue
                if not q.strip() or not a.strip():
                    errors.append(f"baris {lineno}: content kosong")
                    continue
                if q != q.strip() or a != a.strip():
                    errors.append(f"baris {lineno}: ada spasi di awal/akhir content")
                if any(ch in q + a for ch in "\r\t"):
                    errors.append(f"baris {lineno}: mengandung CR atau tab mentah")
                if has_mojibake(q) or has_mojibake(a):
                    errors.append(f"baris {lineno}: terdeteksi karakter rusak/mojibake")
                if BAD_STYLE_RE.search(q) or BAD_STYLE_RE.search(a):
                    errors.append(f"baris {lineno}: menggunakan kata formal saya/anda")
                if OLD_NAME_RE.search(q) or OLD_NAME_RE.search(a):
                    errors.append(f"baris {lineno}: menggunakan nama lama Nara Ai/Nara N1")
                if OLD_V1_SELF_RE.search(a):
                    errors.append(f"baris {lineno}: menyebut diri sebagai Nara-Allegretto-1")
                if "inggris" not in q.lower() and is_mostly_english_prose(a):
                    errors.append(f"baris {lineno}: prosa jawaban terlalu bahasa Inggris")

                if not (1 <= len(q) <= max_q_len):
                    errors.append(f"baris {lineno}: panjang pertanyaan di luar batas ({len(q)})")
                if not (min_a_len <= len(a) <= max_a_len):
                    errors.append(f"baris {lineno}: panjang jawaban di luar batas ({len(a)})")

                q_lengths.append(len(q))
                a_lengths.append(len(a))

                qt = trim_lower_key(q)
                qn = norm_key(q)
                at = trim_lower_key(a)
                an = norm_key(a)

                if qt in seen_q_trim:
                    errors.append(f"baris {lineno}: duplikat pertanyaan (lower+trim) dgn baris {seen_q_trim[qt]}")
                else:
                    seen_q_trim[qt] = lineno

                if qn in seen_q_norm:
                    errors.append(f"baris {lineno}: duplikat pertanyaan (norm) dgn baris {seen_q_norm[qn]}")
                else:
                    seen_q_norm[qn] = lineno

                if at in seen_a_trim:
                    errors.append(f"baris {lineno}: duplikat jawaban (lower+trim) dgn baris {seen_a_trim[at]}")
                else:
                    seen_a_trim[at] = lineno

                if an in seen_a_norm:
                    errors.append(f"baris {lineno}: duplikat jawaban (norm) dgn baris {seen_a_norm[an]}")
                else:
                    seen_a_norm[an] = lineno

                # Cek persamaan aritmetika pada teks non-kode
                prose_only = strip_code_blocks(a)
                for ma in EQ_RE.finditer(prose_only):
                    expr = ma.group(1).strip()
                    if not any(op in expr for op in ("+", "-", "x", ":")):
                        continue
                    if ":" in expr and not re.search(r"\s:\s", expr):
                        continue
                    try:
                        py_expr = expr.replace("x", "*").replace(":", "/")
                        py_expr = re.sub(r"(\d)\.(\d{3})", r"\1\2", py_expr)
                        py_expr = re.sub(r"(\d)\.(\d{3})", r"\1\2", py_expr)
                        if not re.fullmatch(r"[0-9./+*\-() ]+", py_expr):
                            continue
                        expected = eval(py_expr, {"__builtins__": {}}, {})
                    except Exception:
                        continue
                    if isinstance(expected, float) and abs(expected - round(expected)) > 1e-6:
                        continue
                    eq_checked += 1
                    try:
                        actual = _to_int(ma.group(2))
                    except ValueError:
                        continue
                    if abs(float(expected) - actual) > 1e-6:
                        eq_bad += 1
                        errors.append(
                            f"baris {lineno}: persamaan salah `{ma.group(0)}` (seharusnya {expected})"
                        )

                # Cek setiap blok kode berpagar
                if check_code and "```" in a:
                    if a.count("```") % 2 != 0:
                        code_blocks_bad += 1
                        errors.append(f"baris {lineno}: pagar kode ``` tidak berpasangan")
                        continue
                    for fm in FENCE_RE.finditer(a):
                        lang = fm.group(1).lower()
                        snippet = fm.group(2)
                        code_blocks_checked += 1
                        c_lines = snippet.strip("\n").split("\n")
                        if len(c_lines) > MAX_CODE_LINES:
                            code_blocks_bad += 1
                            errors.append(
                                f"baris {lineno}: kode `{lang}` {len(c_lines)} baris (> {MAX_CODE_LINES})"
                            )
                            continue
                        ok = True
                        reason = ""
                        if lang in ("python", "py"):
                            try:
                                ast.parse(snippet)
                            except SyntaxError as exc:
                                ok, reason = False, str(exc)
                        elif lang in ("javascript", "js"):
                            ok, reason = verifier.verify_js_or_ts(snippet, lang="js", run=False)
                        elif lang in ("typescript", "ts"):
                            ok, reason = verifier.verify_js_or_ts(snippet, lang="ts", run=False)
                        elif lang == "html":
                            ok, reason = verifier.verify_html(snippet)
                        elif lang == "css":
                            ok, reason = verifier.verify_css(snippet)
                        elif lang == "sql":
                            ok, reason = verifier.verify_sql(snippet)
                        elif lang in ("bash", "sh"):
                            ok, reason = verifier.verify_bash(snippet)
                        elif lang == "json":
                            ok, reason = verifier.verify_json(snippet)
                        if not ok:
                            code_blocks_bad += 1
                            errors.append(f"baris {lineno}: kode `{lang}` gagal uji ({reason})")

        node_ok, node_err = verifier.flush_node_cli_check()
        if not node_ok:
            code_blocks_bad += 1
            errors.append(f"node --check gagal: {node_err}")
    finally:
        verifier.close()

    line_bytes.sort()
    a_lengths.sort()
    size_bytes = sum(line_bytes)
    report = {
        "file": path,
        "rows": total_rows,
        "size_bytes": size_bytes,
        "size_mib": round(size_bytes / (1024 * 1024), 2),
        "size_mb_decimal": round(size_bytes / 1_000_000, 2),
        "max_line_bytes": line_bytes[-1] if line_bytes else 0,
        "answer_len_min": a_lengths[0] if a_lengths else 0,
        "answer_len_median": a_lengths[len(a_lengths) // 2] if a_lengths else 0,
        "answer_len_mean": round(sum(a_lengths) / max(len(a_lengths), 1), 1),
        "answer_len_max": a_lengths[-1] if a_lengths else 0,
        "equations_checked": eq_checked,
        "equations_bad": eq_bad,
        "code_blocks_checked": code_blocks_checked,
        "code_blocks_bad": code_blocks_bad,
        "issues_count": len(errors),
        "sample_issues": errors[:10],
    }
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+")
    args = parser.parse_args()

    any_failed = False
    for p in args.paths:
        rep = validate_file(p)
        print(json.dumps(rep, ensure_ascii=False, indent=2))
        if rep["issues_count"] > 0:
            any_failed = True
    if any_failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
