# -*- coding: utf-8 -*-
"""Builder Halaman 2: Breakdown 5 Soal UTS + Study Case Baru."""
import sys, pathlib

ROOT = pathlib.Path("C:/Users/rujak/Desktop/01-Kuliah/materi_binus/basicstatistics/persiapan_uts")
sys.path.insert(0, str(ROOT))
from make_site import shell, ROOT

UTS_BODY = r"""
<main>
<div class="nav-tabs">
  <a href="materi.html" class="nav-tab">📖 1. Materi Lengkap PPT</a>
  <a href="uts.html" class="nav-tab active">🎯 2. Breakdown Soal UTS</a>
  <a href="kalkulator.html" class="nav-tab">🖩 3. Kalkulator &amp; Latihan</a>
</div>

<section class="sheet" id="u0">
  <div class="kode">BREAKDOWN 5 NOMOR · CONTOH SOAL UTS</div>
  <h1 style="font-size:25px;font-weight:800;margin-top:4px">Bedah Langkah Hitung 5 Soal UTS
    <br><span style="font-size:16px;font-weight:600;color:var(--ink-soft)">Setiap Soal + Study Case Tambahan (Angka Beda, Konsep Sama)</span></h1>
  <div class="note">
    <b>Petunjuk belajar:</b> Pahami dulu setiap langkah di soal asli UTS. Lalu coba kerjakan <b>Study Case Baru</b> di bawah setiap soal — angka dan ceritanya beda, tapi rumusnya sama persis. Bandingkan langkah lu dengan kunci jawaban yang disediakan.
  </div>
</section>

<!-- ============ SOAL 1 ============ -->
<section class="sheet" id="u1">
  <div class="head"><div class="badge">1</div><div>
    <h2>Soal 1 · Data, Skala &amp; Tabel Kontingensi <span class="pts">20 poin</span></h2>
    <div class="sub">Survei 60 mahasiswa Computer Science &amp; Information Systems tentang bekerja paruh waktu</div>
  </div></div>

  <div class="tblwrap"><table>
    <thead><tr><th>Program Studi</th><th>Bekerja Paruh Waktu</th><th>Tidak Bekerja</th><th>Total Baris</th></tr></thead>
    <tbody>
      <tr><td><b>Computer Science</b></td><td>14</td><td>16</td><td><b>30</b></td></tr>
      <tr><td><b>Information Systems</b></td><td>9</td><td>21</td><td><b>30</b></td></tr>
      <tr><td><b>Total Kolom</b></td><td><b>23</b></td><td><b>37</b></td><td><b>60</b></td></tr>
    </tbody>
  </table></div>

  <div class="sec">Bedah Jawaban Lengkap</div>
  <ul class="tight">
    <li><b>a) Jenis &amp; skala variabel:</b>
      <br>• <b>"Program Studi" (CS / IS):</b> Data <b>kategorikal</b>, skala <b>nominal</b>. Kenapa? Karena "CS" dan "IS" hanyalah nama dua jurusan — tidak bisa diurutkan (CS bukan "lebih tinggi" dari IS), tidak bisa dijumlahkan.
      <br>• <b>"Status Bekerja Paruh Waktu" (Ya / Tidak):</b> Data <b>kategorikal</b>, skala <b>nominal</b>. Alasannya sama — cuma dua label tanpa urutan logis.
    </li>
    <li><b>b) $P(\text{bekerja paruh waktu})$:</b>
      <br>Pertanyaan memilih acak satu dari SELURUH 60 mahasiswa. Total yang bekerja = $14 + 9 = 23$.
      <br>$P(\text{bekerja}) = \frac{23}{60} = \mathbf{0{,}3833 \approx 38{,}33\%}$.
    </li>
    <li><b>c) Peluang bersyarat per jurusan:</b>
      <br>$P(\text{bekerja} | \text{CS}) = \frac{14}{30} = \mathbf{0{,}4667 (46{,}67\%)}$. ← Pembaginya total CS = 30, bukan 60!
      <br>$P(\text{bekerja} | \text{IS}) = \frac{9}{30} = \mathbf{0{,}3000 (30{,}00\%)}$.
    </li>
    <li><b>d) Apakah status bekerja independen terhadap program studi?</b>
      <br>Cek: Kalau independen, $P(\text{bekerja} | \text{CS})$ HARUS sama dengan $P(\text{bekerja} | \text{IS})$ dan sama dengan $P(\text{bekerja})$.
      <br>Kenyataannya: $0{,}4667 \ne 0{,}3000$. <b>Tidak independen</b> — proporsi bekerja CS jauh lebih tinggi daripada IS.
    </li>
    <li><b>e) Tabel distribusi frekuensi 5 kelas dari 40 nilai ujian:</b>
      <br>Data: 52, 58, 61, 63, 64, 65, 67, 68, 68, 70, 71, 71, 72, 72, 73, 74, 74, 75, 75, 76, 77, 77, 78, 78, 79, 80, 80, 81, 82, 82, 83, 84, 85, 86, 87, 88, 89, 91, 94, 96.
      <br>Range $= 96 - 52 = 44$. Lebar kelas $w = 44 / 5 = 8{,}8 \to$ bulatkan ke atas $\to \mathbf{9}$.
      <br><b>Tabel:</b>
    </li>
  </ul>
  <div class="tblwrap"><table>
    <thead><tr><th>Kelas</th><th>Frekuensi ($f$)</th><th>Frek. Relatif ($f/n$)</th><th>Frek. Kumulatif</th></tr></thead>
    <tbody>
      <tr><td>52 – 60</td><td>2</td><td>0,050</td><td>2</td></tr>
      <tr><td>61 – 69</td><td>7</td><td>0,175</td><td>9</td></tr>
      <tr><td>70 – 78</td><td>16</td><td>0,400</td><td>25</td></tr>
      <tr><td>79 – 87</td><td>10</td><td>0,250</td><td>35</td></tr>
      <tr><td>88 – 96</td><td>5</td><td>0,125</td><td>40</td></tr>
      <tr><td><b>Total</b></td><td><b>40</b></td><td><b>1,000</b></td><td>-</td></tr>
    </tbody>
  </table></div>
  <ul class="tight">
    <li><b>f) Proporsi nilai $\ge 80$:</b> Kelas 79–87 punya frekuensi kumulatif sampai batas 78 = 25, maka yang $\ge$ 79 ada 40 − 25 = 15, tapi kita butuh $\ge 80$: data asli dari 80 ke atas ada <b>15 mahasiswa</b> (hitung manual dari data), maka $\frac{15}{40} = \mathbf{0{,}375 (37{,}5\%)}$.</li>
  </ul>

  <div class="self-test">
    <b>🆕 Study Case 1 — Ganti Angka &amp; Cerita:</b>
    <p>Survei 80 mahasiswa di 2 kampus (Kampus A &amp; B) soal apakah mereka menggunakan transportasi umum:</p>
    <div class="tblwrap"><table>
      <thead><tr><th>Kampus</th><th>Pakai TransJakarta</th><th>Tidak Pakai</th></tr></thead>
      <tbody>
        <tr><td><b>Kampus A</b></td><td>20</td><td>30</td></tr>
        <tr><td><b>Kampus B</b></td><td>18</td><td>12</td></tr>
      </tbody>
    </table></div>
    <p><b>Soal:</b> (a) Skala variabel "Kampus" dan "Pakai TransJakarta"? (b) $P(\text{Pakai})$? (c) $P(\text{Pakai} | \text{B})$? (d) Independen?</p>
    <button class="reveal-btn" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">Buka Kunci Jawaban</button>
    <div class="reveal-content">
      <p>Total: A = 50, B = 30, Grand = 80. Total pakai = 38.</p>
      <ul class="tight">
        <li>(a) Keduanya Nominal.</li>
        <li>(b) $P(\text{Pakai}) = 38 / 80 = \mathbf{0,475}$.</li>
        <li>(c) $P(\text{Pakai} | A) = 20/50 = 0,400$. $P(\text{Pakai} | B) = 18/30 = \mathbf{0,600}$.</li>
        <li>(d) <b>Tidak Independen</b>. $0,400 \ne 0,600$. Kampus B proporsi pakai lebih tinggi.</li>
      </ul>
    </div>
  </div>
</section>

<!-- ============ SOAL 2 ============ -->
<section class="sheet" id="u2">
  <div class="head"><div class="badge">2</div><div>
    <h2>Soal 2 · Mean, Variansi, IQR &amp; CV <span class="pts">20 poin</span></h2>
    <div class="sub">Waktu tunggu 15 pelanggan: 8, 10, 11, 12, 12, 13, 14, 15, 15, 16, 18, 20, 22, 24, 25</div>
  </div></div>

  <div class="sec">Langkah Hitung Rinci</div>
  <ul class="tight">
    <li><b>a) Mean ($\bar{x}$):</b>
      <br>$\Sigma X = 8 + 10 + 11 + \ldots + 25 = \mathbf{235}$.
      <br>$\bar{x} = \frac{\Sigma X}{n} = \frac{235}{15} = \mathbf{15,67 \text{ menit}}$.
    </li>
    <li><b>b) Median:</b>
      <br>Data sudah urut naik. $n = 15$ (ganjil). Posisi median $= \frac{15+1}{2} = 8$. Data ke-8 = <b>15 menit</b>.
    </li>
    <li><b>c) Modus:</b>
      <br>Angka 12 muncul 2 kali, angka 15 juga 2 kali. <b>Bimodal (12 dan 15)</b>.
    </li>
    <li><b>d) Variansi Sampel ($s^2$):</b>
      <br>$\Sigma X^2 = 8^2 + 10^2 + 11^2 + \ldots + 25^2 = 64 + 100 + 121 + 144 + 144 + 169 + 196 + 225 + 225 + 256 + 324 + 400 + 484 + 576 + 625 = \mathbf{4.053}$.
      <br>Rumus shortcut: $s^2 = \frac{\Sigma X^2 - \frac{(\Sigma X)^2}{n}}{n - 1} = \frac{4053 - \frac{235^2}{15}}{14} = \frac{4053 - \frac{55225}{15}}{14} = \frac{4053 - 3681,67}{14} = \frac{371,33}{14} = \mathbf{26,52}$.
      <br>$s = \sqrt{26,52} = \mathbf{5,15 \text{ menit}}$.
    </li>
    <li><b>e) Kuartil (Metode Levine) &amp; IQR:</b>
      <br>Posisi $Q_1 = \frac{n+1}{4} = \frac{16}{4} = 4 \to$ data ke-4 $= \mathbf{12}$.
      <br>Posisi $Q_3 = \frac{3(n+1)}{4} = \frac{48}{4} = 12 \to$ data ke-12 $= \mathbf{20}$.
      <br>$IQR = Q_3 - Q_1 = 20 - 12 = \mathbf{8 \text{ menit}}$.
    </li>
    <li><b>f) CV:</b>
      <br>$CV = \frac{s}{\bar{x}} \times 100\% = \frac{5,15}{15,67} \times 100\% = \mathbf{32,86\%}$. (Variabilitas sedang.)
    </li>
    <li><b>g) Deteksi Outlier:</b>
      <br>Pagar bawah $= Q_1 - 1,5 \times IQR = 12 - 12 = \mathbf{0}$.
      <br>Pagar atas $= Q_3 + 1,5 \times IQR = 20 + 12 = \mathbf{32}$.
      <br>Data minimum 8 $\ge$ 0 dan data maksimum 25 $\le$ 32, maka <b>tidak ada outlier</b>.
    </li>
    <li><b>h) Bentuk distribusi:</b>
      <br>Mean $15,67 >$ Median $15,00$. Artinya ekor data memanjang ke kanan $\to$ <b>menceng kanan (positif / right-skewed)</b>.
    </li>
  </ul>

  <div class="self-test">
    <b>🆕 Study Case 2 — Data Baru:</b>
    <p>Skor kepuasan pelanggan 11 orang: <b>3, 4, 5, 5, 6, 7, 7, 7, 8, 9, 15</b>.</p>
    <p><b>Soal:</b> (a) Mean, (b) Median, (c) Variansi sampel, (d) $Q_1$, $Q_3$, IQR, (e) Ada outlier?, (f) Menceng ke mana?</p>
    <button class="reveal-btn" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">Buka Kunci Jawaban</button>
    <div class="reveal-content">
      <ul class="tight">
        <li>(a) $\Sigma X = 76$, $\bar{x} = 76 / 11 = \mathbf{6,91}$.</li>
        <li>(b) $n = 11$ ganjil. Posisi $(11+1)/2 = 6$. Data ke-6 = <b>7</b>.</li>
        <li>(c) $\Sigma X^2 = 580$. $s^2 = (580 - 76^2/11) / 10 = (580 - 525,09) / 10 = 54,91 / 10 = \mathbf{5,49}$. $s = \mathbf{2,34}$.</li>
        <li>(d) $Q_1$ posisi $(11+1)/4 = 3 \to$ data ke-3 = <b>5</b>. $Q_3$ posisi $3 \times 12/4 = 9 \to$ data ke-9 = <b>8</b>. IQR $= 8 - 5 = \mathbf{3}$.</li>
        <li>(e) Pagar bawah $= 5 - 4,5 = 0,5$; pagar atas $= 8 + 4,5 = 12,5$. Nilai <b>15</b> $> 12,5$, maka <b>15 adalah outlier</b>!</li>
        <li>(f) Mean $6,91 <$ Median $7$. Tapi ada outlier di kanan... Sebenarnya $6,91 < 7$ menunjukkan distribusi yang kira-kira simetris, tapi outlier 15 di kanan menandakan ada ekor panjang kanan. Secara numeris strict: <b>menceng kiri sedikit</b> (mean < median), namun secara visual karena outlier di kanan, bentuknya <b>mendekati simetris dengan outlier kanan</b>. Di ujian, pakai acuan mean vs median: $\text{mean} < \text{median} \to$ <b>menceng kiri</b>.</li>
      </ul>
    </div>
  </div>
</section>

<!-- ============ SOAL 3 ============ -->
<section class="sheet" id="u3">
  <div class="head"><div class="badge">3</div><div>
    <h2>Soal 3 · Distribusi Probabilitas Diskrit <span class="pts">20 poin</span></h2>
    <div class="sub">Jumlah barang rusak per hari (X)</div>
  </div></div>

  <div class="tblwrap"><table>
    <thead><tr><th>X</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>Σ</th></tr></thead>
    <tbody><tr><td><b>P(X = x)</b></td><td>0,10</td><td>0,25</td><td>0,35</td><td>0,20</td><td>0,10</td><td><b>1,00</b></td></tr></tbody>
  </table></div>

  <div class="sec">Bedah Jawaban Lengkap</div>
  <ul class="tight">
    <li><b>a) Apakah distribusi ini sah / valid?</b>
      <br>Syarat: (1) Semua $P(x) \ge 0$ ✓ (semuanya positif). (2) $\sum P(x) = 0,10 + 0,25 + 0,35 + 0,20 + 0,10 = 1,00$ ✓.
      <br><b>Sah!</b>
    </li>
    <li><b>b) $P(X \ge 3)$:</b>
      <br>$X \ge 3$ artinya X = 3 atau X = 4 $\to P(3) + P(4) = 0,20 + 0,10 = \mathbf{0,30}$.
      <br>$P(X \le 1) = P(0) + P(1) = 0,10 + 0,25 = \mathbf{0,35}$.
    </li>
    <li><b>c) $P(1 < X \le 3)$:</b>
      <br>Perhatikan! Tanda "$<$" (bukan $\le$) berarti 1 <b>tidak ikut</b>. Yang masuk: $X = 2$ dan $X = 3$.
      <br>$P(2) + P(3) = 0,35 + 0,20 = \mathbf{0,55}$.
    </li>
    <li><b>d) Expected Value $E(X)$:</b>
      <br>$E(X) = \sum x \cdot P(x) = (0)(0,10) + (1)(0,25) + (2)(0,35) + (3)(0,20) + (4)(0,10)$
      <br>$= 0 + 0,25 + 0,70 + 0,60 + 0,40 = \mathbf{1,95 \text{ unit/hari}}$.
    </li>
    <li><b>e) Variansi $\text{Var}(X)$:</b>
      <br>$\sum x^2 P(x) = (0)(0,10) + (1)(0,25) + (4)(0,35) + (9)(0,20) + (16)(0,10) = 0 + 0,25 + 1,40 + 1,80 + 1,60 = \mathbf{5,05}$.
      <br>$\text{Var}(X) = 5,05 - (1,95)^2 = 5,05 - 3,8025 = \mathbf{1,2475}$.
      <br>$\sigma = \sqrt{1,2475} = \mathbf{1,117 \text{ unit}}$.
    </li>
    <li><b>f) Jika biaya harian $C = 10.000 + 25.000 \times X$:</b>
      <br>$E(C) = 10.000 + 25.000 \times E(X) = 10.000 + 25.000 \times 1,95 = 10.000 + 48.750 = \mathbf{Rp\,58.750}$.
    </li>
  </ul>

  <div class="self-test">
    <b>🆕 Study Case 3 — Binomial:</b>
    <p>Sebuah mesin produksi memiliki tingkat cacat 8% ($p = 0,08$). Diambil sampel acak $n = 5$ produk.</p>
    <p><b>Soal:</b> (a) $P(X = 0)$ (tidak ada yang cacat)? (b) $P(X \ge 2)$? (c) $E(X)$?</p>
    <button class="reveal-btn" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">Buka Kunci Jawaban</button>
    <div class="reveal-content">
      <ul class="tight">
        <li>(a) $P(X=0) = {}_5C_0 \times 0,08^0 \times 0,92^5 = 1 \times 1 \times 0,6591 = \mathbf{0,6591}$.</li>
        <li>(b) $P(X \ge 2) = 1 - P(0) - P(1) = 1 - 0,6591 - [{}_5C_1 \times 0,08 \times 0,92^4] = 1 - 0,6591 - [5 \times 0,08 \times 0,7164] = 1 - 0,6591 - 0,2866 = \mathbf{0,0543}$.</li>
        <li>(c) $E(X) = np = 5 \times 0,08 = \mathbf{0,40}$ (rata-rata 0,4 produk cacat per 5 sampel).</li>
      </ul>
    </div>
  </div>
</section>

<!-- ============ SOAL 4 ============ -->
<section class="sheet" id="u4">
  <div class="head"><div class="badge">4</div><div>
    <h2>Soal 4 · Distribusi Normal &amp; Z-Score <span class="pts">20 poin</span></h2>
    <div class="sub">Nilai ujian berdistribusi normal: μ = 72, σ = 8</div>
  </div></div>

  <div class="sec">Bedah Jawaban Lengkap</div>
  <ul class="tight">
    <li><b>a) $P(X < 60)$:</b>
      <br>Standarisasi: $Z = \frac{60 - 72}{8} = \frac{-12}{8} = \mathbf{-1,50}$.
      <br>Buka Tabel Z, baris $-1,5$ kolom $0,00 \to P(Z < -1,50) = \mathbf{0,0668}$.
      <br>Artinya <b>6,68%</b> mahasiswa nilainya di bawah 60.
    </li>
    <li><b>b) $P(60 < X < 80)$:</b>
      <br>$Z_{60} = -1,50 \to$ luas kiri $= 0,0668$.
      <br>$Z_{80} = \frac{80 - 72}{8} = \frac{8}{8} = +1,00 \to$ luas kiri $= 0,8413$.
      <br>$P(60 < X < 80) = 0,8413 - 0,0668 = \mathbf{0,7745 (77,45\%)}$.
    </li>
    <li><b>c) $P(X > 85)$:</b>
      <br>$Z = \frac{85 - 72}{8} = \frac{13}{8} = +1,63 \to$ luas kiri $= 0,9484$.
      <br>$P(X > 85) = 1 - 0,9484 = \mathbf{0,0516 (5,16\%)}$.
    </li>
    <li><b>d) Berapa batas nilai 10% mahasiswa teratas?</b>
      <br>10% teratas artinya 90% ada di bawahnya $\to$ cari luas kiri $= 0,9000$.
      <br>Di tabel Z: $Z \approx \mathbf{1,28}$ (baris 1,2 kolom 0,08 $\to$ 0,8997, paling dekat 0,9000).
      <br>Konversi balik: $X = \mu + Z \times \sigma = 72 + 1,28 \times 8 = 72 + 10,24 = \mathbf{82,24}$.
    </li>
    <li><b>e) $P(X < 58)$ (Tidak lulus):</b>
      <br>$Z = \frac{58 - 72}{8} = \frac{-14}{8} = -1,75 \to$ luas kiri $= \mathbf{0,0401 (4,01\%)}$.
    </li>
  </ul>

  <div class="trap-card">
    <b>⚠️ Jebakan "10% teratas":</b> Banyak mahasiswa langsung mencari angka $0,10$ di tabel Z. Padahal tabel memberikan <b>luas ke kiri</b>! Jadi yang harus dicari di tabel adalah $1 - 0,10 = 0,9000$ (luas KIRI dari batas teratas).
  </div>

  <div class="self-test">
    <b>🆕 Study Case 4 — Data Baru:</b>
    <p>Berat kemasan produk berdistribusi normal dengan $\mu = 500\text{g}$ dan $\sigma = 12\text{g}$.</p>
    <p><b>Soal:</b> (a) $P(X < 480)$? (b) $P(490 < X < 510)$? (c) Berapa batas berat agar masuk 5% terberat?</p>
    <button class="reveal-btn" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">Buka Kunci Jawaban</button>
    <div class="reveal-content">
      <ul class="tight">
        <li>(a) $Z = (480-500)/12 = -1,67 \to$ tabel $= \mathbf{0,0475 (4,75\%)}$.</li>
        <li>(b) $Z_{490} = -0,83 \to 0,2033$; $Z_{510} = +0,83 \to 0,7967$. Jawaban $= 0,7967 - 0,2033 = \mathbf{0,5934 (59,34\%)}$.</li>
        <li>(c) 5% terberat $\to$ luas kiri $= 0,9500 \to Z \approx 1,645$. $X = 500 + 1,645 \times 12 = 500 + 19,74 = \mathbf{519,74\text{g}}$.</li>
      </ul>
    </div>
  </div>
</section>

<!-- ============ SOAL 5 ============ -->
<section class="sheet" id="u5">
  <div class="head"><div class="badge">5</div><div>
    <h2>Soal 5 · Box Plot &amp; Interpretasi <span class="pts">20 poin</span></h2>
    <div class="sub">Five-Number Summary dua kelas</div>
  </div></div>

  <div class="tblwrap"><table>
    <thead><tr><th>Statistik</th><th>Kelas A</th><th>Kelas B</th></tr></thead>
    <tbody>
      <tr><td>Minimum</td><td>45</td><td>40</td></tr>
      <tr><td>$Q_1$</td><td>62</td><td>55</td></tr>
      <tr><td>Median ($Q_2$)</td><td>74</td><td>68</td></tr>
      <tr><td>$Q_3$</td><td>82</td><td>85</td></tr>
      <tr><td>Maksimum</td><td>95</td><td>98</td></tr>
    </tbody>
  </table></div>

  <div class="sec">Bedah Jawaban Lengkap</div>
  <ul class="tight">
    <li><b>a) IQR setiap kelas:</b>
      <br>$IQR_A = Q_3 - Q_1 = 82 - 62 = \mathbf{20}$; $IQR_B = 85 - 55 = \mathbf{30}$.
    </li>
    <li><b>b) Pagar outlier Kelas B:</b>
      <br>Lower Fence $= Q_1 - 1,5 \times IQR = 55 - 1,5(30) = 55 - 45 = \mathbf{10}$.
      <br>Upper Fence $= Q_3 + 1,5 \times IQR = 85 + 45 = \mathbf{130}$.
      <br>Data B: Min $40 \ge 10$ dan Maks $98 \le 130$, jadi <b>tidak ada outlier</b>.
    </li>
    <li><b>c) Kelas mana yang nilainya lebih tinggi?</b>
      <br>Bandingkan median: Kelas A median $74 >$ Kelas B median $68$. <b>Kelas A lebih tinggi</b>.
    </li>
    <li><b>d) Kelas mana yang lebih menyebar?</b>
      <br>Bandingkan IQR: Kelas B IQR $30 >$ Kelas A IQR $20$. <b>Kelas B lebih menyebar</b>.
    </li>
    <li><b>e) Sketsa Box Plot Kelas B:</b>
      <br>Kotak dari 55 s/d 85, garis median vertikal di 68, kumis kiri ke 40, kumis kanan ke 98. Tidak ada titik outlier.
    </li>
    <li><b>f) Bentuk distribusi Kelas B:</b>
      <br>Jarak median ke $Q_1$: $68 - 55 = 13$.
      <br>Jarak median ke $Q_3$: $85 - 68 = 17$.
      <br>Median lebih dekat ke $Q_1$ (13 < 17), artinya ada ekor yang lebih panjang ke arah kanan $\to$ <b>menceng kanan (positif)</b>.
    </li>
  </ul>

  <div class="self-test">
    <b>🆕 Study Case 5 — Data Baru:</b>
    <p>Data gaji bulanan (juta Rp) 9 karyawan: <b>3, 4, 5, 5, 6, 7, 8, 10, 22</b>.</p>
    <p><b>Soal:</b> (a) $Q_1$, $Q_3$, IQR? (b) Pagar outlier? (c) Ada outlier? (d) Bentuk distribusi?</p>
    <button class="reveal-btn" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">Buka Kunci Jawaban</button>
    <div class="reveal-content">
      <ul class="tight">
        <li>(a) $n = 9$. Posisi $Q_1 = (9+1)/4 = 2,5 \to$ rata-rata data ke-2 dan ke-3 $= (4+5)/2 = \mathbf{4,5}$. $Q_3$ posisi $7,5 \to (8+10)/2 = \mathbf{9}$. $IQR = 9 - 4,5 = \mathbf{4,5}$.</li>
        <li>(b) Lower $= 4,5 - 6,75 = -2,25$. Upper $= 9 + 6,75 = \mathbf{15,75}$.</li>
        <li>(c) $22 > 15,75 \to$ <b>22 adalah outlier!</b></li>
        <li>(d) Mean $= 70/9 = 7,78$, Median $= 6$. Mean $>$ Median $\to$ <b>menceng kanan</b> (diperkuat oleh adanya outlier 22 di kanan).</li>
      </ul>
    </div>
  </div>
</section>
</main>
"""

UTS_LEFT = r"""
<aside class="rail left" id="railLeft">
  <div class="panel">
    <h4>Navigasi Soal UTS</h4>
    <ul class="road" id="road">
      <li class="now"><span class="dot"></span><a href="#u0">Pengantar<small>Petunjuk Belajar</small></a></li>
      <li><span class="dot"></span><a href="#u1">Soal 1<small>Skala &amp; Tabel</small></a></li>
      <li><span class="dot"></span><a href="#u2">Soal 2<small>Mean, Var, IQR</small></a></li>
      <li><span class="dot"></span><a href="#u3">Soal 3<small>E(X) &amp; Binomial</small></a></li>
      <li><span class="dot"></span><a href="#u4">Soal 4<small>Z-Score</small></a></li>
      <li><span class="dot"></span><a href="#u5">Soal 5<small>Box Plot</small></a></li>
    </ul>
  </div>
  <div class="panel">
    <h4>Halaman Lain</h4>
    <a href="materi.html" style="display:block;margin-bottom:6px;color:var(--blue);font-weight:700">📖 1. Materi Lengkap →</a>
    <a href="kalkulator.html" style="display:block;color:var(--blue);font-weight:700">🖩 3. Kalkulator &amp; Latihan →</a>
  </div>
</aside>
"""

UTS_RIGHT = r"""
<aside class="rail right" id="railRight">
  <div class="panel info">
    <h4>Info UTS</h4>
    <div class="kv"><span>Jumlah Soal</span><b>5 Nomor</b></div>
    <div class="kv"><span>Total Poin</span><b>100 Poin</b></div>
    <div class="kv"><span>Sifat</span><b>Open Book (1 Lbr A4)</b></div>
    <div class="kv"><span>Kalkulator</span><b>Boleh (Scientific)</b></div>
  </div>
  <div class="panel">
    <h4>Rumus Cepat</h4>
    <div class="fb-block">P(A|B) = P(A∩B) / P(B)</div>
    <div class="fb-block">s² = [ΣX² − (ΣX)²/n] / (n−1)</div>
    <div class="fb-block">Z = (X − μ) / σ</div>
    <div class="fb-block">IQR = Q3 − Q1</div>
    <div class="fb-block">E(X) = Σ x·P(x)</div>
    <div class="fb-block">Var = Σx²P(x) − μ²</div>
  </div>
  <div class="panel">
    <h4>Kamus Kata Soal</h4>
    <div class="fb-block" style="font-size:12.5px;font-family:inherit">
      exactly = P(X = x)<br>
      at least = P(X ≥ x)<br>
      at most = P(X ≤ x)<br>
      more than = P(X > x)<br>
      fewer than = P(X < x)
    </div>
  </div>
</aside>
"""

uts_html = shell("Breakdown 5 Soal UTS · Basic Statistics",
                 UTS_LEFT + UTS_BODY + UTS_RIGHT, "", current_tab="uts")
(ROOT / "uts.html").write_text(uts_html, encoding="utf-8")
print(f"uts.html generated: {len(uts_html)} bytes")
