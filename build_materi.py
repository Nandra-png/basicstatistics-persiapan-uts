# -*- coding: utf-8 -*-
"""Builder lengkap 3 halaman materi UTS Basic Statistics."""
import sys, json, pathlib

ROOT = pathlib.Path("C:/Users/rujak/Desktop/01-Kuliah/materi_binus/basicstatistics/persiapan_uts")
sys.path.insert(0, str(ROOT))
from make_site import shell, ROOT

# ==============================================================================
# 1. MATERI LENGKAP PPT (materi.html)
# ==============================================================================
MATERI_BODY = r"""
<main>
<div class="nav-tabs">
  <a href="materi.html" class="nav-tab active">📖 1. Materi Lengkap PPT</a>
  <a href="uts.html" class="nav-tab">🎯 2. Breakdown Soal UTS</a>
  <a href="kalkulator.html" class="nav-tab">🖩 3. Kalkulator &amp; Latihan</a>
</div>

<section class="sheet" id="m0">
  <div class="kode">STAT6190031 · DR. DANI SUANDI · KELAS DASAR</div>
  <h1 style="font-size:26px;font-weight:800;margin-top:4px">Buku Pegangan Konsep &amp; Contoh PPT
    <br><span style="font-size:16px;font-weight:600;color:var(--ink-soft)">Dipaparkan Dari Nol · 8 PPT Resmi BINUS (Session 1 – 7)</span></h1>
  
  <p style="margin:12px 0 16px;line-height:1.7">
    Halaman ini didesain buat lu yang ngerasa <i>"gatau apa-apa"</i> atau bingung pas dosen nerangin cepat di kelas. 
    Semua istilah dijelaskan dari nol dengan analogi logis sehari-hari, diikuti rumus resmi, jebakan ujian, 
    dan <b>contoh soal asli slide PPT dosen yang dibedah tuntas langkah per langkah</b>.
  </p>

  <div class="sec">Peta Belajar Teori (5 Bab Kunci UTS)</div>
  <div class="step"><div class="n">1</div><div class="body"><b>Bab 1 (Sesi 1 &amp; 2):</b> Skala Data (NOIR), Sampling Methods, 4 Survey Errors, dan Tabel Kontingensi.</div></div>
  <div class="step"><div class="n">2</div><div class="body"><b>Bab 2 (Sesi 2 &amp; 3):</b> Distribusi Frekuensi Berkelompok, Mean, Median, Modus, Variansi Data Kelompok, dan CV.</div></div>
  <div class="step"><div class="n">3</div><div class="body"><b>Bab 3 (Sesi 4):</b> Teori Probabilitas, Aturan Penjumlahan, Komplemen, dan Peluang Bersyarat (Tabel Silang).</div></div>
  <div class="step"><div class="n">4</div><div class="body"><b>Bab 4 (Sesi 5 &amp; 6):</b> Distribusi Diskrit: Nilai Harapan E(X), Variansi Var(X), Binomial, Poisson, &amp; Hipergeometrik.</div></div>
  <div class="step"><div class="n">5</div><div class="body"><b>Bab 5 (Sesi 7):</b> Distribusi Normal Kontinu, Standarisasi Z-Score, Membaca Tabel Z Kiri, dan Transformasi Balik X.</div></div>
</section>

<!-- BAB 1 -->
<section class="sheet" id="m1">
  <div class="head"><div class="badge">1</div><div>
    <h2>Bab 1 · Definisi Data, Skala NOIR &amp; Sampling</h2>
    <div class="sub">PPT Sesi 1 &amp; 2 · Fondasi Pengelompokan Data</div>
  </div></div>

  <div class="sec">1. Populasi vs Sampel (Huruf Yunani vs Huruf Latin)</div>
  <p>Statistika itu ilmu menarik kesimpulan tentang kelompok besar dengan cuma memeriksa kelompok kecil:</p>
  <ul class="tight">
    <li><b>Populasi ($N$):</b> Seluruh individu/objek yang ingin diteliti. Angka pengukurnya disebut <b>Parameter</b>. Simbolnya huruf Yunani: Rata-rata ($\mu$), Standar Deviasi ($\sigma$), Proporsi ($p$).</li>
    <li><b>Sampel ($n$):</b> Sebagian kecil dari populasi yang benar-benar kita kumpulkan datanya. Angka pengukurnya disebut <b>Statistik</b>. Simbolnya huruf Latin: Rata-rata ($\bar{x}$), Standar Deviasi ($s$), Proporsi ($\hat{p}$).</li>
  </ul>

  <div class="sec">2. Jembatan Keledai 4 Skala Pengukuran: N - O - I - R</div>
  <p>Jangan hafalkan definisinya, gunakan <b>uji logika bertingkat</b> ini:</p>
  
  <div class="tblwrap"><table>
    <thead><tr><th>Skala</th><th>Uji Logika</th><th>Ciri Khas</th><th>Contoh Nyata</th></tr></thead>
    <tbody>
      <tr>
        <td><b>Nominal</b></td>
        <td>Bisa diurutkan secara adil?<br><b>TIDAK BISA</b></td>
        <td>Hanya label pembeda atau nama kategori. Operasi hitung (+, −, ×, ÷) tidak bermakna sama sekali.</td>
        <td>Jenis Kelamin, Agama, Merek Laptop, Jurusan, Nomor Rekening, <b>NIM Mahasiswa</b>.</td>
      </tr>
      <tr>
        <td><b>Ordinal</b></td>
        <td>Bisa diurutkan? <b>YA</b><br>Jarak antar tingkat pasti sama? <b>TIDAK</b></td>
        <td>Punya tingkatan/ranking, tapi selisih antar ranking tidak bisa diukur persis.</td>
        <td>Tingkat Kepuasan (Puas vs Tidak Puas), Bintang Hotel (1–5), Juara Lomba (1, 2, 3), Ukuran Baju (S, M, L, XL).</td>
      </tr>
      <tr>
        <td><b>Interval</b></td>
        <td>Jarak antar angka sama? <b>YA</b><br>Angka 0 artinya tiada/kosong? <b>TIDAK</b></td>
        <td>Jarak bernilai tetap, tapi <b>tidak punya nol mutlak</b>. Angka nol hanyalah titik perjanjian skala.</td>
        <td>Suhu $0^\circ\text{C}$ (bukan berarti tidak ada suhu/panas), Tahun Kalender Masehi (tahun 0 bukan awal alam semesta), Skor IQ.</td>
      </tr>
      <tr>
        <td><b>Rasio (Ratio)</b></td>
        <td>Punya nol mutlak (0 = kosong total)?<br><b>YA PUNYA</b></td>
        <td>Bisa diperbandingkan kelipatannya (misal: "dua kali lipat", "setengahnya"). Skala paling sempurna.</td>
        <td>Gaji ($0 = tidak dapat uang sama sekali$), Berat Badan ($0\text{ kg} = tidak ada massa$), Jarak Tempuh, Waktu Tunggu, Usia.</td>
      </tr>
    </tbody>
  </table></div>

  <div class="trap-card">
    <b>⚠️ Jebakan Dosen Soal Skala:</b>
    <br>Jika di soal ujian ada <i>"Nomor Induk Mahasiswa (NIM)"</i>, <i>"Nomor Responden"</i>, atau <i>"Kode Pos"</i>, mentang-mentang isinya deretan angka, mahasiswa sering jawab Interval atau Rasio. <b>Itu SALAH!</b> Jawabannya adalah <b>NOMINAL</b> karena fungsinya murni sebagai label/nama penanda identitas, bukan kuantitas yang bisa dijumlah atau dirata-ratakan.
  </div>

  <div class="sec">3. Metode Penarikan Sampel (Sampling) &amp; 4 Survey Errors</div>
  <ul class="tight">
    <li><b>Simple Random:</b> Setiap orang punya nomor undian, diacak murni (peluang terpilih sama rata).</li>
    <li><b>Systematic:</b> Menghitung interval kelipatan $k = N/n$. Contoh: pilih setiap orang kelipatan ke-10 di antrean.</li>
    <li><b>Stratified:</b> Populasi dibagi menjadi lapisan homogen (Strata, misal: angkatan 2024, 2025, 2026), lalu dari <i>setiap</i> strata diambil beberapa orang secara acak.</li>
    <li><b>Cluster:</b> Populasi dibagi jadi gugus wilayah mini yang heterogen (Cluster, misal: RT atau gedung kantor), lalu beberapa cluster dipilih acak dan <i>seluruh orang di dalam cluster itu</i> diteliti.</li>
  </ul>
  
  <p><b>4 Sumber Kesalahan Survei (Survey Errors):</b></p>
  <ul class="tight">
    <li><b>Coverage Error:</b> Kerangka daftar populasi tidak lengkap (misal survei online mengabaikan warga yang tak punya internet).</li>
    <li><b>Nonresponse Error:</b> Orang yang terpilih menolak menjawab atau tidak mengangkat telepon.</li>
    <li><b>Sampling Error:</b> Perbedaan angka alami antara sampel acak dan populasi asli (pasti ada, disebut <i>margin of error</i>).</li>
    <li><b>Measurement Error:</b> Kesalahan akibat pertanyaan menjebak/ambigu, pewawancara salah catat, atau responden berbohong.</li>
  </ul>

  <div class="worked">
    <h4>Contoh PPT Bedah 1: Mengidentifikasi Skala Data &amp; Galat Survei</h4>
    <p><b>Soal PPT:</b> Suatu departemen HRD mengirimkan kuesioner kepada 200 karyawan melalui email untuk mengukur kepuasan kerja (skala 1–5), mencatat departemen (IT, Sales, HR), masa kerja (tahun), dan gaji bulanan. Hanya 110 karyawan yang membalas email.</p>
    <p><b>Bedah Tuntas:</b></p>
    <ul class="tight">
      <li><b>Departemen:</b> Skala <b>Nominal</b> (label kelompok kerja).</li>
      <li><b>Tingkat Kepuasan (1–5):</b> Skala <b>Ordinal</b> (ada urutan kepuasan, selisih 4 ke 5 belum tentu setara 1 ke 2).</li>
      <li><b>Masa Kerja &amp; Gaji:</b> Skala <b>Rasio</b> (punya nol mutlak; 0 tahun = belum mulai kerja, 0 rupiah = tanpa gaji).</li>
      <li><b>Galat yang Terjadi:</b> Terjadi <b>Nonresponse Error</b> karena ada 90 karyawan terpilih yang tidak membalas email, berpotensi membuat hasil survei bias ke karyawan yang rajin cek email saja.</li>
    </ul>
  </div>
</section>

<!-- BAB 2 -->
<section class="sheet" id="m2">
  <div class="head"><div class="badge">2</div><div>
    <h2>Bab 2 · Distribusi Frekuensi &amp; Ukuran Pemusatan Data</h2>
    <div class="sub">PPT Sesi 2 &amp; 3 · Mengolah Data Berkelompok (Grouped Data)</div>
  </div></div>

  <div class="sec">1. Rumus Membuat Tabel Distribusi Frekuensi</div>
  <ol class="tight">
    <li><b>Rentang (Range):</b> $R = X_{\max} - X_{\min}$</li>
    <li><b>Banyak Kelas ($k$):</b> Aturan $2^k \ge n$ atau Aturan Sturges: $k = 1 + 3,322 \log_{10}(n)$</li>
    <li><b>Lebar Kelas ($w$):</b> $w = \frac{R}{k}$ (selalu bulatkan ke atas ke angka bilangan bulat terdekat)</li>
    <li><b>Titik Tengah Kelas (Midpoint $m$):</b> $m_i = \frac{\text{Batas Bawah} + \text{Batas Atas}}{2}$</li>
  </ol>

  <div class="sec">2. Rumus Pemusatan &amp; Variansi Data Berkelompok</div>
  <div class="formula-card">
    <b>A. Rata-Rata Sampel (Mean) Data Kelompok:</b>
    $$\bar{x} = \frac{\sum (f_i \cdot m_i)}{n}$$
    <i>Keterangan: $f_i$ = frekuensi kelas ke-$i$, $m_i$ = titik tengah kelas ke-$i$, $n = \sum f_i$.</i>
  </div>

  <div class="formula-card">
    <b>B. Median Data Kelompok ($Me$):</b>
    $$Me = L + \left( \frac{\frac{n}{2} - F_{sebelum}}{f_{med}} \right) \times w$$
    <i>Keterangan:</i>
    <br>• $L$ = Tepi bawah kelas median (Batas Bawah $- 0,5$)
    <br>• $n/2$ = Letak urutan tengah
    <br>• $F_{sebelum}$ = Frekuensi kumulatif kelas <i>sebelum</i> kelas median
    <br>• $f_{med}$ = Frekuensi asli dari kelas median itu sendiri
    <br>• $w$ = Lebar/panjang kelas
  </div>

  <div class="formula-card">
    <b>C. Variansi &amp; Standar Deviasi Sampel Data Kelompok:</b>
    $$s^2 = \frac{\sum (f_i \cdot m_i^2) - \frac{(\sum f_i \cdot m_i)^2}{n}}{n - 1}$$
    $$s = \sqrt{s^2}$$
    <i>Koefisien Variasi ($CV$): $CV = \left(\frac{s}{\bar{x}}\right) \times 100\%$ (tanpa satuan, untuk membandingkan sebaran antar kelompok).</i>
  </div>

  <div class="worked">
    <h4>Contoh PPT Bedah 2: Hitung Mean &amp; Standar Deviasi Data Kelompok</h4>
    <p><b>Data Penjualan Harian 20 Hari Toko (diambil dari PPT Sesi 3):</b></p>
    <div class="tblwrap"><table>
      <thead><tr><th>Kelas Penjualan (Juta Rp)</th><th>Frekuensi ($f$)</th><th>Midpoint ($m$)</th><th>$f \cdot m$</th><th>$m^2$</th><th>$f \cdot m^2$</th></tr></thead>
      <tbody>
        <tr><td>10 – 14</td><td>3</td><td>12</td><td>36</td><td>144</td><td>432</td></tr>
        <tr><td>15 – 19</td><td>6</td><td>17</td><td>102</td><td>289</td><td>1.734</td></tr>
        <tr><td>20 – 24</td><td>8</td><td>22</td><td>176</td><td>484</td><td>3.872</td></tr>
        <tr><td>25 – 29</td><td>3</td><td>27</td><td>81</td><td>729</td><td>2.187</td></tr>
        <tr><td><b>Total ($\sum$)</b></td><td><b>$n = 20$</b></td><td>-</td><td><b>395</b></td><td>-</td><td><b>8.225</b></td></tr>
      </tbody>
    </table></div>
    <p><b>Langkah Hitung Rinci:</b></p>
    <ul class="tight">
      <li><b>Mean ($\bar{x}$):</b> $\frac{\sum f \cdot m}{n} = \frac{395}{20} = \mathbf{19,75\text{ Juta Rp}}$.</li>
      <li><b>Letak Median:</b> Posisi $n/2 = 20/2 = 10$. Frekuensi kumulatif: Kelas 1 = 3, Kelas 2 = 9, Kelas 3 = 17. Posisi 10 ada di Kelas 3 (20–24).
        <br>$L = 19,5$; $F_{sebelum} = 9$; $f_{med} = 8$; $w = 5$.
        <br>$Me = 19,5 + \left(\frac{10 - 9}{8}\right) \times 5 = 19,5 + \left(\frac{1}{8}\right) \times 5 = 19,5 + 0,625 = \mathbf{20,125\text{ Juta Rp}}$.</li>
      <li><b>Variansi Sampel ($s^2$):</b>
        <br>Pembilang $= \sum f \cdot m^2 - \frac{(\sum f \cdot m)^2}{n} = 8.225 - \frac{395^2}{20} = 8.225 - \frac{156.025}{20} = 8.225 - 7.801,25 = 423,75$.
        <br>Penyebut $= n - 1 = 20 - 1 = 19$.
        <br>$s^2 = \frac{423,75}{19} = \mathbf{22,30}$.
        <br>Standar Deviasi $s = \sqrt{22,30} = \mathbf{4,72\text{ Juta Rp}}$.</li>
      <li><b>Koefisien Variasi:</b> $CV = (4,72 / 19,75) \times 100\% = \mathbf{23,90\%}$.</li>
    </ul>
  </div>
</section>

<!-- BAB 3 -->
<section class="sheet" id="m3">
  <div class="head"><div class="badge">3</div><div>
    <h2>Bab 3 · Probabilitas Dasar &amp; Tabel Kontingensi</h2>
    <div class="sub">PPT Sesi 4 · Aturan Gabungan, Irisan, &amp; Peluang Bersyarat</div>
  </div></div>

  <div class="sec">1. Hukum-Hukum Peluang yang Wajib Dihafal</div>
  <ul class="tight">
    <li>Rentang Peluang: $0 \le P(A) \le 1$. Total seluruh semesta: $P(S) = 1$.</li>
    <li><b>Komplemen (Bukan A):</b> $P(A') = 1 - P(A)$.</li>
    <li><b>Aturan Penjumlahan (OR / Gabungan):</b>
      $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
      <i>(Jika dua kejadian Saling Lepas / Mutually Exclusive, maka $P(A \cap B) = 0$).</i>
    </li>
    <li><b>Peluang Bersyarat (Peluang A jika diketahui B sudah terjadi):</b>
      $$P(A|B) = \frac{P(A \cap B)}{P(B)}$$
      <b>Rahasia Logika:</b> Ingat bahwa huruf di belakang garis tegak ($B$) adalah <b>ruang sampel baru</b>. Maka pembagi di penyebut WAJIB total dari si $B$!
    </li>
    <li><b>Uji Dua Kejadian Independen (Saling Bebas):</b>
      Kejadian $A$ dan $B$ dikatakan independen jika peluang $A$ sama sekali tidak terpengaruh oleh adanya $B$:
      $$P(A|B) = P(A) \quad \text{atau} \quad P(A \cap B) = P(A) \times P(B)$$
    </li>
  </ul>

  <div class="worked">
    <h4>Contoh PPT Bedah 3: Tabel Kontingensi Pembelian Tiket Pesawat</h4>
    <p><b>Data Slide PPT Sesi 4:</b> Survei 100 penumpang mengenai kelas penerbangan (Bisnis / Ekonomi) dan kepuasan pelayanan (Puas / Tidak Puas):</p>
    <div class="tblwrap"><table>
      <thead><tr><th>Kelas Tiket</th><th>Puas ($S$)</th><th>Tidak Puas ($S'$)</th><th>Total Baris</th></tr></thead>
      <tbody>
        <tr><td><b>Bisnis ($B$)</b></td><td>35</td><td>5</td><td><b>40</b></td></tr>
        <tr><td><b>Ekonomi ($E$)</b></td><td>40</td><td>20</td><td><b>60</b></td></tr>
        <tr><td><b>Total Kolom</b></td><td><b>75</b></td><td><b>25</b></td><td><b>Grand Total = 100</b></td></tr>
      </tbody>
    </table></div>
    <p><b>Pertanyaan &amp; Bedah Jawaban:</b></p>
    <ul class="tight">
      <li><b>Hitung $P(B)$ (Peluang penumpang kelas Bisnis):</b> Ambil total Bisnis dibagi grand total $\to \frac{40}{100} = \mathbf{0,40}$.</li>
      <li><b>Hitung $P(S \cup B)$ (Peluang Puas ATAU Bisnis):</b>
        <br>$P(S) + P(B) - P(S \cap B) = \frac{75}{100} + \frac{40}{100} - \frac{35}{100} = \frac{80}{100} = \mathbf{0,80}$.</li>
      <li><b>Hitung $P(S|B)$ (Peluang Puas JIKA penumpang dari kelas Bisnis):</b>
        <br>Fokus hanya pada baris Bisnis (total 40 orang). Yang puas ada 35.
        <br>$P(S|B) = \frac{35}{40} = \mathbf{0,875 (87,5\%)}$.</li>
      <li><b>Hitung $P(S|E)$ (Peluang Puas JIKA penumpang dari kelas Ekonomi):</b>
        <br>Fokus pada baris Ekonomi (total 60 orang). Yang puas ada 40.
        <br>$P(S|E) = \frac{40}{60} = \mathbf{0,667 (66,7\%)}$.</li>
      <li><b>Apakah Kepuasan Independen terhadap Kelas Tiket?</b>
        <br>Karena $P(S|B) = 0,875 \ne P(S|E) = 0,667$ (atau tidak sama dengan $P(S) = 0,75$), maka <b>TIDAK INDEPENDEN</b>. Ada keterikatan nyata: penumpang kelas bisnis jauh lebih puas.</li>
    </ul>
  </div>
</section>

<!-- BAB 4 -->
<section class="sheet" id="m4">
  <div class="head"><div class="badge">4</div><div>
    <h2>Bab 4 · Distribusi Probabilitas Diskrit</h2>
    <div class="sub">PPT Sesi 5 &amp; 6 · Nilai Harapan E(X), Binomial, Poisson &amp; Hipergeometrik</div>
  </div></div>

  <div class="sec">1. Variabel Acak Diskrit Umum: Nilai Harapan &amp; Variansi</div>
  <p>Jika diberikan tabel pasangan nilai $x$ dan peluangnya $P(X = x)$:</p>
  <div class="formula-card">
    <b>Nilai Harapan / Rata-rata Jangka Panjang:</b>
    $$E(X) = \mu = \sum [x \cdot P(x)]$$
    <b>Variansi:</b>
    $$\text{Var}(X) = \sigma^2 = \sum [x^2 \cdot P(x)] - [E(X)]^2$$
    <b>Standar Deviasi:</b> $\sigma = \sqrt{\text{Var}(X)}$
  </div>

  <div class="sec">2. Tabel Pemilihan 3 Distribusi Diskrit Khusus</div>
  <div class="tblwrap"><table>
    <thead><tr><th>Nama Distribusi</th><th>Ciri Kalimat di Soal</th><th>Rumus Probabilitas $P(X = x)$</th><th>Mean ($\mu$) &amp; Variansi ($\sigma^2$)</th></tr></thead>
    <tbody>
      <tr>
        <td><b>Binomial</b></td>
        <td>• Ada $n$ percobaan tetap.<br>• Hanya 2 hasil (sukses/gagal).<br>• Peluang sukses $p$ tetap tiap percobaan.</td>
        <td>$$P(X = x) = {}_nC_x \cdot p^x \cdot (1-p)^{n-x}$$
          <i>dengan ${}_nC_x = \frac{n!}{x!(n-x)!}$</i>
        </td>
        <td>$\mu = n \cdot p$<br>$\sigma^2 = n \cdot p \cdot (1-p)$</td>
      </tr>
      <tr>
        <td><b>Poisson</b></td>
        <td>• Menghitung kejadian dalam rentang waktu/luas (misal "rata-rata kedatangan $\lambda$ per jam").<br>• Nilai $n$ sangat besar tapi $p$ kecil.</td>
        <td>$$P(X = x) = \frac{e^{-\lambda} \cdot \lambda^x}{x!}$$
          <i>dengan $e \approx 2,71828$</i>
        </td>
        <td>$\mu = \lambda$<br>$\sigma^2 = \lambda$<br>$\sigma = \sqrt{\lambda}$</td>
      </tr>
      <tr>
        <td><b>Hypergeometric</b></td>
        <td>• Sampel diambil sebanyak $n$ dari total populasi $N$.<br>• <b>TANPA PENGEMBALIAN (Without Replacement)</b>.</td>
        <td>$$P(X = x) = \frac{{}_AC_x \cdot {}_{N-A}C_{n-x}}{{}_NC_n}$$
          <i>$A$ = jumlah sukses di populasi.</i>
        </td>
        <td>$\mu = n \cdot \left(\frac{A}{N}\right)$</td>
      </tr>
    </tbody>
  </table></div>

  <div class="worked">
    <h4>Contoh PPT Bedah 4: Menghitung Peluang Binomial &amp; Poisson</h4>
    <p><b>Kasus A (Binomial):</b> Sebuah pabrik memproduksi microchip dengan tingkat cacat 5% ($p = 0,05$). Diambil 6 chip secara acak ($n = 6$). Berapa peluang menemukan tepat 1 chip yang cacat?</p>
    <ul class="tight">
      <li>${}_6C_1 = \frac{6!}{1! \cdot 5!} = 6$</li>
      <li>$P(X = 1) = 6 \times (0,05)^1 \times (0,95)^{6 - 1} = 6 \times 0,05 \times (0,95)^5 = 6 \times 0,05 \times 0,77378 = \mathbf{0,2321 (23,21\%)}$.</li>
    </ul>
    <p><b>Kasus B (Poisson):</b> Rata-rata panggilan masuk ke call center adalah 3 panggilan per menit ($\lambda = 3$). Berapa peluang dalam 1 menit ke depan masuk tepat 2 panggilan?</p>
    <ul class="tight">
      <li>$P(X = 2) = \frac{e^{-3} \cdot 3^2}{2!} = \frac{0,049787 \times 9}{2} = \frac{0,44808}{2} = \mathbf{0,2240 (22,40\%)}$.</li>
    </ul>
  </div>
</section>

<!-- BAB 5 -->
<section class="sheet" id="m5">
  <div class="head"><div class="badge">5</div><div>
    <h2>Bab 5 · Distribusi Normal Kontinu &amp; Nilai Z</h2>
    <div class="sub">PPT Sesi 7 · Standarisasi &amp; Membaca Luas Kurva Tabel Z</div>
  </div></div>

  <div class="sec">1. Rumus Inti Z-Score</div>
  <div class="formula-card">
    <b>A. Standarisasi dari Nilai Asli $X$ ke Nilai Standar $Z$:</b>
    $$Z = \frac{X - \mu}{\sigma}$$
    <b>B. Konversi Balik dari Nilai $Z$ ke Nilai Asli $X$:</b>
    $$X = \mu + Z \cdot \sigma$$
    <i>Arti Angka Z: Menunjukkan berapa jarak standar deviasi posisi nilai $X$ terhadap titik tengah rata-rata $\mu$. Z positif berarti di atas rata-rata, Z negatif di bawah rata-rata.</i>
  </div>

  <div class="sec">2. Cara Membaca Luas Area Tabel Z Standar (Cum. Left Tail)</div>
  <ul class="tight">
    <li><b>Peluang Kurang Dari $P(X < a)$ atau $P(Z < z_1)$:</b>
      <br>Langsung baca tabel Z pada perpotongan baris dan kolom yang cocok. Nilai di tabel itu sudah langsung jawabannya!
    </li>
    <li><b>Peluang Lebih Dari $P(X > a)$ atau $P(Z > z_1)$:</b>
      <br>Ingat total seluruh luas kurva adalah $1$. Maka:
      $$P(Z > z_1) = 1 - P(Z < z_1)$$
    </li>
    <li><b>Peluang Di Antara Dua Nilai $P(a < X < b)$:</b>
      <br>Hitung Z untuk batas atas ($z_2$) dan Z batas bawah ($z_1$), lalu kurangkan luas kirinya:
      $$P(z_1 < Z < z_2) = P(Z < z_2) - P(Z < z_1)$$
    </li>
  </ul>

  <div class="worked">
    <h4>Contoh PPT Bedah 5: Menghitung Peluang Nilai Mahasiswa</h4>
    <p><b>Soal PPT:</b> Nilai ujian Basic Statistics berdistribusi normal dengan rata-rata $\mu = 70$ dan standar deviasi $\sigma = 10$.</p>
    <ul class="tight">
      <li><b>1. Berapa persen mahasiswa bernilai di bawah 60?</b>
        <br>$Z = \frac{60 - 70}{10} = \frac{-10}{10} = -1,00$.
        <br>Buka Tabel Z baris $-1,0$ kolom $0,00 \to$ Angka tabel: $0,1587$.
        <br>Maka peluangnya $= \mathbf{0,1587 (15,87\%)}$.
      </li>
      <li><b>2. Berapa persen mahasiswa bernilai di atas 85?</b>
        <br>$Z = \frac{85 - 70}{10} = \frac{15}{10} = +1,50$.
        <br>Buka Tabel Z baris $+1,5$ kolom $0,00 \to$ Luas kiri tabel: $0,9332$.
        <br>Peluang di atas $85 = 1 - 0,9332 = \mathbf{0,0668 (6,68\%)}$.
      </li>
      <li><b>3. Berapa batas nilai minimum agar masuk ke 5% mahasiswa terbaik (Top 5%)?</b>
        <br>Top 5% di kanan artinya ada 95% (luas 0,9500) mahasiswa di sebelah kirinya!
        <br>Cari angka $0,9500$ di badan tabel Z $\to$ Berada di antara $Z = 1,64$ ($0,9495$) dan $Z = 1,65$ ($0,9505$), kita ambil $Z = 1,645$.
        <br>Gunakan rumus konversi balik:
        <br>$X = \mu + Z \cdot \sigma = 70 + (1,645 \times 10) = 70 + 16,45 = \mathbf{86,45}$.
        <br><i>Jadi nilai minimal untuk masuk 5% teratas adalah <b>86,45</b>.</i>
      </li>
    </ul>
  </div>
</section>
</main>
"""

MATERI_LEFT = r"""
<aside class="rail left" id="railLeft">
  <div class="panel">
    <h4>Navigasi Materi</h4>
    <ul class="road" id="road">
      <li class="now"><span class="dot"></span><a href="#m0">Pengantar<small>Peta Teori</small></a></li>
      <li><span class="dot"></span><a href="#m1">Bab 1 · NOIR<small>Skala &amp; Sampling</small></a></li>
      <li><span class="dot"></span><a href="#m2">Bab 2 · Kelompok<small>Mean, Med, Var, CV</small></a></li>
      <li><span class="dot"></span><a href="#m3">Bab 3 · Peluang<small>Hukum &amp; Kontingensi</small></a></li>
      <li><span class="dot"></span><a href="#m4">Bab 4 · Diskrit<small>E(X), Binomial, Poisson</small></a></li>
      <li><span class="dot"></span><a href="#m5">Bab 5 · Normal Z<small>Z-score &amp; Tabel</small></a></li>
    </ul>
  </div>
  <div class="panel">
    <h4>Halaman Lain</h4>
    <p style="margin:4px 0 8px;font-size:13px;line-height:1.5">Lanjut ke pembahasan soal UTS atau panduan kalkulator:</p>
    <a href="uts.html" style="display:block;margin-bottom:6px;color:var(--red);font-weight:700">🎯 2. Breakdown UTS →</a>
    <a href="kalkulator.html" style="display:block;color:var(--blue);font-weight:700">🖩 3. Kalkulator &amp; Latihan →</a>
  </div>
</aside>
"""

MATERI_RIGHT = r"""
<aside class="rail right" id="railRight">
  <div class="panel info">
    <h4>Info Modul</h4>
    <div class="kv"><span>Matkul</span><b>Basic Statistics</b></div>
    <div class="kv"><span>Kode</span><b>STAT6190031</b></div>
    <div class="kv"><span>Sifat</span><b>Open Book (1 Lbr A4)</b></div>
    <div class="kv"><span>Sumber</span><b>8 Slide PPT LMS</b></div>
    <div class="kv"><span>Dosen</span><b>Dr. Dani Suandi</b></div>
  </div>
  <div class="panel">
    <h4>Kamus Cepat Simbol</h4>
    <div class="fb-block" style="font-size:13px;font-family:inherit">
      <b>$\mu$</b> = Mean populasi<br>
      <b>$\bar{x}$</b> = Mean sampel<br>
      <b>$\sigma^2$</b> = Variansi populasi<br>
      <b>$s^2$</b> = Variansi sampel ($n-1$)<br>
      <b>$E(X)$</b> = Nilai harapan diskrit<br>
      <b>$\lambda$</b> = Rata-rata Poisson
    </div>
  </div>
  <div class="panel">
    <h4>Aturan Skala</h4>
    <div class="fb-block" style="font-size:12.5px;font-family:inherit">
      • <b>Nominal:</b> Nama/Kategori<br>
      • <b>Ordinal:</b> Ada Tingkatan<br>
      • <b>Interval:</b> Nol Semu<br>
      • <b>Rasio:</b> Nol Mutlak (Habis)
    </div>
  </div>
</aside>
"""

materi_html = shell("Buku Pegangan Materi PPT · Basic Statistics UTS",
                    MATERI_LEFT + MATERI_BODY + MATERI_RIGHT, "", current_tab="materi")
(ROOT / "materi.html").write_text(materi_html, encoding="utf-8")
print(f"materi.html generated: {len(materi_html)} bytes")
