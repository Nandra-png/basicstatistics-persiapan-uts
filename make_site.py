# -*- coding: utf-8 -*-
"""Framework halaman belajar: paper-sheet + sticky notes + konversi math ke HTML/Unicode.

Semua builder import `shell`. LaTeX di dalam $...$ dikonversi jadi HTML asli
(<sup>, <sub>, fraksi bersusun) supaya simbol kebaca tanpa JS dan tanpa font khusus.
"""
import pathlib, re

ROOT = pathlib.Path(__file__).parent
TPL = pathlib.Path(r"C:\Users\rujak\AppData\Local\hermes\skills\productivity\class-with-hermes\templates\paper-sheet.html")

tpl_text = TPL.read_text(encoding="utf-8")
css = re.search(r"<style>(.*?)</style>", tpl_text, re.S).group(1)
basejs = re.search(r"<script>(.*?)</script>", tpl_text, re.S).group(1)

TABS = [
    ("materi.html", "materi", "📖 1. Materi"),
    ("rangkuman.html", "rangkuman", "🧠 2. Rangkuman PDF"),
    ("uts.html", "uts", "🎯 3. Breakdown UTS"),
    ("kalkulator.html", "kalkulator", "🖩 4. Kalkulator"),
]

SYMBOLS = {
    "approx": "≈", "ne": "≠", "neq": "≠", "le": "≤", "leq": "≤", "ge": "≥", "geq": "≥",
    "mid": " | ", "to": "→", "rightarrow": "→", "leftarrow": "←", "infty": "∞",
    "mu": "μ", "sigma": "σ", "Sigma": "Σ", "sum": "Σ", "lambda": "λ", "pi": "π",
    "Phi": "Φ", "phi": "φ", "alpha": "α", "beta": "β", "theta": "θ", "Delta": "Δ",
    "chi": "χ", "rho": "ρ", "tau": "τ", "eta": "η", "epsilon": "ε",
    "cdot": "·", "times": "×", "div": "÷", "pm": "±", "mp": "∓",
    "cup": "∪", "cap": "∩", "in": "∈", "notin": "∉", "subset": "⊂",
    "forall": "∀", "exists": "∃", "therefore": "∴", "because": "∵",
    "ldots": "…", "dots": "…", "cdots": "⋯",
    "quad": "  ", "qquad": "    ", ",": " ", ";": " ", ":": " ", "!": "",
    "%": "%", "&": "&", "#": "#",
    "circ": "°", "degree": "°", "prime": "′",
    "log": "log", "ln": "ln", "max": "max", "min": "min", "exp": "exp",
    "left": "", "right": "", "big": "", "Big": "", "bigl": "", "bigr": "",
    "displaystyle": "", "limits": "", "textstyle": "",
    "lfloor": "⌊", "rfloor": "⌋", "lceil": "⌈", "rceil": "⌉",
    "{": "{", "}": "}", "|": "‖",
}
SUPS = {"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵",
        "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹", "n": "ⁿ", "k": "ᵏ",
        "+": "⁺", "-": "⁻", "x": "ˣ", "i": "ⁱ"}
SUBS = {"0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅",
        "6": "₆", "7": "₇", "8": "₈", "9": "₉", "n": "ₙ", "k": "ₖ",
        "i": "ᵢ", "j": "ⱼ", "x": "ₓ", "a": "ₐ"}


def _group(s, i):
    if i >= len(s) or s[i] != "{":
        return (s[i] if i < len(s) else ""), i + 1
    depth, j = 0, i
    while j < len(s):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    return s[i + 1:], len(s)


def _script(cmd, body):
    table = SUPS if cmd == "^" else SUBS
    if len(body) == 1 and body in table:
        return table[body]
    tag = "sup" if cmd == "^" else "sub"
    return f"<{tag}>{body}</{tag}>"


def tex(s):
    """Konversi potongan LaTeX (tanpa $) ke HTML."""
    out, i = [], 0
    while i < len(s):
        c = s[i]

        if c == "\\":
            j = i + 1
            if j < len(s) and not s[j].isalpha():
                name, i = s[j], j + 1
            else:
                while j < len(s) and s[j].isalpha():
                    j += 1
                name, i = s[i + 1:j], j

            if name in ("frac", "dfrac", "tfrac", "cfrac"):
                a, i = _group(s, i)
                b, i = _group(s, i)
                out.append(f'<span class="frac"><span class="top">{tex(a)}</span>'
                           f'<span class="bot">{tex(b)}</span></span>')
            elif name == "binom":
                a, i = _group(s, i)
                b, i = _group(s, i)
                out.append(f'<span class="binom">{tex(a)}<span class="over">{tex(b)}</span></span>')
            elif name == "sqrt":
                body, i = _group(s, i)
                out.append(f'√<span class="rad">{tex(body)}</span>')
            elif name in ("text", "mathrm", "textrm", "operatorname", "textnormal"):
                body, i = _group(s, i)
                out.append(tex(body))
            elif name in ("mathbf", "textbf", "boldsymbol"):
                body, i = _group(s, i)
                out.append(f"<b>{tex(body)}</b>")
            elif name in ("mathit", "textit"):
                body, i = _group(s, i)
                out.append(f"<i>{tex(body)}</i>")
            elif name in ("bar", "overline", "hat", "widehat", "vec"):
                body, i = _group(s, i)
                mark = "̄" if name in ("bar", "overline") else "̂"
                out.append(f"{tex(body)}{mark}")
            elif name == "mathbb":
                body, i = _group(s, i)
                out.append({"R": "ℝ", "N": "ℕ", "Z": "ℤ", "Q": "ℚ"}.get(body, tex(body)))
            else:
                out.append(SYMBOLS.get(name, name))
            continue

        if c in "^_":
            i += 1
            body, i = _group(s, i)
            out.append(_script(c, tex(body)))
            continue

        if c == "{":
            body, i = _group(s, i)
            out.append(tex(body))
            continue
        if c == "}":
            i += 1
            continue

        out.append(c)
        i += 1

    return "".join(out)


_MATH_SPAN = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.S)
_LEFTOVER = re.compile(
    r"\\(?:d?t?frac\{[^{}]*\}\{[^{}]*\}|binom\{[^{}]*\}\{[^{}]*\}|sqrt\{[^{}]*\}"
    r"|mathbf\{[^{}]*\}|text\{[^{}]*\}|left[.([]|right[.)\]]"
    r"|approx|neq?|leq?|geq?|mid|to|mu|sigma|Sigma|sum|lambda|pi|cdot|times"
    r"|ldots|quad|circ|max|min|log|infty|pm|cup|cap|in)(?![a-zA-Z])"
)


def render_math(html):
    html = _MATH_SPAN.sub(lambda m: tex(m.group(1) if m.group(1) is not None else m.group(2)), html)
    for _ in range(4):
        new = _LEFTOVER.sub(lambda m: tex(m.group(0)), html)
        if new == html:
            break
        html = new
    return html


EXTRA_CSS = """
/* ---------- matematika ---------- */
.frac{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;
      padding:0 3px;font-size:.95em;line-height:1.2}
.frac .top{border-bottom:1.5px solid currentColor;padding:0 3px 1px}
.frac .bot{padding:1px 3px 0}
.binom{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;
       font-size:.92em;line-height:1.15;padding:0 2px}
.binom .over{border-top:1.5px solid currentColor;padding-top:1px}
.rad{border-top:1.5px solid currentColor;padding:0 3px}
sup,sub{font-size:.72em;line-height:0}
.formula{font-size:15px;line-height:2.1;letter-spacing:.2px}
.formula .frac{font-size:.9em}

/* ---------- layout ---------- */
.code{font-family:'Consolas',ui-monospace,monospace;font-size:13px;line-height:1.62;background:#fffdf5;
      border:1.5px solid #ddd4bd;border-left:4px solid var(--blue);border-radius:6px;padding:9px 12px;
      margin:8px 0 10px;overflow-x:auto;white-space:pre;color:#1e2530}
.mono{font-family:'Consolas',ui-monospace,monospace;font-size:.93em;background:#f1ece0;border-radius:4px;padding:1px 5px;border:1px solid #e2dac6}
ul.tight{margin:6px 0 6px 18px;padding:0}
ul.tight li{margin:6px 0;font-size:14.5px;line-height:1.65}
.fb-block{font-size:14.5px;background:#fffdf5;border:1.5px solid #ddd4bd;border-left:4px solid var(--red);
          border-radius:6px;padding:9px 12px;margin:9px 0;line-height:1.95}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
@media(max-width:650px){.grid2{grid-template-columns:1fr}}

.nav-tabs{display:flex;gap:8px;margin-bottom:18px;border-bottom:2px solid var(--edge);padding-bottom:10px;overflow-x:auto}
.nav-tab{padding:8px 14px;border-radius:8px;font-weight:700;font-size:13px;text-decoration:none;
         color:var(--ink);background:#f2ede2;border:1.5px solid var(--edge);white-space:nowrap}
.nav-tab.active{background:var(--red);color:#fff;border-color:var(--red)}
.nav-tab:hover:not(.active){background:#e8e0d0}

/* ---------- PRAKTEK DULU ---------- */
.praktek-card{background:#f4fbf0;border:2px solid #4a8c2a;border-radius:10px;padding:14px 18px;margin:16px 0}
.praktek-card .ptag{display:inline-block;background:#4a8c2a;color:#fff;font-weight:800;font-size:11.5px;
                    padding:3px 10px;border-radius:4px;margin-bottom:8px;text-transform:uppercase;letter-spacing:.05em}
.praktek-card h3{margin:4px 0 8px;font-size:17px;color:#2b5a12}

/* ---------- FORMULA HERO ---------- */
.formula-hero{background:#fffef8;border:2px solid #1f5f8b;border-radius:10px;padding:14px 18px;margin:14px 0}
.formula-hero .fname{font-size:16px;font-weight:800;color:#1f5f8b;display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:6px}
.formula-hero .alias{background:#e2effa;color:#104064;font-size:11.5px;padding:3px 10px;border-radius:14px;
                     border:1px solid #b8d9f2;font-weight:800;letter-spacing:.03em}
.formula-hero .kapan{font-size:13.5px;line-height:1.75;color:#333;margin:10px 0 0;padding:8px 0 0 12px;border-left:3px solid #b8d9f2}

/* ---------- ANALOGI ---------- */
.analogi{background:#fefbf2;border:1.5px dashed #c49742;border-left:5px solid #d48b14;border-radius:8px;padding:14px 16px;margin:14px 0}
.analogi h4{margin:0 0 6px;color:#8f5600;font-size:15px;font-weight:800}
.analogi p{margin:5px 0;font-size:14px;line-height:1.75}
.analogi .kesimpulan{background:#fff;border:1px solid #ebd8b0;border-radius:6px;padding:9px 12px;margin-top:10px;
                     font-size:13.5px;color:#613e05;font-weight:700;line-height:1.65}

/* ---------- lain ---------- */
.trap-card{background:#fff5f3;border:1.5px solid #f1cfc8;border-left:4px solid var(--red);border-radius:8px;padding:12px 16px;margin:10px 0}
.trap-card b{color:var(--red);font-size:14.5px}
.self-test{background:#f7f5ec;border:1.5px dashed #cfc6af;border-radius:8px;padding:14px;margin:16px 0}
.reveal-btn{font:inherit;font-weight:700;font-size:13px;cursor:pointer;padding:6px 14px;border-radius:6px;
            border:1.5px solid var(--ink);background:#fff;margin-top:8px}
.reveal-content{margin-top:10px;padding-top:10px;border-top:1px dashed #dcd3be;display:none}
.worked{background:#fdfcf7;border:1.5px solid #d9d1bc;border-left:4px solid var(--ok);border-radius:8px;padding:12px 16px;margin:12px 0}
.worked h4{margin:0 0 8px;font-size:14px;color:var(--ok);font-weight:800;letter-spacing:.03em;text-transform:uppercase}

/* ---------- drill "tebak rumus" ---------- */
.drill-opts{display:grid;gap:7px;margin:9px 0}
.drill-opts button{font:inherit;font-size:13.5px;text-align:left;cursor:pointer;padding:9px 13px;
  border:1.5px solid #cfc6af;border-radius:7px;background:#fff;color:var(--ink);transition:.12s}
.drill-opts button:hover:not([style*="background"]){background:#f6f2e6;border-color:var(--ink-soft)}
.drill-opts button:disabled{cursor:default}
.drill-fb{display:none;font-size:13.5px;padding:8px 12px;border-radius:6px;background:#f7f5ec;
  border:1px dashed #cfc6af;margin-top:4px;line-height:1.6}

.tblwrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
.rumus-tbl{width:100%;border-collapse:collapse;font-size:13.5px;margin:10px 0}
.rumus-tbl th{background:#eef3f7;text-align:left;padding:8px 10px;border:1px solid #cdd8e0;font-size:12.5px}
.rumus-tbl td{padding:8px 10px;border:1px solid #e0dccd;vertical-align:top;line-height:1.6}
.rumus-tbl td:first-child{font-weight:800;color:#1f5f8b}
"""

NAV_RE = re.compile(r'<div class="nav-tabs">.*?</div>', re.S)


def _nav(active):
    links = "".join(
        f'<a href="{href}" class="nav-tab{" active" if key == active else ""}">{label}</a>'
        for href, key, label in TABS
    )
    return f'<div class="nav-tabs">{links}</div>'


def shell(title, body, script="", current_tab="materi"):
    body = NAV_RE.sub(_nav(current_tab), body, count=1)
    body = render_math(body)

    return f"""<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<style>
{css}{EXTRA_CSS}
</style>
</head>
<body>
<div class="toggles">
  <button id="tLeft" type="button">☰ Menu Nav</button>
  <button id="tRight" type="button">📌 Catatan Sticky</button>
</div>
<div class="wrap">
{body}
</div>
<script>
{basejs}
</script>
<script>
{script}
</script>
</body>
</html>"""


def F(num, den):
    return f'<span class="frac"><span class="top">{num}</span><span class="bot">{den}</span></span>'


if __name__ == "__main__":
    assert tex(r"\frac{23}{60}") == ('<span class="frac"><span class="top">23</span>'
                                    '<span class="bot">60</span></span>')
    assert tex(r"P(\text{bekerja})") == "P(bekerja)"
    assert tex(r"s^2") == "s²"
    assert tex(r"\bar{x}") == "x̄"
    assert tex(r"x_{i}") == "xᵢ"
    assert tex(r"x_{k+1}") == "x<sub>k+1</sub>"
    assert tex(r"\left(\frac{a}{b}\right)").count("frac") == 1
    assert render_math("nilai $\\mu = 200$, $\\sigma = 40$").count("$") == 0
    print("make_site.py v5: konversi math native, self-check lulus.")