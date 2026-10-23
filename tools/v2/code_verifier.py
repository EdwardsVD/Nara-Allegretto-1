"""Penguji kode otomatis sebelum masuk dataset Nara-Allegretto-2.

Aturan keras (Point 3):
- Maksimal 8 baris kode per cuplikan (agar model kecil tidak kewalahan).
- Python: ast.parse() + eksekusi langsung & cocokkan output (bila eksekusi murni).
- JavaScript: node --check + eksekusi vm & cocokkan console.log (bila non-DOM).
- TypeScript: stripTypeScriptTypes (Node 22) + node --check + eksekusi vm.
- C++ / C: kompilasi g++ / gcc sungguhan + verifikasi output bila diminta.
- SQL: eksekusi sungguhan di sqlite3 (:memory:).
- HTML: validasi struktur tag pembuka/penutup bersarang ketat.
- CSS: validasi kurung kurawal, properti, titik dua, dan titik koma.
- Bash: bash -n.
- JSON: json.loads().
Cuplikan yang gagal otomatis dibuang.
"""
from __future__ import annotations

import ast
import contextlib
import html.parser
import io
import json
import os
import re
import sqlite3
import subprocess
import tempfile

MAX_CODE_LINES = 8

VOID_HTML_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}

VALID_HTML_TAGS = VOID_HTML_TAGS | {
    "html", "head", "title", "body", "header", "nav", "main", "section",
    "article", "aside", "footer", "div", "span", "p", "h1", "h2", "h3",
    "h4", "h5", "h6", "a", "ul", "ol", "li", "dl", "dt", "dd", "table",
    "thead", "tbody", "tfoot", "tr", "th", "td", "caption", "form",
    "label", "button", "select", "option", "textarea", "fieldset",
    "legend", "strong", "em", "b", "i", "u", "small", "mark", "sub",
    "sup", "code", "pre", "blockquote", "figure", "figcaption", "details",
    "summary", "dialog", "progress", "meter", "time", "audio", "video",
    "canvas", "svg", "circle", "rect", "style", "script",
}

KNOWN_CSS_PROPS = {
    "color", "background", "background-color", "background-image",
    "background-size", "background-position", "font-size", "font-family",
    "font-weight", "font-style", "line-height", "text-align",
    "text-decoration", "text-transform", "letter-spacing", "word-spacing",
    "margin", "margin-top", "margin-right", "margin-bottom", "margin-left",
    "padding", "padding-top", "padding-right", "padding-bottom", "padding-left",
    "border", "border-top", "border-right", "border-bottom", "border-left",
    "border-radius", "border-color", "border-width", "border-style",
    "width", "min-width", "max-width", "height", "min-height", "max-height",
    "display", "flex", "flex-direction", "flex-wrap", "justify-content",
    "align-items", "align-self", "gap", "row-gap", "column-gap",
    "grid-template-columns", "grid-template-rows", "place-items",
    "position", "top", "right", "bottom", "left", "z-index",
    "overflow", "overflow-x", "overflow-y", "opacity", "cursor",
    "box-shadow", "box-sizing", "transition", "transform", "list-style",
    "outline", "white-space", "object-fit", "aspect-ratio", "visibility",
}


class _StrictHTMLParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.errors: list[str] = []
        self.seen_tag = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        t = tag.lower()
        self.seen_tag = True
        if t not in VALID_HTML_TAGS:
            self.errors.append(f"tag tidak dikenal: {t}")
            return
        for k, _ in attrs:
            if not re.fullmatch(r"[a-zA-Z_:][a-zA-Z0-9_.:-]*", k):
                self.errors.append(f"atribut invalid: {k}")
        if t not in VOID_HTML_TAGS:
            self.stack.append(t)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        t = tag.lower()
        self.seen_tag = True
        if t not in VALID_HTML_TAGS:
            self.errors.append(f"tag tidak dikenal: {t}")

    def handle_endtag(self, tag: str) -> None:
        t = tag.lower()
        if t in VOID_HTML_TAGS:
            self.errors.append(f"void tag tidak boleh ditutup: {t}")
            return
        if not self.stack or self.stack[-1] != t:
            self.errors.append(f"tag penutup tidak cocok: </{t}> (stack={self.stack})")
            return
        self.stack.pop()


_NODE_HELPER_JS = r"""
const readline = require("node:readline");
const vm = require("node:vm");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const { execFileSync } = require("node:child_process");
const { stripTypeScriptTypes } = require("node:module");

const tmpFile = path.join(os.tmpdir(), `nara_node_check_${process.pid}.js`);

function formatVal(v) {
  if (typeof v === "string") return v;
  if (Array.isArray(v) || (v && typeof v === "object")) return JSON.stringify(v);
  return String(v);
}

const rl = readline.createInterface({ input: process.stdin, crlfDelay: Infinity });
rl.on("line", (line) => {
  if (!line.trim()) return;
  let req;
  try {
    req = JSON.parse(line);
  } catch (e) {
    process.stdout.write(JSON.stringify({ ok: false, err: "bad json" }) + "\n");
    return;
  }
  const { lang, code, run, useNodeCheck } = req;
  try {
    let jsCode = code;
    if (lang === "ts" || lang === "typescript") {
      jsCode = stripTypeScriptTypes(code);
    }
    if (useNodeCheck) {
      fs.writeFileSync(tmpFile, jsCode, "utf8");
      execFileSync(process.execPath, ["--check", tmpFile], { stdio: "pipe" });
    } else {
      new vm.Script(jsCode);
    }
    let out = "";
    if (run) {
      const logs = [];
      const sandbox = {
        console: {
          log: (...args) => logs.push(args.map(formatVal).join(" ")),
        },
        Math, Number, String, Boolean, Array, Object, JSON, Date, RegExp,
        Map, Set, Promise, parseInt, parseFloat, isNaN, isFinite,
      };
      vm.runInNewContext(jsCode, sandbox, { timeout: 250 });
      out = logs.join("\n").trim();
    }
    process.stdout.write(JSON.stringify({ ok: true, out }) + "\n");
  } catch (e) {
    process.stdout.write(JSON.stringify({ ok: false, err: String(e.message || e) }) + "\n");
  }
});
rl.on("close", () => {
  try { fs.unlinkSync(tmpFile); } catch (_) {}
});
"""


class CodeVerifier:
    """Penguji lintas bahasa pemrograman dengan statistik lulus/gagal."""

    def __init__(self, max_lines: int = MAX_CODE_LINES) -> None:
        self.max_lines = max_lines
        self.stats: dict[str, dict[str, int]] = {}
        self._node_proc: subprocess.Popen | None = None
        self._js_checked_batch: list[str] = []

    def _bump(self, lang: str, ok: bool) -> None:
        bucket = self.stats.setdefault(lang, {"passed": 0, "failed": 0})
        bucket["passed" if ok else "failed"] += 1

    def check_lines(self, code: str) -> bool:
        lines = code.strip("\n").split("\n")
        if not (1 <= len(lines) <= self.max_lines):
            return False
        if any(len(ln) > 92 for ln in lines):
            return False
        return True

    def verify_python(
        self,
        code: str,
        *,
        run: bool = True,
        expected_out: str | None = None,
    ) -> tuple[bool, str]:
        code = code.strip("\n")
        if not self.check_lines(code):
            self._bump("python", False)
            return False, "melebihi batas baris"
        try:
            tree = ast.parse(code)
        except SyntaxError as exc:
            self._bump("python", False)
            return False, f"SyntaxError: {exc}"

        if not run:
            self._bump("python", True)
            return True, ""

        buf = io.StringIO()
        ns: dict = {"__builtins__": __builtins__, "__name__": "__main__"}
        try:
            with contextlib.redirect_stdout(buf):
                exec(compile(tree, "<nara_py>", "exec"), ns, ns)
        except Exception as exc:
            self._bump("python", False)
            return False, f"RuntimeError: {exc}"

        out = buf.getvalue().strip()
        if expected_out is not None and out != str(expected_out).strip():
            self._bump("python", False)
            return False, f"output mismatch: got {out!r}, expected {expected_out!r}"

        self._bump("python", True)
        return True, out

    def _ensure_node(self) -> subprocess.Popen:
        if self._node_proc is None or self._node_proc.poll() is not None:
            self._node_proc = subprocess.Popen(
                ["node", "--no-warnings", "-e", _NODE_HELPER_JS],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
            )
        return self._node_proc

    def verify_js_or_ts(
        self,
        code: str,
        *,
        lang: str = "js",
        run: bool = True,
        expected_out: str | None = None,
        strict_node_check: bool = False,
    ) -> tuple[bool, str]:
        tag = "typescript" if lang in ("ts", "typescript") else "javascript"
        code = code.strip("\n")
        if not self.check_lines(code):
            self._bump(tag, False)
            return False, "melebihi batas baris"
        if tag == "typescript" and not re.search(
            r"(:\s*(string|number|boolean|void|unknown|any|[A-Z][A-Za-z0-9_]*)|interface\s+\w+|type\s+\w+\s*=|<[A-Z]\w*>)",
            code,
        ):
            self._bump(tag, False)
            return False, "tidak ada anotasi TypeScript"

        proc = self._ensure_node()
        assert proc.stdin is not None and proc.stdout is not None
        payload = json.dumps(
            {
                "lang": "ts" if tag == "typescript" else "js",
                "code": code,
                "run": run,
                "useNodeCheck": strict_node_check,
            }
        )
        proc.stdin.write(payload + "\n")
        proc.stdin.flush()
        resp_line = proc.stdout.readline()
        if not resp_line:
            self._bump(tag, False)
            return False, "node helper closed"
        resp = json.loads(resp_line)
        if not resp.get("ok"):
            self._bump(tag, False)
            return False, resp.get("err", "node error")

        out = resp.get("out", "")
        if run and expected_out is not None and out != str(expected_out).strip():
            self._bump(tag, False)
            return False, f"output mismatch: got {out!r}, expected {expected_out!r}"

        if tag == "javascript":
            self._js_checked_batch.append(code)
        self._bump(tag, True)
        return True, out

    def flush_node_cli_check(self) -> tuple[bool, str]:
        """Jalankan `node --check file.js` sungguhan untuk seluruh cuplikan JS."""
        if not self._js_checked_batch:
            return True, ""
        wrapped = "\n".join(
            f"(() => {{\n{snip}\n}})();" for snip in self._js_checked_batch
        )
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as tf:
            tf.write(wrapped + "\n")
            path = tf.name
        try:
            res = subprocess.run(["node", "--check", path], capture_output=True, text=True)
            if res.returncode != 0:
                return False, res.stderr.strip()
            return True, ""
        finally:
            if os.path.exists(path):
                os.unlink(path)

    def verify_html(self, code: str) -> tuple[bool, str]:
        code = code.strip("\n")
        if not self.check_lines(code):
            self._bump("html", False)
            return False, "melebihi batas baris"
        if "<" not in code or ">" not in code:
            self._bump("html", False)
            return False, "bukan HTML"
        parser = _StrictHTMLParser()
        try:
            parser.feed(code)
            parser.close()
        except Exception as exc:
            self._bump("html", False)
            return False, str(exc)
        if not parser.seen_tag or parser.errors or parser.stack:
            self._bump("html", False)
            return False, f"errors={parser.errors}, unclosed={parser.stack}"
        self._bump("html", True)
        return True, ""

    def verify_css(self, code: str) -> tuple[bool, str]:
        code = code.strip("\n")
        if not self.check_lines(code):
            self._bump("css", False)
            return False, "melebihi batas baris"
        cleaned = re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL).strip()
        if cleaned.count("{") == 0 or cleaned.count("{") != cleaned.count("}"):
            self._bump("css", False)
            return False, "kurung kurawal tidak seimbang"
        blocks = re.findall(r"([^{}]+)\{([^{}]+)\}", cleaned)
        if not blocks:
            self._bump("css", False)
            return False, "blok CSS kosong"
        for sel, body in blocks:
            if not sel.strip():
                self._bump("css", False)
                return False, "selektor kosong"
            decls = [d.strip() for d in body.strip().split(";") if d.strip()]
            if not decls or not body.strip().endswith(";"):
                self._bump("css", False)
                return False, "deklarasi harus diakhiri titik koma"
            for decl in decls:
                if ":" not in decl:
                    self._bump("css", False)
                    return False, f"deklarasi tanpa titik dua: {decl}"
                prop, val = [x.strip() for x in decl.split(":", 1)]
                if not (prop in KNOWN_CSS_PROPS or prop.startswith("--")):
                    self._bump("css", False)
                    return False, f"properti CSS tidak dikenal: {prop}"
                if not val or val.count("(") != val.count(")"):
                    self._bump("css", False)
                    return False, f"nilai CSS invalid: {val}"
        self._bump("css", True)
        return True, ""

    def verify_sql(
        self,
        code: str,
        *,
        setup_sql: str = "",
        expected_rows: list[tuple] | None = None,
    ) -> tuple[bool, str]:
        code = code.strip("\n")
        if not self.check_lines(code):
            self._bump("sql", False)
            return False, "melebihi batas baris"
        conn = sqlite3.connect(":memory:")
        try:
            cur = conn.cursor()
            cur.executescript(
                """
                CREATE TABLE siswa (id INTEGER PRIMARY KEY, nama TEXT, kelas TEXT, nilai INTEGER, umur INTEGER);
                INSERT INTO siswa VALUES (1, 'Budi', '10A', 85, 16), (2, 'Siti', '10A', 92, 15), (3, 'Raka', '10B', 78, 16), (4, 'Nadia', '10B', 95, 16);
                CREATE TABLE produk (id INTEGER PRIMARY KEY, nama TEXT, kategori TEXT, harga INTEGER, stok INTEGER);
                INSERT INTO produk VALUES (1, 'Buku Tulis', 'Alat Tulis', 5000, 40), (2, 'Pulpen', 'Alat Tulis', 3500, 80), (3, 'Tas Sekolah', 'Tas', 120000, 12), (4, 'Botol Minum', 'Aksesoris', 45000, 25);
                CREATE TABLE pegawai (id INTEGER PRIMARY KEY, nama TEXT, divisi TEXT, gaji INTEGER);
                INSERT INTO pegawai VALUES (1, 'Andi', 'IT', 8000000), (2, 'Dewi', 'HR', 6500000), (3, 'Fajar', 'IT', 9000000);
                """
            )
            if setup_sql:
                cur.executescript(setup_sql)
            statements = [s.strip() for s in code.split(";") if s.strip()]
            rows_out: list[tuple] = []
            for stmt in statements:
                cur.execute(stmt)
                if stmt.upper().lstrip().startswith("SELECT"):
                    rows_out = cur.fetchall()
            if expected_rows is not None and rows_out != expected_rows:
                self._bump("sql", False)
                return False, f"SQL output mismatch: {rows_out} != {expected_rows}"
            self._bump("sql", True)
            return True, repr(rows_out)
        except sqlite3.Error as exc:
            self._bump("sql", False)
            return False, f"SQLite error: {exc}"
        finally:
            conn.close()

    def verify_bash(self, code: str) -> tuple[bool, str]:
        code = code.strip("\n")
        if not self.check_lines(code):
            self._bump("bash", False)
            return False, "melebihi batas baris"
        res = subprocess.run(["bash", "-n"], input=code + "\n", capture_output=True, text=True)
        ok = res.returncode == 0
        self._bump("bash", ok)
        return ok, res.stderr.strip()

    def verify_json(self, code: str) -> tuple[bool, str]:
        code = code.strip("\n")
        if not self.check_lines(code):
            self._bump("json", False)
            return False, "melebihi batas baris"
        try:
            json.loads(code)
            self._bump("json", True)
            return True, ""
        except json.JSONDecodeError as exc:
            self._bump("json", False)
            return False, str(exc)

    def verify_cpp_batch(
        self, items: list[tuple[str, str | None]]
    ) -> list[tuple[bool, str]]:
        """Kompilasi dan jalankan sekumpulan cuplikan C++ sekaligus dengan g++."""
        results: list[tuple[bool, str]] = [False_res := (False, "init") for _ in items]
        del False_res
        valid_indices: list[int] = []
        for idx, (code, _) in enumerate(items):
            if not self.check_lines(code.strip("\n")):
                self._bump("cpp", False)
                results[idx] = (False, "melebihi batas baris")
            else:
                valid_indices.append(idx)

        CHUNK = 180
        for start in range(0, len(valid_indices), CHUNK):
            batch_ids = valid_indices[start : start + CHUNK]
            batch_ok = self._compile_and_run_cpp_chunk(items, batch_ids, results)
            if not batch_ok:
                for single_id in batch_ids:
                    self._compile_and_run_cpp_chunk(items, [single_id], results)
        return results

    def _compile_and_run_cpp_chunk(
        self,
        items: list[tuple[str, str | None]],
        batch_ids: list[int],
        results: list[tuple[bool, str]],
    ) -> bool:
        src_parts = [
            "#include <iostream>",
            "#include <sstream>",
            "#include <string>",
            "#include <vector>",
            "#include <algorithm>",
            "#include <numeric>",
            "#include <cmath>",
            "#include <map>",
            "#include <iomanip>",
            "using namespace std;",
        ]
        for idx in batch_ids:
            code, _ = items[idx]
            body_lines = []
            for ln in code.strip("\n").split("\n"):
                s = ln.strip()
                if s.startswith("#include") or s == "using namespace std;":
                    continue
                body_lines.append(ln)
            body = "\n".join(body_lines)
            body = re.sub(r"\bint\s+main\s*\([^)]*\)", "int run_snip()", body, count=1)
            src_parts.append(f"namespace ns_{idx} {{\n{body}\n}}")

        src_parts.append("int main() {")
        src_parts.append("  streambuf* orig = cout.rdbuf();")
        for idx in batch_ids:
            src_parts.append(f"  {{ ostringstream oss; cout.rdbuf(oss.rdbuf()); ns_{idx}::run_snip(); cout.rdbuf(orig); cout << \"__SNIP_{idx}__:\" << oss.str() << \"__END_{idx}__\\n\"; }}")
        src_parts.append("  return 0;\n}")

        full_cpp = "\n".join(src_parts)
        with tempfile.TemporaryDirectory() as tmpd:
            cpp_path = os.path.join(tmpd, "batch.cpp")
            bin_path = os.path.join(tmpd, "batch_bin")
            with open(cpp_path, "w", encoding="utf-8") as f:
                f.write(full_cpp)
            comp = subprocess.run(
                ["g++", "-std=c++17", "-O0", cpp_path, "-o", bin_path],
                capture_output=True,
                text=True,
            )
            if comp.returncode != 0:
                if len(batch_ids) == 1:
                    only = batch_ids[0]
                    self._bump("cpp", False)
                    results[only] = (False, comp.stderr.strip()[:200])
                return False

            run_res = subprocess.run([bin_path], capture_output=True, text=True, timeout=10)
            if run_res.returncode != 0:
                if len(batch_ids) == 1:
                    only = batch_ids[0]
                    self._bump("cpp", False)
                    results[only] = (False, "runtime crash")
                return False

            stdout = run_res.stdout
            for idx in batch_ids:
                _, expected = items[idx]
                m = re.search(rf"__SNIP_{idx}__:(.*?)__END_{idx}__", stdout, flags=re.DOTALL)
                out = m.group(1).strip() if m else ""
                if expected is not None and out != str(expected).strip():
                    self._bump("cpp", False)
                    results[idx] = (False, f"cpp mismatch: {out!r} != {expected!r}")
                else:
                    self._bump("cpp", True)
                    results[idx] = (True, out)
            return True

    def verify_c_batch(
        self, items: list[tuple[str, str | None]]
    ) -> list[tuple[bool, str]]:
        """Kompilasi dan jalankan cuplikan C dengan gcc -std=c11."""
        results: list[tuple[bool, str]] = [(False, "init") for _ in items]
        valid_indices: list[int] = []
        for idx, (code, _) in enumerate(items):
            if not self.check_lines(code.strip("\n")):
                self._bump("c", False)
                results[idx] = (False, "melebihi batas baris")
            else:
                valid_indices.append(idx)

        CHUNK = 180
        for start in range(0, len(valid_indices), CHUNK):
            batch_ids = valid_indices[start : start + CHUNK]
            if not self._compile_and_run_c_chunk(items, batch_ids, results):
                for single_id in batch_ids:
                    self._compile_and_run_c_chunk(items, [single_id], results)
        return results

    def _compile_and_run_c_chunk(
        self,
        items: list[tuple[str, str | None]],
        batch_ids: list[int],
        results: list[tuple[bool, str]],
    ) -> bool:
        src_parts = [
            "#include <stdio.h>",
            "#include <string.h>",
            "#include <stdlib.h>",
            "#include <math.h>",
        ]
        for idx in batch_ids:
            code, _ = items[idx]
            body_lines = [
                ln for ln in code.strip("\n").split("\n") if not ln.strip().startswith("#include")
            ]
            body = "\n".join(body_lines)
            body = re.sub(r"\bint\s+main\s*\([^)]*\)", f"int run_c_{idx}(void)", body, count=1)
            src_parts.append(body)

        src_parts.append("int main(void) {")
        for idx in batch_ids:
            src_parts.append(f'  printf("__CSNIP_{idx}__:"); fflush(stdout); run_c_{idx}(); printf("__CEND_{idx}__\\n"); fflush(stdout);')
        src_parts.append("  return 0;\n}")

        with tempfile.TemporaryDirectory() as tmpd:
            c_path = os.path.join(tmpd, "batch.c")
            bin_path = os.path.join(tmpd, "batch_c_bin")
            with open(c_path, "w", encoding="utf-8") as f:
                f.write("\n".join(src_parts))
            comp = subprocess.run(
                ["gcc", "-std=c11", "-O0", c_path, "-lm", "-o", bin_path],
                capture_output=True,
                text=True,
            )
            if comp.returncode != 0:
                if len(batch_ids) == 1:
                    self._bump("c", False)
                    results[batch_ids[0]] = (False, comp.stderr.strip()[:200])
                return False
            run_res = subprocess.run([bin_path], capture_output=True, text=True, timeout=10)
            if run_res.returncode != 0:
                if len(batch_ids) == 1:
                    self._bump("c", False)
                    results[batch_ids[0]] = (False, "runtime crash")
                return False
            stdout = run_res.stdout
            for idx in batch_ids:
                _, expected = items[idx]
                m = re.search(rf"__CSNIP_{idx}__:(.*?)__CEND_{idx}__", stdout, flags=re.DOTALL)
                out = m.group(1).strip() if m else ""
                if expected is not None and out != str(expected).strip():
                    self._bump("c", False)
                    results[idx] = (False, f"c mismatch: {out!r} != {expected!r}")
                else:
                    self._bump("c", True)
                    results[idx] = (True, out)
            return True

    def close(self) -> None:
        if self._node_proc is not None and self._node_proc.poll() is None:
            assert self._node_proc.stdin is not None
            try:
                self._node_proc.stdin.close()
                self._node_proc.wait(timeout=3)
            except Exception:
                self._node_proc.kill()
        self._node_proc = None
