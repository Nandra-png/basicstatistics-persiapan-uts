# -*- coding: utf-8 -*-
"""Builder Halaman 2: Rangkuman Modul UTS Basic Statistics.
UI 3-kolom identik materi.html: aside.rail.left | main | aside.rail.right.
"""
import pathlib, sys

ROOT = pathlib.Path(r"C:\Users\rujak\Desktop\01-Kuliah\materi_binus\basicstatistics\persiapan_uts")
sys.path.insert(0, str(ROOT))
from make_site import shell

BODY = r"""
<aside class="rail left" id="railLeft">
  <div class="panel">
    <h4>Navigasi Rangkuman</h4>
    <ul class="road" id="road">
      <li class="now"><span class="dot"></span><a href="#r0">Peta UTS<small>Kisi-kisi &amp; Rubrik</small></a></li>
      <li><span class="dot"></span><a href="#r1">Bab 1 · NOIR<small>Skala &amp; Sampling</small></a></li>
      <li><span class="dot"></span><a href="#r2">Bab 2–3 · Statistik<small>Mean, IQR, Outlier</small></a></li>
      <li><span class="dot"></span><a href="#r3">Bab 4 · Probabilitas<small>Tabel &amp; Independensi</small></a></li>
      <li><span class="dot"></span><a href="#r4">Bab 5 · Diskrit<small>Binom, Pois, Hiper</small></a></li>
      <li><span class="dot"></span><a href="#r5">Bab 6 · Normal Z<small>Kurva Z &amp; Luas</small></a></li>
      <li><span class="dot"></span><a href="#r6">Contekan A4<small>Tips Open Notes</small></a></li>
    </ul>
  </div>
  <div class="panel">
    <h4>Daftar Halaman</h4>
    <a href="materi.html" style="display:block;margin-bottom:6px;color:var(--ink);font-weight:700">📖 1. Materi PPT →</a>
    <a href="uts.html" style="display:block;margin-bottom:6px;color:var(--red);font-weight:700">🎯 3. Breakdown UTS →</a>
    <a href="kalkulator.html" style="display:block;color:var(--blue);font-weight:700">🖩 4. Kalkulator &amp; Latihan →</a>
  </div>
</aside>

<main>
<div class="nav-tabs"></div>

<!-- HEADER -->
<section class="sheet" id="r0">
  <div class="kode">STAT6190031 · MODUL UTS BASIC STATISTICS · BINUS UNIVERSITY</div>
  <h1 style="font-size:26px;font-weight:800;margin-top:4px">Rangkuman Inti Modul UTS (Bab 1 – 6)
    <br><span style="font-size:16px;font-weight:600;color:var(--ink-soft)">Ekstrak Lengkap Modul UTS + Textbook Levine 9e + Soal Latihan</span></h1>
  <p style="margin:12px 0 16px;line-height:1.75">
    Halaman ini merangkum seluruh isi <b>Modul_UTS_Basic_Statistics.pdf</b> ke dalam format paper-sheet bergaris.
    Format penjelasan: <b>Peta UTS → Konsep Inti → Rumus Cepat → Jebakan Dosen → Template Kalimat Kesimpulan</b>.
    Cocok banget buat bahan bikin <b>1 lembar A4 contekan tulis tangan bolak-balik</b> yang diizinkan pas ujian!
  </p>

  <div class="sec">Peta Kisi-Kisi UTS &amp; Bobot Soal</div>
  <div class="tblwrap"><table>
    <thead><tr><th>No. Soal</th><th>Bab Materi</th><th>Tipe Soal</th><th>Kunci Jawaban yang Dinilai Dosen</th></tr></thead>
    <tbody>
      <tr><td><b>Soal 1</b></td><td>Bab 1</td><td>Klasifikasi Variabel &amp; Sampling</td><td>Tipe data (kategorik/numerik), skala (NOIR), nama sampling, 4 survey error.</td></tr>
      <tr><td><b>Soal 2</b></td><td>Bab 2 &amp; 3</td><td>Tabel Kontingensi &amp; Peluang Dasar</td><td>Baca sel gabungan, marginal, $P(A \cup B)$, $P(B|A)$, uji independensi $P(A \cap B) = P(A)P(B)$.</td></tr>
      <tr><td><b>Soal 3</b></td><td>Bab 3</td><td>Ukuran Pemusatan &amp; Sebaran</td><td>Mean, Median, Modus, Varians ($s^2$), Standar Deviasi ($s$), CV, Deteksi Outlier ($1{,}5 \times IQR$).</td></tr>
      <tr><td><b>Soal 4</b></td><td>Bab 4 / 5</td><td>Distribusi Diskrit</td><td>Pilih model yang pas: <b>Binomial</b> (n tetap, 2 hasil), <b>Poisson</b> (per satuan waktu), <b>Hipergeometrik</b> (tanpa kembali).</td></tr>
      <tr><td><b>Soal 5</b></td><td>Bab 6</td><td>Distribusi Normal &amp; Z-Score</td><td>Standarisasi $Z = (X-\mu)/\sigma$, baca luas tabel Z kiri, konversi balik $X = \mu + Z\sigma$.</td></tr>
      <tr><td><b>Soal 6</b></td><td>Review</td><td>Membaca Boxplot &amp; Skewness</td><td>Pusat (median), sebaran (IQR), arah kemiringan (mean vs median, whisker), outlier titik.</td></tr>
    </tbody>
  </table></div>

  <div class="note">
    <b>Format Jawaban Aman (Rubrik Excellent):</b>
    <br>(1) Tulis rumus baku → (2) Substitusi angka → (3) Hitung hasil → (4) <b>Kalimat kesimpulan dalam konteks soal!</b>
  </div>
</section>

<!-- BAB 1 -->
<section class="sheet" id="r1">
  <div class="head"><div class="badge">1</div><div>
    <h2>Bab 1 · Defining &amp; Collecting Data</h2>
    <div class="sub">Klasifikasi Variabel, Skala NOIR, Teknik Sampling, Survey Errors</div>
  </div></div>

  <div class="sec">1. Pohon Klasifikasi Variabel</div>
  <div class="tblwrap"><table>
    <thead><tr><th>Klasifikasi</th><th>Sub-Tipe</th><th>Definisi</th><th>Contoh Ujian</th></tr></thead>
    <tbody>
      <tr>
        <td rowspan="2"><b>Kategorik</b><br><small>Label / kelompok</small></td>
        <td><b>Nominal</b></td>
        <td>Nama label pembeda, tanpa urutan.</td>
        <td>Jenis kelamin, merek HP, jurusan, NIM.</td>
      </tr>
      <tr>
        <td><b>Ordinal</b></td>
        <td>Kategori punya urutan, selisih tidak pasti.</td>
        <td>Rating 1–5, ukuran S/M/L/XL, ranking.</td>
      </tr>
      <tr>
        <td rowspan="2"><b>Numerik</b><br><small>Angka hitung / ukur</small></td>
        <td><b>Diskrit</b></td>
        <td>Hasil <b>MENGHITUNG</b> (bilangan bulat).</td>
        <td>Jumlah keluhan, banyak SMS, jumlah bug.</td>
      </tr>
      <tr>
        <td><b>Kontinu</b></td>
        <td>Hasil <b>MENGUKUR</b> (bisa desimal).</td>
        <td>Waktu download, suhu °C, berat kg.</td>
      </tr>
    </tbody>
  </table></div>

  <div class="sec">2. Skala Pengukuran NOIR</div>
  <ul class="tight">
    <li><b>Nominal:</b> Cuma label pembeda, tidak bisa diurutkan.</li>
    <li><b>Ordinal:</b> Punya urutan, jarak antar peringkat tidak bermakna pasti.</li>
    <li><b>Interval:</b> Jarak bermakna, <b>tapi NOL BUKAN mutlak</b>. Contoh: Suhu $0^\circ$C masih ada panas.</li>
    <li><b>Rasio:</b> Jarak bermakna DAN <b>NOL = ketiadaan total</b>. Contoh: Rp 0 = tidak ada uang.</li>
  </ul>

  <div class="sec">3. Metode Sampling</div>
  <div class="tblwrap"><table>
    <thead><tr><th>Metode</th><th>Cara Kerja</th><th>Keunggulan / Kelemahan</th></tr></thead>
    <tbody>
      <tr><td><b>Simple Random</b></td><td>Peluang sama rata, acak murni.</td><td>Adil; butuh daftar lengkap populasi.</td></tr>
      <tr><td><b>Systematic</b></td><td>$k = N / n$, ambil setiap ke-$k$.</td><td>Praktis; bahaya pola tersembunyi.</td></tr>
      <tr><td><b>Stratified</b></td><td>Bagi jadi strata homogen, acak dari tiap strata.</td><td>Minoritas terwakili proporsional.</td></tr>
      <tr><td><b>Cluster</b></td><td>Pilih acak beberapa gugus, ambil semua di dalamnya.</td><td>Hemat; variansi estimasi lebih besar.</td></tr>
    </tbody>
  </table></div>

  <div class="sec">4. Empat Survey Errors</div>
  <ul class="tight">
    <li><b>Coverage Error:</b> Kelompok populasi tidak terdaftar di kerangka sampel.</li>
    <li><b>Nonresponse Error:</b> Responden menolak / tidak bisa dihubungi.</li>
    <li><b>Sampling Error:</b> Selisih alami hasil sampel vs parameter populasi.</li>
    <li><b>Measurement Error:</b> Pertanyaan ambigu, alat rusak, responden bohong.</li>
  </ul>
</section>

<!-- BAB 2 & 3 -->
<section class="sheet" id="r2">
  <div class="head"><div class="badge">2</div><div>
    <h2>Bab 2 &amp; 3 · Tabel Frekuensi &amp; Ukuran Statistik</h2>
    <div class="sub">Distribusi Frekuensi, Mean, Median, Kuartil, Varians, Std Dev, CV, Outlier</div>
  </div></div>

  <div class="sec">1. Tabel Distribusi Frekuensi Kelompok</div>
  <ol class="tight">
    <li><b>Range:</b> $R = X_{\max} - X_{\min}$</li>
    <li><b>Banyak Kelas:</b> $k = 1 + 3{,}322 \log_{10}(n)$ (bulatkan ke atas).</li>
    <li><b>Lebar Kelas:</b> $w = R / k$ (bulatkan ke atas).</li>
  </ol>

  <div class="sec">2. Ukuran Pemusatan</div>
  <ul class="tight">
    <li><b>Mean Sampel:</b> $\bar{x} = \frac{\sum x_i}{n}$ — Sensitif outlier.</li>
    <li><b>Median:</b> Urut kecil → besar, posisi $= \frac{n + 1}{2}$ — Tahan outlier.</li>
    <li><b>Modus:</b> Nilai yang frekuensinya terbanyak.</li>
  </ul>

  <div class="sec">3. Kuartil, IQR, Deteksi Outlier</div>
  <div class="formula-card">
    <b>Posisi Kuartil:</b>
    <br>$Q_1 = \frac{n + 1}{4}$ &nbsp;|&nbsp; $Q_2 = \frac{n + 1}{2}$ &nbsp;|&nbsp; $Q_3 = \frac{3(n + 1)}{4}$
    <br><br>
    <b>Interquartile Range:</b> $$IQR = Q_3 - Q_1$$
    <b>Pagar Outlier:</b>
    <br>Batas Bawah $= Q_1 - 1{,}5 \times IQR$ &nbsp;|&nbsp; Batas Atas $= Q_3 + 1{,}5 \times IQR$
    <br><i>Data di luar interval ini dinyatakan <b>OUTLIER</b>!</i>
  </div>

  <div class="sec">4. Varians, Standar Deviasi, CV</div>
  <div class="formula-card">
    $$s^2 = \frac{\sum x_i^2 - \frac{(\sum x_i)^2}{n}}{n - 1} \quad \Longleftrightarrow \quad s = \sqrt{s^2}$$
    <b>Koefisien Variasi:</b>
    $$CV = \left(\frac{s}{\bar{x}}\right) \times 100\%$$
    <i>CV makin kecil = data makin konsisten / stabil.</i>
  </div>
</section>

<!-- BAB 4 -->
<section class="sheet" id="r3">
  <div class="head"><div class="badge">3</div><div>
    <h2>Bab 4 · Probabilitas &amp; Tabel Kontingensi</h2>
    <div class="sub">Tabel Silang 2×2, Peluang Marginal, Joint, Bersyarat, Uji Independensi</div>
  </div></div>

  <div class="sec">1. Cara Baca Tabel Kontingensi 2×2</div>
  <div class="tblwrap"><table>
    <thead><tr><th></th><th>$B$</th><th>$B^c$</th><th>Total</th></tr></thead>
    <tbody>
      <tr><td><b>$A$</b></td><td>$n(A \cap B)$ [Joint]</td><td>$n(A \cap B^c)$</td><td><b>$n(A)$ [Marginal]</b></td></tr>
      <tr><td><b>$A^c$</b></td><td>$n(A^c \cap B)$</td><td>$n(A^c \cap B^c)$</td><td><b>$n(A^c)$</b></td></tr>
      <tr><td><b>Total</b></td><td><b>$n(B)$</b></td><td><b>$n(B^c)$</b></td><td><b>$N$</b></td></tr>
    </tbody>
  </table></div>

  <div class="sec">2. Kamus Rumus Peluang</div>
  <ul class="tight">
    <li><b>Marginal:</b> $P(A) = \frac{n(A)}{N}$</li>
    <li><b>Joint (DAN):</b> $P(A \cap B) = \frac{n(A \cap B)}{N}$</li>
    <li><b>Gabungan (ATAU):</b> $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$</li>
    <li><b>Bersyarat (JIKA):</b> $$P(B \mid A) = \frac{P(A \cap B)}{P(A)} = \frac{n(A \cap B)}{n(A)}$$
      <i>Pembagi berubah ke total baris $A$, bukan $N$!</i></li>
    <li><b>Uji Independensi:</b>
      $$P(A \cap B) = P(A) \times P(B) \quad \text{atau} \quad P(B \mid A) = P(B)$$
      Jika tidak sama → <b>DEPENDEN</b>.</li>
  </ul>
</section>

<!-- BAB 5 -->
<section class="sheet" id="r4">
  <div class="head"><div class="badge">4</div><div>
    <h2>Bab 5 · Distribusi Peluang Diskrit</h2>
    <div class="sub">E(X), Var(X), Binomial, Poisson, Hipergeometrik</div>
  </div></div>

  <div class="sec">1. Nilai Harapan &amp; Varians</div>
  <div class="formula-card">
    $$\mu = E(X) = \sum [x_i \cdot P(X = x_i)]$$
    $$\sigma^2 = \sum [x_i^2 \cdot P(X = x_i)] - [E(X)]^2$$
    <i>Syarat: $0 \le P(x) \le 1$ dan $\sum P(x) = 1$.</i>
  </div>

  <div class="sec">2. Pohon Keputusan Distribusi Diskrit</div>
  <div class="tblwrap"><table>
    <thead><tr><th>Distribusi</th><th>Ciri Khas Soal</th><th>$P(X = k)$</th><th>Mean &amp; Var</th></tr></thead>
    <tbody>
      <tr>
        <td><b>Binomial</b><br><small>🏷️ VENOM-BINOM</small></td>
        <td>$n$ percobaan tetap, 2 hasil, peluang $\pi$ konstan (<b>dengan pengembalian</b>).</td>
        <td>$$\binom{n}{k} \pi^k (1 - \pi)^{n - k}$$</td>
        <td>$E = n\pi$<br>$V = n\pi(1 - \pi)$</td>
      </tr>
      <tr>
        <td><b>Poisson</b><br><small>🏷️ CROISSANT-POIS</small></td>
        <td>Kejadian langka <b>per satuan waktu/luas</b> (rata-rata $\lambda$).</td>
        <td>$$\frac{e^{-\lambda} \cdot \lambda^k}{k!}$$</td>
        <td>$E = \lambda$<br>$V = \lambda$</td>
      </tr>
      <tr>
        <td><b>Hipergeometrik</b><br><small>🏷️ KARTU-HIPER</small></td>
        <td>$N$ populasi, $A$ sukses, ambil $n$ <b>tanpa pengembalian</b>.</td>
        <td>$$\frac{\binom{A}{k} \binom{N - A}{n - k}}{\binom{N}{n}}$$</td>
        <td>$E = n(A/N)$</td>
      </tr>
    </tbody>
  </table></div>

  <div class="note">
    <b>Jalan Pintas Komplemen:</b> $P(X \ge 1) = 1 - P(X = 0)$. Jangan hitung satu per satu!
  </div>
</section>

<!-- BAB 6 -->
<section class="sheet" id="r5">
  <div class="head"><div class="badge">5</div><div>
    <h2>Bab 6 · Distribusi Normal &amp; Z-Score</h2>
    <div class="sub">Standarisasi, 3 Pola Luas Tabel Z, Persentil Konversi Balik</div>
  </div></div>

  <div class="sec">1. Standarisasi Z</div>
  <div class="formula-card">
    $$Z = \frac{X - \mu}{\sigma} \quad \Longleftrightarrow \quad X = \mu + Z \cdot \sigma$$
    <i>$Z$ = berapa standar deviasi posisi $X$ dari rata-rata.</i>
  </div>

  <div class="sec">2. Tiga Pola Membaca Tabel Z (Cumulative Left Tail)</div>
  <div class="tblwrap"><table>
    <thead><tr><th>Pertanyaan</th><th>Rumus</th><th>Cara Hitung</th></tr></thead>
    <tbody>
      <tr>
        <td><b>Kurang dari</b></td>
        <td>$P(X < a) = P(Z < z)$</td>
        <td>Langsung baca tabel Z.</td>
      </tr>
      <tr>
        <td><b>Lebih dari</b></td>
        <td>$P(X > a) = P(Z > z)$</td>
        <td>$1 - P(Z < z)$</td>
      </tr>
      <tr>
        <td><b>Di antara</b></td>
        <td>$P(a < X < b)$</td>
        <td>$P(Z < z_2) - P(Z < z_1)$</td>
      </tr>
    </tbody>
  </table></div>

  <div class="sec">3. Mencari Batas $X$ dari Persentil</div>
  <div class="worked">
    <h4>Langkah Cari Nilai X (Top k%)</h4>
    <ol class="tight">
      <li>Top 10% → luas kiri = 0,9000. Cari angka itu di badan tabel Z → $Z \approx 1{,}28$.</li>
      <li>$X = \mu + Z \cdot \sigma$.</li>
    </ol>
  </div>
</section>

<!-- CONTEKAN A4 -->
<section class="sheet" id="r6">
  <div class="head"><div class="badge">6</div><div>
    <h2>Panduan Contekan 1 Lembar A4 (Tulis Tangan)</h2>
    <div class="sub">Strategi Menyusun Open Notes Bolak-Balik Sesuai Aturan Ujian</div>
  </div></div>

  <p>Ujian mengizinkan <b>1 lembar A4 tulis tangan bolak-balik</b>. Jangan buang tempat buat kalimat panjang; tulis <b>Rumus Baku + Bagan Alur + Nilai Z Kunci</b>!</p>

  <div class="grid2">
    <div class="fb-block">
      <b>Sisi Depan (Bab 1, 2, 3):</b>
      <ul class="tight">
        <li>NOIR: Nominal, Ordinal, Interval, Rasio.</li>
        <li>Sturges: $k = 1 + 3{,}322 \log_{10}(n)$, $w = R/k$.</li>
        <li>Kuartil: $Q_1 = (n+1)/4$, $Q_3 = 3(n+1)/4$.</li>
        <li>Outlier: $Q_1 - 1{,}5 \times IQR$ dan $Q_3 + 1{,}5 \times IQR$.</li>
        <li>Varians: $s^2 = [\sum X^2 - (\sum X)^2 / n] / (n - 1)$.</li>
        <li>CV: $(s / \bar{x}) \times 100\%$.</li>
        <li>Bersyarat: $P(B|A) = P(A \cap B) / P(A)$.</li>
        <li>Independen: $P(A \cap B) = P(A) \cdot P(B)$.</li>
      </ul>
    </div>
    <div class="fb-block">
      <b>Sisi Belakang (Bab 4, 5, 6):</b>
      <ul class="tight">
        <li>Binom: $\binom{n}{k} \pi^k (1-\pi)^{n-k}$, $\mu=n\pi$.</li>
        <li>Poisson: $(e^{-\lambda} \lambda^k)/k!$, $\mu=\lambda, \sigma^2=\lambda$.</li>
        <li>Hiper: $[\binom{A}{k}\binom{N-A}{n-k}] / \binom{N}{n}$.</li>
        <li>Z-score: $Z = (X - \mu)/\sigma$, $X = \mu + Z\sigma$.</li>
        <li>Nilai Z Penting:<br>
          90% → 1,28 · 95% → 1,645 · 97,5% → 1,96 · 99% → 2,33</li>
        <li>Template Kesimpulan: subjek + persentase + satuan.</li>
      </ul>
    </div>
  </div>
</section>

</main>

<aside class="rail right" id="railRight">
  <div class="panel info">
    <h4>Info Dokumen</h4>
    <div class="kv"><span>Sumber</span><b>Modul UTS PDF</b></div>
    <div class="kv"><span>Matkul</span><b>Basic Statistics</b></div>
    <div class="kv"><span>Kode</span><b>STAT6190031</b></div>
    <div class="kv"><span>Textbook</span><b>Levine 9e</b></div>
    <div class="kv"><span>Sifat</span><b>Open Book (1 Lbr A4)</b></div>
    <div class="kv"><span>Dosen</span><b>Dr. Dani Suandi</b></div>
  </div>
  <div class="panel">
    <h4>Kunci Rumus Cepat</h4>
    <div class="fb-block" style="font-size:13px;font-family:inherit">
      <b>IQR</b> = Q₃ − Q₁<br>
      <b>Outlier Bawah</b> = Q₁ − 1,5·IQR<br>
      <b>Outlier Atas</b> = Q₃ + 1,5·IQR<br>
      <b>Z</b> = (X − μ) / σ
    </div>
  </div>
  <div class="panel">
    <h4>Jebakan Ujian ⚠️</h4>
    <div class="fb-block" style="font-size:12px;font-family:inherit;margin:0;padding:6px 8px">
      • <b>NIM / No Telp:</b> Nominal, bukan Rasio.<br>
      • <b>Suhu Celsius:</b> Interval, bukan Rasio.<br>
      • <b>P(A|B):</b> Pembagi = total B, bukan Grand Total!<br>
      • <b>Varians sampel:</b> Bagi $n-1$, bukan $n$!<br>
      • <b>Per Jam</b> = Poisson. <b>Tanpa Ganti</b> = Hiper.
    </div>
  </div>
  <div class="panel">
    <h4>🖩 Tips Kalkulator Casio</h4>
    <div class="fb-block" style="font-size:12px;font-family:inherit;margin:0;padding:6px 8px">
      Menu → 6 (Statistics) → 1-Variable.<br>
      Isi angka, tekan <b>OPTN → 2</b> → langsung dapat x̄, Σx, Σx², s², s tanpa hitung manual!
    </div>
  </div>
</aside>
"""

script = """
console.log('Rangkuman Modul UTS loaded with native clean math.');
"""

out = shell("Rangkuman Lengkap Modul UTS Basic Statistics | BINUS",
            BODY, script, current_tab="rangkuman")
path = ROOT / "rangkuman.html"
path.write_text(out, encoding="utf-8")
print(f"rangkuman.html generated: {len(out):,} bytes")
