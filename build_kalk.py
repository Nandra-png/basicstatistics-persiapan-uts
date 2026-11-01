# -*- coding: utf-8 -*-
"""Builder Halaman 3: Tutorial Kalkulator Joyko CC-23 & Latihan Mandiri."""
import sys, pathlib

ROOT = pathlib.Path("C:/Users/rujak/Desktop/01-Kuliah/materi_binus/basicstatistics/persiapan_uts")
sys.path.insert(0, str(ROOT))
from make_site import shell, ROOT

KALK_BODY = r"""
<main>
<div class="nav-tabs">
  <a href="materi.html" class="nav-tab">📖 1. Materi Lengkap PPT</a>
  <a href="uts.html" class="nav-tab">🎯 2. Breakdown Soal UTS</a>
  <a href="kalkulator.html" class="nav-tab active">🖩 3. Kalkulator &amp; Latihan</a>
</div>

<section class="sheet" id="k0">
  <div class="kode">TUTORIAL JOYKO CC-23 / CASIO SERI MS &amp; DRILL MANDIRI</div>
  <h1 style="font-size:25px;font-weight:800;margin-top:4px">Tutorial Kalkulator &amp; Latihan Mandiri
    <br><span style="font-size:16px;font-weight:600;color:var(--ink-soft)">Kuasai Tuts Fisik Ujian + 10 Soal Prediksi UTS Lengkap dengan Kunci Jawaban</span></h1>
  
  <p style="margin:12px 0 16px;line-height:1.7">
    Ujian Basic Statistics memperbolehkan kalkulator scientific fisik. Jangan hitung manual $\Sigma X$ dan $\Sigma X^2$ satu per satu di kertas — lu bakal kehabisan waktu dan rawan salah ketik! Pelajari shortcut tombol mode statistik di bawah ini, lalu uji pemahaman lu di 10 soal latihan mandiri.
  </p>
</section>

<!-- TUTORIAL KALKULATOR -->
<section class="sheet" id="k1">
  <div class="head"><div class="badge">1</div><div>
    <h2>Mode Statistik Kalkulator (SD Mode)</h2>
    <div class="sub">Tuts Khusus Joyko CC-23, Casio fx-350MS, fx-570MS, fx-991MS</div>
  </div></div>

  <div class="sec">1. Cara Masuk ke Mode Statistik (SD Mode)</div>
  <div class="code">1. Tekan tombol [MODE] -> Muncul pilihan [1:COMP, 2:SD, 3:REG]
2. Tekan angka [2] -> Indikator "SD" kecil akan menyala di layar atas.
3. WAJIB RESET MEMORI STATISTIK SEBELUM MULAI:
   Tekan [SHIFT] -> [MODE] (CLR) -> [1] (Scl) -> [=]
   Layar akan menampilkan: "Stat Clear"</div>

  <div class="sec">2. Cara Memasukkan Data Angka Tunggal</div>
  <p>Misalkan data nilai ujian: <b>12, 15, 15, 18, 20</b></p>
  <div class="code">Ketik: 12 -> Tekan [M+]  -> Layar muncul: n=1
Ketik: 15 -> Tekan [M+]  -> Layar muncul: n=2
Ketik: 15 -> Tekan [M+]  -> Layar muncul: n=3
Ketik: 18 -> Tekan [M+]  -> Layar muncul: n=4
Ketik: 20 -> Tekan [M+]  -> Layar muncul: n=5</div>
  <p><i>Tips Cepat untuk Angka Kembar:</i> Kalau angka 15 muncul 2 kali, bisa ketik: <code>15 [SHIFT] [;] 2 [M+]</code></p>

  <div class="sec">3. Cara Mengeluarkan Hasil Langsung (Tanpa Hitung Manual!)</div>
  <div class="tblwrap"><table>
    <thead><tr><th>Nilai yang Dicari</th><th>Kombinasi Tombol</th><th>Simbol di Layar</th></tr></thead>
    <tbody>
      <tr><td><b>Rata-rata ($\bar{x}$)</b></td><td><code>[SHIFT] [2] (S-VAR) [1] [=]</code></td><td>$\bar{x}$</td></tr>
      <tr><td><b>Standar Deviasi Sampel ($s$)</b></td><td><code>[SHIFT] [2] (S-VAR) [3] [=]</code></td><td>$x\sigma_{n-1}$ atau $s$</td></tr>
      <tr><td><b>Standar Deviasi Populasi ($\sigma$)</b></td><td><code>[SHIFT] [2] (S-VAR) [2] [=]</code></td><td>$x\sigma_n$</td></tr>
      <tr><td><b>Jumlah Nilai ($\sum X$)</b></td><td><code>[SHIFT] [1] (S-SUM) [2] [=]</code></td><td>$\sum x$</td></tr>
      <tr><td><b>Jumlah Kuadrat Nilai ($\sum X^2$)</b></td><td><code>[SHIFT] [1] (S-SUM) [1] [=]</code></td><td>$\sum x^2$</td></tr>
      <tr><td><b>Banyaknya Data ($n$)</b></td><td><code>[SHIFT] [1] (S-SUM) [3] [=]</code></td><td>$n$</td></tr>
    </tbody>
  </table></div>

  <div class="trap-card">
    <b>⚠️ Jebakan Terbesar di Kalkulator:</b>
    <br>Saat menekan <code>[SHIFT] [2]</code>, ada dua pilihan standar deviasi:
    <br>• Angka <b>[2]</b> adalah $x\sigma_n$ (pembagi $N$ untuk populasi).
    <br>• Angka <b>[3]</b> adalah $x\sigma_{n-1}$ (pembagi $n-1$ untuk sampel).
    <br><b>UNTUK UTS BINUS: SELALU PAKAI NOMOR [3]</b> karena data soal adalah sampel acak ($n-1$)!
  </div>

  <div class="sec">4. Tombol Distribusi Khusus (Kombinasi &amp; Poisson)</div>
  <ul class="tight">
    <li><b>Kombinasi ${}_nC_r$ (Binomial &amp; Hypergeometric):</b>
      <br>Untuk menghitung ${}_6C_2$: Ketik <code>6 [nCr] 2 [=]</code> $\to$ Layar: <code>15</code>.
    </li>
    <li><b>Eksponensial $e^{-x}$ (Poisson):</b>
      <br>Untuk menghitung $e^{-3}$: Ketik <code>[SHIFT] [ln] (-) 3 [=]</code> $\to$ Layar: <code>0.049787</code>.
    </li>
    <li><b>Faktorial $x!$:</b>
      <br>Untuk menghitung $5!$: Ketik <code>5 [SHIFT] [x!] [=]</code> $\to$ Layar: <code>120</code>.
    </li>
  </ul>
</section>

<!-- LATIHAN MANDIRI -->
<section class="sheet" id="k2">
  <div class="head"><div class="badge">2</div><div>
    <h2>10 Soal Latihan Mandiri UTS (Self-Drill)</h2>
    <div class="sub">Kerjakan Sendiri di Kertas/Kalkulator, Buka Kunci Jawaban untuk Cek Hasil</div>
  </div></div>

  <!-- SOAL 1 -->
  <div class="self-test">
    <b>Soal 1 · Skala Pengukuran Data</b>
    <p>Seorang analis data mengumpulkan variabel berikut dari aplikasi e-commerce: (1) ID Pelanggan, (2) Rating Bintang Produk (1–5), (3) Suhu Ruang Server ($^\circ\text{C}$), (4) Total Belanja Bulanan (Rp). Tentukan skala pengukuran keempat variabel tersebut secara berurutan!</p>
    <button class="reveal-btn" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">Lihat Pembahasan &amp; Kunci</button>
    <div class="reveal-content">
      <p><b>Jawaban:</b> Nominal, Ordinal, Interval, Rasio.</p>
      <ul class="tight">
        <li>ID Pelanggan = <b>Nominal</b> (identitas/label).</li>
        <li>Rating Bintang = <b>Ordinal</b> (ada tingkat kepuasan, rentang tidak pasti sama).</li>
        <li>Suhu Celsius = <b>Interval</b> (punya urutan dan jarak pasti, tapi 0°C bukan ketiadaan suhu).</li>
        <li>Total Belanja = <b>Rasio</b> (0 rupiah berarti tidak belanja sama sekali, ada rasio kelipatan).</li>
      </ul>
    </div>
  </div>

  <!-- SOAL 2 -->
  <div class="self-test">
    <b>Soal 2 · Probabilitas Tabel Kontingensi</b>
    <p>Dalam sebuah kantor cabang bank, tercatat data 120 nasabah berdasarkan jenis tabungan dan kepemilikan kartu kredit:</p>
    <div class="tblwrap"><table>
      <thead><tr><th>Tabungan</th><th>Punya Kartu Kredit ($K$)</th><th>Tidak Punya ($K'$)</th></tr></thead>
      <tbody>
        <tr><td><b>Prioritas ($P$)</b></td><td>25</td><td>15</td></tr>
        <tr><td><b>Reguler ($R$)</b></td><td>20</td><td>60</td></tr>
      </tbody>
    </table></div>
    <p>Berapa nilai: (a) $P(K)$? (b) $P(K | P)$? (c) $P(P \cup K)$?</p>
    <button class="reveal-btn" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">Lihat Pembahasan &amp; Kunci</button>
    <div class="reveal-content">
      <ul class="tight">
        <li>Total baris Prioritas = $25 + 15 = 40$. Total Reguler = $20 + 60 = 80$. Grand Total = 120.</li>
        <li>Total Punya Kartu Kredit ($K$) = $25 + 20 = 45$.</li>
        <li><b>(a) $P(K) = \frac{45}{120} = \mathbf{0,375 (37,5\%)}$.</b></li>
        <li><b>(b) $P(K | P)$:</b> Fokus baris Prioritas (total 40). $P(K|P) = \frac{25}{40} = \mathbf{0,625 (62,5\%)}$.</li>
        <li><b>(c) $P(P \cup K) = P(P) + P(K) - P(P \cap K) = \frac{40}{120} + \frac{45}{120} - \frac{25}{120} = \frac{60}{120} = \mathbf{0,500 (50\%)}$.</b></li>
      </ul>
    </div>
  </div>

  <!-- SOAL 3 -->
  <div class="self-test">
    <b>Soal 3 · Mean, Median, Variansi &amp; CV Data Tunggal</b>
    <p>Data jumlah komplain harian selama 10 hari kerja: <b>4, 6, 7, 7, 8, 9, 10, 11, 12, 16</b>.</p>
    <p>Hitunglah: (a) Mean, (b) Median, (c) Variansi Sampel ($s^2$), (d) Koefisien Variasi ($CV$)!</p>
    <button class="reveal-btn" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">Lihat Pembahasan &amp; Kunci</button>
    <div class="reveal-content">
      <ul class="tight">
        <li>$\sum X = 90$, $n = 10 \to$ <b>Mean $\bar{x} = \frac{90}{10} = \mathbf{9,00}$ komplain</b>.</li>
        <li>Data sudah urut. Median $= \frac{\text{data ke-5} + \text{data ke-6}}{2} = \frac{8 + 9}{2} = \mathbf{8,50}$.</li>
        <li>$\sum X^2 = 16 + 36 + 49 + 49 + 64 + 81 + 100 + 121 + 144 + 256 = 916$.</li>
        <li>$s^2 = \frac{916 - \frac{90^2}{10}}{9} = \frac{916 - 810}{9} = \frac{106}{9} = \mathbf{11,78}$.</li>
        <li>$s = \sqrt{11,78} = \mathbf{3,43}$ komplain.</li>
        <li>$CV = \frac{3,43}{9,00} \times 100\% = \mathbf{38,11\%}$.</li>
      </ul>
    </div>
  </div>

  <!-- SOAL 4 -->
  <div class="self-test">
    <b>Soal 4 · Kuartil &amp; Uji Outlier Pagar 1,5 x IQR</b>
    <p>Dari data Soal 3 di atas: <b>4, 6, 7, 7, 8, 9, 10, 11, 12, 16</b> ($n = 10$).</p>
    <p>Tentukan: (a) $Q_1$, (b) $Q_3$, (c) $IQR$, (d) Apakah nilai 16 merupakan outlier?</p>
    <button class="reveal-btn" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">Lihat Pembahasan &amp; Kunci</button>
    <div class="reveal-content">
      <ul class="tight">
        <li>Posisi $Q_1 = \frac{n+1}{4} = \frac{11}{4} = 2,75 \to \text{Data ke-2} + 0,75(\text{Data ke-3} - \text{Data ke-2}) = 6 + 0,75(7 - 6) = \mathbf{6,75}$.</li>
        <li>Posisi $Q_3 = \frac{3(n+1)}{4} = \frac{33}{4} = 8,25 \to \text{Data ke-8} + 0,25(\text{Data ke-9} - \text{Data ke-8}) = 11 + 0,25(12 - 11) = \mathbf{11,25}$.</li>
        <li>$IQR = Q_3 - Q_1 = 11,25 - 6,75 = \mathbf{4,50}$.</li>
        <li>Pagar Atas $= Q_3 + 1,5 \times IQR = 11,25 + (1,5 \times 4,50) = 11,25 + 6,75 = \mathbf{18,00}$.</li>
        <li>Karena $16 < 18,00$, maka <b>nilai 16 BUKAN outlier</b>.</li>
      </ul>
    </div>
  </div>

  <!-- SOAL 5 -->
  <div class="self-test">
    <b>Soal 5 · Mean &amp; Standar Deviasi Data Berkelompok</b>
    <p>Tabel frekuensi waktu pengerjaan tugas (menit) dari 25 mahasiswa:</p>
    <div class="tblwrap"><table>
      <thead><tr><th>Kelas Waktu</th><th>Frekuensi ($f$)</th><th>Midpoint ($m$)</th><th>$f \cdot m$</th><th>$f \cdot m^2$</th></tr></thead>
      <tbody>
        <tr><td>20 – 29</td><td>5</td><td>24,5</td><td>122,5</td><td>3.001,25</td></tr>
        <tr><td>30 – 39</td><td>12</td><td>34,5</td><td>414,0</td><td>14.283,00</td></tr>
        <tr><td>40 – 49</td><td>8</td><td>44,5</td><td>356,0</td><td>15.842,00</td></tr>
        <tr><td><b>Total</b></td><td><b>$n = 25$</b></td><td>-</td><td><b>892,5</b></td><td><b>33.126,25</b></td></tr>
      </tbody>
    </table></div>
    <p>Hitunglah Mean ($\bar{x}$) dan Standar Deviasi ($s$) sampel data tersebut!</p>
    <button class="reveal-btn" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">Lihat Pembahasan &amp; Kunci</button>
    <div class="reveal-content">
      <ul class="tight">
        <li>Mean $\bar{x} = \frac{\sum f \cdot m}{n} = \frac{892,5}{25} = \mathbf{35,70\text{ menit}}$.</li>
        <li>Pembilang variansi $= \sum f \cdot m^2 - \frac{(\sum f \cdot m)^2}{n} = 33.126,25 - \frac{(892,5)^2}{25} = 33.126,25 - \frac{796.556,25}{25} = 33.126,25 - 31.862,25 = \mathbf{1.264,00}$.</li>
        <li>Penyebut $= n - 1 = 25 - 1 = 24$.</li>
        <li>$s^2 = \frac{1.264,00}{24} = \mathbf{52,67}$.</li>
        <li>Standar deviasi $s = \sqrt{52,67} = \mathbf{7,26\text{ menit}}$.</li>
      </ul>
    </div>
  </div>

  <!-- SOAL 6 -->
  <div class="self-test">
    <b>Soal 6 · Expected Value E(X) &amp; Var(X)</b>
    <p>Distribusi jumlah order kopi per meja di sebuah kafe ($X$):</p>
    <div class="tblwrap"><table>
      <thead><tr><th>x</th><th>1</th><th>2</th><th>3</th><th>4</th></tr></thead>
      <tbody><tr><td><b>P(X = x)</b></td><td>0,20</td><td>0,50</td><td>0,20</td><td>0,10</td></tr></tbody>
    </table></div>
    <p>Hitunglah Nilai Harapan $E(X)$ dan Variansi $\text{Var}(X)$!</p>
    <button class="reveal-btn" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">Lihat Pembahasan &amp; Kunci</button>
    <div class="reveal-content">
      <ul class="tight">
        <li>$E(X) = (1)(0,20) + (2)(0,50) + (3)(0,20) + (4)(0,10) = 0,20 + 1,00 + 0,60 + 0,40 = \mathbf{2,20\text{ cangkir}}$.</li>
        <li>$\sum x^2 P(x) = (1^2)(0,20) + (2^2)(0,50) + (3^2)(0,20) + (4^2)(0,10) = 0,20 + 2,00 + 1,80 + 1,60 = \mathbf{5,60}$.</li>
        <li>$\text{Var}(X) = 5,60 - (2,20)^2 = 5,60 - 4,84 = \mathbf{0,76}$.</li>
        <li>$\sigma = \sqrt{0,76} = \mathbf{0,87\text{ cangkir}}$.</li>
      </ul>
    </div>
  </div>

  <!-- SOAL 7 -->
  <div class="self-test">
    <b>Soal 7 · Distribusi Binomial</b>
    <p>Sebuah tes pilihan ganda memiliki 5 soal ($n = 5$), masing-masing 4 opsi jawaban ($p = 0,25$). Seorang mahasiswa menjawab murni dengan menebak acak. Berapa peluang ia menjawab <b>tepat 3 soal dengan benar</b>?</p>
    <button class="reveal-btn" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">Lihat Pembahasan &amp; Kunci</button>
    <div class="reveal-content">
      <ul class="tight">
        <li>${}_5C_3 = \frac{5!}{3! \cdot 2!} = 10$.</li>
        <li>$P(X = 3) = 10 \times (0,25)^3 \times (0,75)^{5 - 3} = 10 \times 0,015625 \times (0,75)^2 = 0,15625 \times 0,5625 = \mathbf{0,0879 (8,79\%)}$.</li>
      </ul>
    </div>
  </div>

  <!-- SOAL 8 -->
  <div class="self-test">
    <b>Soal 8 · Distribusi Poisson</b>
    <p>Rata-rata terdapat 2 kesalahan ketik per halaman naskah novel ($\lambda = 2$). Berapa peluang dalam satu halaman acak terdapat <b>tepat 1 kesalahan ketik</b>?</p>
    <button class="reveal-btn" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">Lihat Pembahasan &amp; Kunci</button>
    <div class="reveal-content">
      <ul class="tight">
        <li>$P(X = 1) = \frac{e^{-2} \times 2^1}{1!} = \frac{0,135335 \times 2}{1} = \mathbf{0,2707 (27,07\%)}$.</li>
      </ul>
    </div>
  </div>

  <!-- SOAL 9 -->
  <div class="self-test">
    <b>Soal 9 · Distribusi Normal Standar Z</b>
    <p>Daya tahan baterai ponsel berdistribusi normal dengan rata-rata $\mu = 14\text{ jam}$ dan simpangan baku $\sigma = 2\text{ jam}$. Berapa persentase baterai yang mampu bertahan <b>antara 11 jam hingga 17 jam</b>?</p>
    <button class="reveal-btn" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">Lihat Pembahasan &amp; Kunci</button>
    <div class="reveal-content">
      <ul class="tight">
        <li>$Z_{11} = \frac{11 - 14}{2} = -1,50 \to$ Luas kiri tabel Z $= \mathbf{0,0668}$.</li>
        <li>$Z_{17} = \frac{17 - 14}{2} = +1,50 \to$ Luas kiri tabel Z $= \mathbf{0,9332}$.</li>
        <li>$P(11 < X < 17) = P(Z < 1,50) - P(Z < -1,50) = 0,9332 - 0,0668 = \mathbf{0,8664 (86,64\%)}$.</li>
      </ul>
    </div>
  </div>

  <!-- SOAL 10 -->
  <div class="self-test">
    <b>Soal 10 · Nilai Ambang Z Balik (Inverse Normal)</b>
    <p>Masih dari data baterai ponsel di Soal 9 ($\mu = 14$, $\sigma = 2$). Produsen ingin memberikan garansi ganti baru untuk <b>2,5% ponsel dengan daya tahan baterai terpendek</b>. Berapa jam batas daya tahan maksimum agar masih memenuhi syarat garansi?</p>
    <button class="reveal-btn" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">Lihat Pembahasan &amp; Kunci</button>
    <div class="reveal-content">
      <ul class="tight">
        <li>2,5% terpendek berada di ekor kiri paling bawah $\to$ Cari luas tabel $= 0,0250$.</li>
        <li>Di tabel Z: nilai luas $0,0250$ persis berada pada baris $-1,9$ kolom $0,06 \to Z = \mathbf{-1,96}$.</li>
        <li>Konversi balik ke nilai jam $X$:</li>
        <li>$X = \mu + Z \times \sigma = 14 + (-1,96 \times 2) = 14 - 3,92 = \mathbf{10,08\text{ jam}}$.</li>
        <li><i>Kesimpulan: Baterai yang bertahan kurang dari <b>10,08 jam</b> berhak klaim garansi.</i></li>
      </ul>
    </div>
  </div>
</section>
</main>
"""

KALK_LEFT = r"""
<aside class="rail left" id="railLeft">
  <div class="panel">
    <h4>Navigasi Halaman</h4>
    <ul class="road" id="road">
      <li class="now"><span class="dot"></span><a href="#k0">Pengantar<small>Trik Kalkulator</small></a></li>
      <li><span class="dot"></span><a href="#k1">Panduan Tuts<small>Mode SD &amp; Shortcut</small></a></li>
      <li><span class="dot"></span><a href="#k2">10 Latihan<small>Drill Mandiri UTS</small></a></li>
    </ul>
  </div>
  <div class="panel">
    <h4>Halaman Lain</h4>
    <a href="materi.html" style="display:block;margin-bottom:6px;color:var(--blue);font-weight:700">📖 1. Materi Lengkap →</a>
    <a href="uts.html" style="display:block;color:var(--red);font-weight:700">🎯 2. Breakdown UTS →</a>
  </div>
</aside>
"""

KALK_RIGHT = r"""
<aside class="rail right" id="railRight">
  <div class="panel info">
    <h4>Info Ujian</h4>
    <div class="kv"><span>Tipe Alat</span><b>Kalkulator Fisik</b></div>
    <div class="kv"><span>Model</span><b>Joyko / Casio MS</b></div>
    <div class="kv"><span>Latihan</span><b>10 Butir Mandiri</b></div>
    <div class="kv"><span>Solusi</span><b>Revealable Step</b></div>
  </div>
  <div class="panel">
    <h4>Sekuens Tombol</h4>
    <div class="fb-block" style="font-size:12px;font-family:inherit">
      • Masuk: <code>MODE 2</code><br>
      • Reset: <code>SHIFT MODE 1 =</code><br>
      • Input: <code>angka M+</code><br>
      • Rata-rata: <code>SHIFT 2 1 =</code><br>
      • Deviasi Sampel: <code>SHIFT 2 3 =</code>
    </div>
  </div>
  <div class="panel">
    <h4>Tips Ujian</h4>
    <div class="fb-block" style="font-size:12.5px;font-family:inherit">
      Selalu cek indikator "SD" di atas layar sebelum input data! Kalau lupa reset, data dari soal sebelumnya bakal kecampur.
    </div>
  </div>
</aside>
"""

kalk_html = shell("Tutorial Kalkulator & 10 Latihan Mandiri · Basic Statistics",
                  KALK_LEFT + KALK_BODY + KALK_RIGHT, "", current_tab="kalkulator")
(ROOT / "kalkulator.html").write_text(kalk_html, encoding="utf-8")
print(f"kalkulator.html generated: {len(kalk_html)} bytes")
