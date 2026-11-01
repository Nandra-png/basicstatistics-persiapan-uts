# -*- coding: utf-8 -*-
"""Generator Learn with Hermes - Basic Statistics UTS (pola paper-sheet PDM)."""
import pathlib, re, json

ROOT = pathlib.Path(__file__).parent
TPL = pathlib.Path(r"C:\Users\rujak\AppData\Local\hermes\skills\productivity\class-with-hermes\templates\paper-sheet.html")

tpl_text = TPL.read_text(encoding="utf-8")
css = re.search(r"<style>(.*?)</style>", tpl_text, re.S).group(1)
basejs = re.search(r"<script>(.*?)</script>", tpl_text, re.S).group(1)

data_json = (ROOT / "src" / "data.json").read_text(encoding="utf-8")
data = json.loads(data_json)

EXTRA_CSS = """
.code{font-family:'Consolas',ui-monospace,monospace;font-size:13px;line-height:1.62;background:#fffdf5;border:1.5px solid #ddd4bd;border-left:4px solid var(--blue);border-radius:6px;padding:9px 12px;margin:8px 0 10px;overflow-x:auto;white-space:pre;color:#1e2530}
.mono{font-family:'Consolas',ui-monospace,monospace;font-size:.93em;background:#f1ece0;border-radius:4px;padding:1px 5px;border:1px solid #e2dac6}
ul.tight{margin:6px 0 6px 18px;padding:0}
ul.tight li{margin:5px 0;font-size:14.5px;line-height:1.6}
.fb-block{font-family:'Cambria Math',Georgia,serif;font-size:15px;background:#fffdf5;border:1.5px solid #ddd4bd;border-left:4px solid var(--red);border-radius:6px;padding:8px 12px;margin:8px 0 10px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
@media(max-width:650px){.grid2{grid-template-columns:1fr}}
.qmeta{font-size:11.5px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin:14px 0 6px}
.dq{font-size:16.5px;font-weight:600;line-height:1.55;margin:4px 0 12px}
.opts{display:flex;flex-direction:column;gap:8px;margin-bottom:10px}
.opt{text-align:left;font:inherit;font-size:14.5px;line-height:1.45;cursor:pointer;padding:10px 13px;border-radius:9px;border:1.5px solid var(--edge);background:#fffdf5;color:var(--ink);transition:.14s}
.opt:hover:not(:disabled){border-color:var(--blue)}
.opt.ok{border-color:var(--ok);background:#f0fbf2;box-shadow:inset 3px 0 0 var(--ok)}
.opt.no{border-color:var(--red);background:#fff5f3;box-shadow:inset 3px 0 0 var(--red)}
.nextbtn{font:inherit;font-weight:700;font-size:14px;cursor:pointer;padding:9px 18px;border-radius:9px;border:none;background:var(--ink);color:#fffdf5}
.fb{margin-top:10px;font-size:14px;line-height:1.62;padding:9px 13px;border-radius:8px;background:#f7f4ea;border-left:3px solid var(--ink-soft)}
.fb.ok{background:#f0fbf2;border-left-color:var(--ok);color:#146c2e}
.fb.bad{background:#fff5f3;border-left-color:var(--red);color:#a5281c}
.track2{height:6px;border-radius:999px;background:#e3dcc8;overflow:hidden;margin-top:8px}
.track2 i{display:block;height:100%;width:0;background:var(--red);transition:width .3s}
.donebox{text-align:center;padding:14px 0}
.donebox .sc{font-size:40px;font-weight:800;color:var(--red);line-height:1.1}
.btn2{font:inherit;font-weight:700;cursor:pointer;padding:10px 20px;border-radius:10px;border:1.5px solid var(--ink);background:var(--red);color:#fff;margin-top:12px}
"""

SHEETS = r"""
<section class="sheet" id="s0">
  <div class="kode">STAT6190031 · Basic Statistics · UTS PREP</div>
  <h1 style="font-size:26px;font-weight:800;letter-spacing:-.02em;margin-top:4px">Learn with Hermes
    <br><span style="font-size:17px;font-weight:600;color:var(--ink-soft)">Persiapan UTS · 5 Nomor Latihan Resmi</span></h1>
  <div class="sec">Jalan keledai 60 detik</div>
  <div class="step"><div class="n">1</div><div class="body"><b>NIM / ID / Jurusan = Nominal.</b> Biarpun isinya angka, sifatnya cuma label. Jangan pernah dihitung rata-ratanya.</div></div>
  <div class="step"><div class="n">2</div><div class="body"><b>Peluang bersyarat: denominator = syarat.</b> P(Bekerja | CS) dibagi total mahasiswa CS, bukan grand total 60.</div></div>
  <div class="step"><div class="n">3</div><div class="body"><b>Variansi sampel selalu bagi (n − 1).</b> Bukan n. Bagi n itu rumus populasi.</div></div>
  <div class="step"><div class="n">4</div><div class="body"><b>Bentuk distribusi cukup Mean vs Median.</b> Mean &gt; Median = menceng kanan. Mean &lt; Median = menceng kiri.</div></div>
  <div class="step"><div class="n">5</div><div class="body"><b>Tabel Z = luas ke kiri.</b> P(X &gt; a) = 1 − luas kiri. Pagar outlier = Q ± 1,5·IQR.</div></div>
  <div class="note"><b>Cara pakai halaman ini:</b> baca trik per soal di tengah, pantau rumus di kolom kanan, lalu uji di Drill 20 Soal paling bawah. Langkah kalkulator ada di <a href="cara.html">Cara Ngerjain</a>.</div>
</section>

<section class="sheet" id="s1">
  <div class="head"><div class="badge">1</div><div>
    <h2>Soal 1 · Data, Skala &amp; Kontingensi <span class="pts">20 poin</span></h2>
    <div class="sub">Survei 60 mahasiswa Computer Science &amp; Information Systems</div>
  </div></div>
  <div class="tblwrap"><table>
    <thead><tr><th>Program Studi</th><th>Bekerja Paruh Waktu</th><th>Tidak Bekerja</th><th>Total Baris</th></tr></thead>
    <tbody>
      <tr><td><b>Computer Science</b></td><td>14</td><td>16</td><td><b>30</b></td></tr>
      <tr><td><b>Information Systems</b></td><td>9</td><td>21</td><td><b>30</b></td></tr>
      <tr><td><b>Total Kolom</b></td><td><b>23</b></td><td><b>37</b></td><td><b>60</b></td></tr>
    </tbody>
  </table></div>
  <div class="sec">Bedah jawaban</div>
  <ul class="tight">
    <li><b>a) Jenis &amp; skala:</b> Program Studi = kategorikal, skala <b>nominal</b>. Status Bekerja = kategorikal, skala <b>nominal</b>.</li>
    <li><b>b) P(bekerja):</b> 23 / 60 = <b>0,3833 (38,33%)</b>.</li>
    <li><b>c) Peluang bersyarat:</b> P(bekerja | CS) = 14 / 30 = <b>0,4667</b>; P(bekerja | IS) = 9 / 30 = <b>0,3000</b>.</li>
    <li><b>d) Independen?</b> Tidak. Karena 0,4667 ≠ 0,3000, status bekerja <b>terikat</b> pada program studi.</li>
    <li><b>e) Distribusi 5 kelas (40 nilai):</b> range 96 − 52 = 44, lebar w = 44/5 ≈ 9.
      <br>52–60 (f 2) · 61–69 (f 7) · 70–78 (f 16) · 79–87 (f 10) · 88–96 (f 5).</li>
    <li><b>f) Frekuensi relatif kelas 70–78:</b> 16 / 40 = <b>0,400 (40%)</b>. Frekuensi kumulatif sampai kelas itu = 25.</li>
  </ul>
  <div class="note"><b>Jebakan:</b> kalau soalnya bilang "dari seluruh responden", pembaginya 60. Kalau "dari kelompok pria/CS", pembaginya total kelompok itu. Baca kalimatnya, jangan hafal.</div>
</section>

<section class="sheet" id="s2">
  <div class="head"><div class="badge">2</div><div>
    <h2>Soal 2 · Pemusatan &amp; Variasi <span class="pts">20 poin</span></h2>
    <div class="sub">Waktu tunggu 15 pelanggan: 8 10 11 12 12 13 14 15 15 16 18 20 22 24 25</div>
  </div></div>
  <div class="sec">Langkah hitung</div>
  <ul class="tight">
    <li><b>a) Mean:</b> ΣX = 235 → x̄ = 235 / 15 = <b>15,67 menit</b>.</li>
    <li><b>b) Median:</b> n = 15 ganjil → posisi (15+1)/2 = ke-8 → <b>15 menit</b>.</li>
    <li><b>c) Modus:</b> <b>12 dan 15</b> (bimodal, masing-masing 2 kali).</li>
    <li><b>d) Variansi sampel:</b> ΣX² = 4.053.
      <br>s² = [4053 − 235²/15] / 14 = [4053 − 3682,08] / 14 = <b>26,49</b>.
      <br>s = √26,49 = <b>5,15 menit</b>.</li>
    <li><b>e) Kuartil &amp; IQR:</b> Q1 = data ke-(16/4) = ke-4 = <b>12</b>; Q3 = data ke-(3·16/4) = ke-12 = <b>20</b>.
      <br>IQR = 20 − 12 = <b>8 menit</b>.</li>
    <li><b>f) CV:</b> (5,15 / 15,67) × 100% = <b>32,85%</b>. Variabilitas sedang.</li>
    <li><b>g) Outlier?</b> Pagar bawah 12 − 12 = <b>0</b>; pagar atas 20 + 12 = <b>32</b>. Semua data (8–25) di dalam → <b>tidak ada outlier</b>.</li>
    <li><b>h) Bentuk:</b> Mean 15,67 &gt; Median 15,00 → <b>menceng kanan (positif)</b>.</li>
  </ul>
  <div class="note"><b>Jebakan:</b> variansi data berkelompok pakai titik tengah m: s² = [Σ(f·m²) − (Σf·m)²/n] / (n − 1). Jangan lupa bagi n − 1.</div>
</section>

<section class="sheet" id="s3">
  <div class="head"><div class="badge">3</div><div>
    <h2>Soal 3 · Distribusi Probabilitas Diskrit <span class="pts">20 poin</span></h2>
    <div class="sub">Jumlah barang rusak per hari (X)</div>
  </div></div>
  <div class="tblwrap"><table>
    <thead><tr><th>X</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>Σ</th></tr></thead>
    <tbody><tr><td><b>P(X = x)</b></td><td>0,10</td><td>0,25</td><td>0,35</td><td>0,20</td><td>0,10</td><td><b>1,00</b></td></tr></tbody>
  </table></div>
  <div class="sec">Bedah jawaban</div>
  <ul class="tight">
    <li><b>a) Sah?</b> Sah. Semua P(x) ≥ 0 dan ΣP(x) = 0,10+0,25+0,35+0,20+0,10 = <b>1,00</b>.</li>
    <li><b>b) P(X ≥ 3):</b> 0,20 + 0,10 = <b>0,30</b>. P(X ≤ 1) = 0,10 + 0,25 = <b>0,35</b>.</li>
    <li><b>c) P(1 &lt; X ≤ 3):</b> X = 2 dan 3 → 0,35 + 0,20 = <b>0,55</b>.</li>
    <li><b>d) E(X):</b> Σx·P(x) = 0 + 0,25 + 0,70 + 0,60 + 0,40 = <b>1,95 unit</b>.</li>
    <li><b>e) Var(X):</b> Σx²·P(x) = 0 + 0,25 + 1,40 + 1,80 + 1,60 = 5,05.
      <br>Var = 5,05 − 1,95² = 5,05 − 3,8025 = <b>1,2475</b>; σ = <b>1,117 unit</b>.</li>
    <li><b>f) Biaya harian:</b> C = 10.000 + 25.000·X → E(C) = 10.000 + 25.000(1,95) = <b>Rp 58.750</b>.</li>
  </ul>
  <div class="sec">Kalau soalnya ganti ke distribusi bernama</div>
  <pre class="code">Binomial        P(X=x) = nCx · p^x · (1-p)^(n-x)
Poisson         P(X=x) = e^(-λ) · λ^x / x!      E = Var = λ
Hypergeometric  P(X=x) = C(k,x)·C(N-k,n-x) / C(N,n)</pre>
  <div class="note"><b>Pemicu:</b> "tanpa pengembalian" = hypergeometric. "per menit/per hari" = Poisson. "n percobaan, sukses/gagal" = binomial.</div>
</section>

<section class="sheet" id="s4">
  <div class="head"><div class="badge">4</div><div>
    <h2>Soal 4 · Distribusi Normal &amp; Z <span class="pts">20 poin</span></h2>
    <div class="sub">Nilai ujian normal: μ = 72, σ = 8</div>
  </div></div>
  <pre class="code">Z = (X − μ) / σ        X = μ + Z·σ
P(X &lt; a)  → tabel kiri
P(X &gt; a)  → 1 − tabel kiri
P(a &lt; X &lt; b) → kiri(b) − kiri(a)</pre>
  <ul class="tight">
    <li><b>a) P(X &lt; 60):</b> Z = (60−72)/8 = <b>−1,50</b> → <b>0,0668 (6,68%)</b>.</li>
    <li><b>b) P(60 &lt; X &lt; 80):</b> kiri(−1,50) = 0,0668; kiri(+1,00) = 0,8413 → <b>0,7745 (77,45%)</b>.</li>
    <li><b>c) P(X &gt; 85):</b> Z = 13/8 = 1,63 → 1 − 0,9484 = <b>0,0516 (5,16%)</b>.</li>
    <li><b>d) 10% teratas:</b> cari luas kiri 0,9000 → Z ≈ 1,28 → X = 72 + 1,28(8) = <b>82,24</b>.</li>
    <li><b>e) Tidak lulus (&lt; 58):</b> Z = −1,75 → <b>0,0401 (4,01%)</b>.</li>
  </ul>
  <div class="note"><b>Jebakan:</b> "10% teratas" bukan cari 0,10 di tabel. Tabel memberi luas kiri, jadi yang dicari 0,9000.</div>
</section>

<section class="sheet" id="s5">
  <div class="head"><div class="badge">5</div><div>
    <h2>Soal 5 · Box Plot &amp; Interpretasi <span class="pts">20 poin</span></h2>
    <div class="sub">Ringkasan lima angka dua kelas</div>
  </div></div>
  <div class="tblwrap"><table>
    <thead><tr><th>Statistik</th><th>Kelas A</th><th>Kelas B</th></tr></thead>
    <tbody>
      <tr><td>Minimum</td><td>45</td><td>40</td></tr>
      <tr><td>Q1</td><td>62</td><td>55</td></tr>
      <tr><td>Median</td><td>74</td><td>68</td></tr>
      <tr><td>Q3</td><td>82</td><td>85</td></tr>
      <tr><td>Maksimum</td><td>95</td><td>98</td></tr>
    </tbody>
  </table></div>
  <ul class="tight">
    <li><b>a) IQR:</b> A = 82 − 62 = <b>20</b>; B = 85 − 55 = <b>30</b>.</li>
    <li><b>b) Pagar outlier B:</b> bawah 55 − 45 = <b>10</b>; atas 85 + 45 = <b>130</b>. Data 40–98 aman → <b>tidak ada outlier</b>.</li>
    <li><b>c) Lebih tinggi?</b> <b>Kelas A</b> — median 74 &gt; 68.</li>
    <li><b>d) Lebih menyebar?</b> <b>Kelas B</b> — IQR 30 &gt; 20.</li>
    <li><b>e) Sketsa B:</b> kotak 55–85, garis median di 68, kumis 40 dan 98.</li>
    <li><b>f) Bentuk B:</b> median 68 lebih dekat ke Q1 (selisih 13) daripada ke Q3 (selisih 17) → <b>menceng kanan</b>.</li>
  </ul>
  <div class="note"><b>Baca cepat:</b> kotak panjang = data menyebar. Median mepet salah satu sisi kotak = arah kemencengan ada di sisi yang jauh.</div>
</section>

<section class="sheet" id="s6">
  <div class="head"><div class="badge">6</div><div>
    <h2>Drill 20 Soal <span class="pts">Mock Test</span></h2>
    <div class="sub">3 nyawa · streak · petunjuk bertahap kalau salah</div>
  </div></div>
  <div id="dzone">
    <div class="qmeta"><span id="dtopic">Topik</span> · Soal <b id="dqnum">1</b> / 20</div>
    <p class="dq" id="dq"></p>
    <div class="opts" id="dans"></div>
    <div class="fb" id="dfb" hidden></div>
    <button class="nextbtn" id="dnext" hidden type="button">Lanjut →</button>
  </div>
  <div class="donebox" id="ddone" hidden>
    <div class="sc" id="dscore">0 / 20</div>
    <p id="dverdict" style="font-size:16px;font-weight:700;margin-top:6px"></p>
    <p id="dweak" style="font-size:13.5px;color:var(--ink-soft)"></p>
    <button class="btn2" type="button" id="drestart">Ulangi drill</button>
  </div>
</section>
"""

LEFT = r"""
<aside class="rail left" id="railLeft">
  <div class="panel">
    <h4>Progress</h4>
    <div class="total"><b id="pct">0%</b><span id="cnt">0 / 7</span></div>
    <div class="pbar"><i id="pfill"></i></div>
  </div>
  <div class="panel">
    <h4>Roadmap</h4>
    <ul class="road" id="road">
      <li class="now"><span class="dot"></span><a href="#s0">Jalan Keledai<small>Trik 60 detik</small></a></li>
      <li><span class="dot"></span><a href="#s1">Soal 1 · Data<small>Skala &amp; kontingensi</small></a></li>
      <li><span class="dot"></span><a href="#s2">Soal 2 · Ukuran<small>Mean, s², CV</small></a></li>
      <li><span class="dot"></span><a href="#s3">Soal 3 · Diskrit<small>E(X), Var(X)</small></a></li>
      <li><span class="dot"></span><a href="#s4">Soal 4 · Normal<small>Z-score</small></a></li>
      <li><span class="dot"></span><a href="#s5">Soal 5 · Box plot<small>IQR &amp; outlier</small></a></li>
      <li><span class="dot"></span><a href="#s6">Drill 20<small id="c7">0 / 20</small></a></li>
    </ul>
  </div>
  <div class="panel">
    <h4>Lanjutan</h4>
    <a href="cara.html" style="color:var(--blue);font-weight:700;text-decoration:none;border-bottom:1px solid var(--blue)">Cara ngerjain + kalkulator →</a>
  </div>
</aside>
"""

RIGHT = r"""
<aside class="rail right" id="railRight">
  <div class="panel info">
    <h4>Ujian</h4>
    <div class="kv"><span>Matkul</span><b>Basic Statistics</b></div>
    <div class="kv"><span>Kode</span><b>STAT6190031</b></div>
    <div class="kv"><span>Dosen</span><b>Dr. Dani Suandi</b></div>
    <div class="kv"><span>Sifat</span><b>Open book</b></div>
    <div class="kv"><span>Nyawa</span><b id="lives">♥ ♥ ♥</b></div>
    <div class="kv"><span>Streak</span><b id="streak">0</b></div>
    <div class="kv"><span>Drill</span><b id="dcnt">0 / 20</b></div>
    <div class="track2"><i id="dprog"></i></div>
  </div>
  <div class="panel">
    <h4>Rumus cepat</h4>
    <div class="fb-block">P(A|B) = P(A∩B) / P(B)</div>
    <div class="fb-block">s² = [ΣX² − (ΣX)²/n] / (n−1)</div>
    <div class="fb-block">Z = (X − μ) / σ</div>
    <div class="fb-block">IQR = Q3 − Q1</div>
  </div>
  <div class="panel">
    <h4>Jebakan dosen</h4>
    <div class="fb-block" style="font-family:inherit;font-size:12.5px">NIM / ID = nominal<br>at least = ≥<br>variansi sampel bagi n−1<br>tabel Z = luas kiri</div>
  </div>
</aside>
"""

DRILL_JS = r"""
var setupDrill;
(function(){
  var idx = 0, lives = 3, streak = 0, right = 0, hint = 0, locked = false, wrong = {};
  var $ = function(s){ return document.querySelector(s); };
  function hud(){
    $('#lives').textContent = '\u2665 '.repeat(Math.max(0,lives)) + '\u2661 '.repeat(Math.max(0,3-lives));
    $('#streak').textContent = streak;
    $('#dcnt').textContent = Math.min(idx, ITEMS.length) + ' / ' + ITEMS.length;
    $('#dprog').style.width = (idx / ITEMS.length * 100) + '%';
    $('#dqnum').textContent = Math.min(idx + 1, ITEMS.length);
  }
  function finish(){
    $('#dzone').hidden = true; $('#ddone').hidden = false;
    $('#dscore').textContent = right + ' / ' + ITEMS.length;
    var acc = Math.round(right / ITEMS.length * 100);
    $('#dverdict').textContent = acc >= 85 ? 'Siap UTS. Pertahankan.' : acc >= 65 ? 'Lumayan. Poles bagian yang keliru.' : 'Baca jalan keledai, lalu ulangi.';
    var w = Object.keys(wrong);
    $('#dweak').textContent = w.length ? 'Masih goyang: ' + w.join(' · ') : 'Semua benar.';
    $('#c7').textContent = right + ' / ' + ITEMS.length;
    $('#dprog').style.width = '100%'; $('#dcnt').textContent = ITEMS.length + ' / ' + ITEMS.length;
  }
  function render(){
    if (idx >= ITEMS.length) return finish();
    var it = ITEMS[idx]; hint = 0; locked = false;
    $('#dtopic').textContent = it.t; $('#dq').textContent = it.q;
    var fb = $('#dfb'); fb.hidden = true; fb.className = 'fb'; fb.innerHTML = '';
    $('#dnext').hidden = true;
    var box = $('#dans'); box.innerHTML = '';
    it.p.forEach(function(opt, k){
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'opt'; b.textContent = opt;
      b.onclick = function(){ answer(b, k === it.a, it); };
      box.appendChild(b);
    });
    hud();
  }
  function answer(btn, ok, it){
    if (locked) return;
    var fb = $('#dfb');
    if (ok){
      locked = true; right++; streak++;
      btn.classList.add('ok');
      document.querySelectorAll('#dans .opt').forEach(function(b){ b.disabled = true; });
      fb.hidden = false; fb.className = 'fb ok'; fb.innerHTML = '<b>Benar.</b> ' + it.w;
      $('#dnext').hidden = false;
    } else {
      lives--; streak = 0; wrong[it.t] = 1;
      btn.classList.add('no'); btn.disabled = true;
      fb.hidden = false; fb.className = 'fb bad';
      if (lives <= 0){
        locked = true;
        document.querySelectorAll('#dans .opt').forEach(function(b){ b.disabled = true; });
        fb.innerHTML = '<b>Nyawa habis.</b> Jawaban: <u>' + it.p[it.a] + '</u><br><small>' + it.w + '</small>';
        $('#dnext').hidden = false;
      } else {
        fb.innerHTML = '<b>Belum tepat.</b> Petunjuk: ' + it.h[Math.min(hint, it.h.length - 1)];
        hint++;
      }
    }
    hud();
  }
  $('#dnext').onclick = function(){ idx++; render(); };
  $('#drestart').onclick = function(){
    idx = 0; lives = 3; streak = 0; right = 0; hint = 0; locked = false; wrong = {};
    $('#dzone').hidden = false; $('#ddone').hidden = true; render();
  };
  render();
})();
"""

js = "var ITEMS = " + data_json + ";\n" + basejs + "\n" + DRILL_JS


def shell(title, body, script):
    return (
        "<!doctype html>\n<html lang=\"id\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
        f"<title>{title}</title>\n<style>\n{css}{EXTRA_CSS}</style>\n</head>\n<body>\n"
        "<div class=\"toggles\">\n  <button id=\"tLeft\" type=\"button\">☰ Roadmap</button>\n"
        "  <button id=\"tRight\" type=\"button\">ⓘ Info</button>\n</div>\n"
        f"<div class=\"wrap\">\n{body}</div>\n<script>\n{script}</script>\n</body>\n</html>"
    )


index_html = shell("Learn with Hermes · Basic Statistics UTS",
                   LEFT + "<main>\n" + SHEETS + "</main>\n" + RIGHT, js)
(ROOT / "index.html").write_text(index_html, encoding="utf-8")

# ---------------- cara.html : langkah kalkulator Joyko CC-23 ----------------
CARA_BODY = r"""
<main>
<section class="sheet" id="c0">
  <div class="kode">JOYKO CC-23 · TOMBOL PER SOAL</div>
  <h1 style="font-size:24px;margin-top:4px">Cara Ngerjain di Kalkulator</h1>
  <div class="note">Kalkulator ini satu keluarga dengan Casio seri MS. Untuk ujian, jangan pakai mode STAT — akumulasi pakai <b>M+</b>, baca total dengan <b>RCL M</b>.</div>
  <div class="sec">Tombol dasar</div>
  <pre class="code">SHIFT        tombol kuning (fungsi atas)
ALPHA        tombol merah (variabel)
M+ / RCL M   tambah ke memori / baca memori
√            akar
x²           kuadrat
^            pangkat
nCr          kombinasi (di atas tombol ÷ / SHIFT)
ln           log natural (SHIFT dari e^x)</pre>
</section>

<section class="sheet" id="c1">
  <div class="head"><div class="badge">1</div><div><h2>Soal 1 · Persen &amp; Tabel</h2><div class="sub">cukup bagi, tidak perlu tombol khusus</div></div></div>
  <pre class="code">23 ÷ 60 =                 → 0,38333
23 ÷ 60 × 100 =           → 38,333
14 ÷ 30 =                 → 0,46667
0,46667 − 0,3 =           → 0,16667 (bukti tidak independen)</pre>
</section>

<section class="sheet" id="c2">
  <div class="head"><div class="badge">2</div><div><h2>Soal 2 · Mean, Variansi, Kuartil</h2><div class="sub">akumulasi ΣX dan ΣX²</div></div></div>
  <div class="sec">ΣX</div>
  <pre class="code">AC  →  8 M+ 10 M+ 11 M+ 12 M+ 12 M+ 13 M+ 14 M+
        15 M+ 15 M+ 16 M+ 18 M+ 20 M+ 22 M+ 24 M+ 25 M+
RCL M                     → 235
235 ÷ 15 =                → 15,6667</pre>
  <div class="sec">ΣX²</div>
  <pre class="code">AC  →  8 x² M+ 10 x² M+ 11 x² M+ 12 x² M+ ... 25 x² M+
RCL M                     → 4053
( 4053 − 235 x² ÷ 15 ) ÷ 14 =    → 26,494
√                         → 5,1472</pre>
  <div class="sec">Kuartil (data ke-4 dan ke-12)</div>
  <pre class="code">posisi Q1 = (15+1) ÷ 4 = 4    → data ke-4 = 12
posisi Q3 = 3 × 4 = 12        → data ke-12 = 20</pre>
</section>

<section class="sheet" id="c3">
  <div class="head"><div class="badge">3</div><div><h2>Soal 3 · E(X) &amp; Var(X)</h2><div class="sub">pakai M+ untuk ΣxP(x)</div></div></div>
  <pre class="code">0 × 0,10 = M+
1 × 0,25 = M+
2 × 0,35 = M+
3 × 0,20 = M+
4 × 0,10 = M+
RCL M                     → 1,95      (E(X))

AC  → 0 x² × 0,10 M+ 1 x² × 0,25 M+ ...
RCL M                     → 5,05
5,05 − 1,95 x² =          → 1,2475    (Var)
√                         → 1,1169</pre>
  <div class="sec">Binomial &amp; Poisson</div>
  <pre class="code">12 nCr 2 =                → 66
0,05 x² 3 =  ...  pakai ^ : 0,05 ^ 3 =  → 0,000125
e^(-λ):  SHIFT ln (-) 2 = → 0,13534
3! :  3 SHIFT x! =        → 6</pre>
</section>

<section class="sheet" id="c4">
  <div class="head"><div class="badge">4</div><div><h2>Soal 4 · Z</h2><div class="sub">satu rumus, dua arah</div></div></div>
  <pre class="code">Z:   ( 60 − 72 ) ÷ 8 =    → −1,5
X:   72 + 1,28 × 8 =      → 82,24</pre>
  <div class="note">Nilai Z dari tabel dibaca manual. Kalkulator cuma dipakai untuk transformasi.</div>
</section>

<section class="sheet" id="c5">
  <div class="head"><div class="badge">5</div><div><h2>Soal 5 · IQR &amp; Pagar</h2><div class="sub">tiga baris selesai</div></div></div>
  <pre class="code">82 − 62 =                 → 20        (IQR A)
85 − 55 =                 → 30        (IQR B)
55 − 1,5 × 30 =           → 10        (pagar bawah)
85 + 1,5 × 30 =           → 130       (pagar atas)</pre>
</section>
</main>
"""
CARA_LEFT = r"""
<aside class="rail left" id="railLeft">
  <div class="panel">
    <h4>Navigasi</h4>
    <ul class="road" id="road">
      <li class="now"><span class="dot"></span><a href="#c0">Tombol dasar<small>SHIFT, M+, nCr</small></a></li>
      <li><span class="dot"></span><a href="#c1">Soal 1<small>Persen</small></a></li>
      <li><span class="dot"></span><a href="#c2">Soal 2<small>ΣX, ΣX², kuartil</small></a></li>
      <li><span class="dot"></span><a href="#c3">Soal 3<small>E(X), nCr</small></a></li>
      <li><span class="dot"></span><a href="#c4">Soal 4<small>Z</small></a></li>
      <li><span class="dot"></span><a href="#c5">Soal 5<small>IQR</small></a></li>
    </ul>
  </div>
  <div class="panel"><h4>Balik</h4><a href="index.html" style="color:var(--blue);font-weight:700;text-decoration:none;border-bottom:1px solid var(--blue)">← Latihan UTS</a></div>
</aside>
"""
cara_html = shell("Cara Ngerjain · Joyko CC-23", CARA_LEFT + CARA_BODY + RIGHT, basejs)
(ROOT / "cara.html").write_text(cara_html, encoding="utf-8")

print(f"index.html {len(index_html)} bytes | cara.html {len(cara_html)} bytes | {len(data)} drill items")