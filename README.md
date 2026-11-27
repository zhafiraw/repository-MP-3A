# Analisis Variabilitas Volume Ekspor dan Impor pada Empat Pelabuhan Utama Indonesia

Program Python untuk menganalisis perkembangan volume ekspor dan impor pada Pelabuhan Belawan, Tanjung Priok, Tanjung Perak, dan Makassar selama periode pengamatan 2015–2024. Analisis dilakukan menggunakan statistik deskriptif dan metode tren linear (*linear trend*) untuk melihat pola perubahan serta memperkirakan volume perdagangan hingga tahun 2030.

## Daftar Isi
1. [Latar Belakang](#latar-belakang)
2. [Tujuan](#tujuan)
3. [Fitur Utama](#fitur-utama)
4. [Metodologi](#metodologi)
5. [Struktur Repositori](#struktur-repositori)
6. [Persyaratan Sistem](#persyaratan-sistem)
7. [Cara Menjalankan Program](#cara-menjalankan-program)
8. [Panduan Penggunaan](#panduan-penggunaan)
9. [Format Data](#format-data)
10. [Keterbatasan](#keterbatasan)
11. [Tim](#tim)

## 1. Latar Belakang

Pelabuhan memiliki peran penting dalam mendukung perdagangan internasional melalui kegiatan bongkar dan muat barang. Perubahan volume ekspor dan impor dapat menunjukkan perkembangan arus perdagangan pada suatu pelabuhan.

Program ini menggunakan data dari _Hub Network_ (HUBNET) Kementerian Perhubungan yang mencakup empat pelabuhan utama Indonesia, yaitu Belawan, Tanjung Priok, Tanjung Perak, dan Makassar. Data diolah untuk mengetahui perkembangan volume perdagangan, tingkat variasinya, serta kecenderungan perubahannya berdasarkan data historis.

## 2. Tujuan

- Mengetahui perkembangan volume ekspor dan impor pada empat pelabuhan utama.
- Membandingkan volume perdagangan antarpelabuhan.
- Mengukur variasi volume ekspor dan impor menggunakan statistik deskriptif.
- Mengidentifikasi kecenderungan perubahan volume melalui tren linear.
- Menghasilkan estimasi volume ekspor dan impor hingga tahun 2030.

## 3. Fitur Utama

| Fitur | Deskripsi |
|---|---|
| Login | Memverifikasi username dan password sebelum pengguna mengakses program. |
| Pemilihan Tahun | Memungkinkan pengguna menentukan satu tahun atau rentang tahun analisis. |
| Tabel Ekspor dan Impor | Menampilkan volume ekspor, impor, dan total pada setiap pelabuhan beserta jumlah keseluruhannya. |
| Tabel Historis per Pelabuhan | Menampilkan perkembangan volume ekspor dan impor masing-masing pelabuhan berdasarkan tahun. |
| Tabel Tren Linear | Membandingkan volume aktual dengan nilai hasil perhitungan tren linear. |
| Perbandingan Tren Linear | Menampilkan estimasi volume ekspor dan impor hingga tahun 2030 beserta selisih keduanya. |
| Ringkasan Perhitungan | Menampilkan rata-rata, standar deviasi, koefisien variasi, pertumbuhan tahunan, dan persamaan tren linear. |
| Ganti Rentang Tahun | Memungkinkan pengguna mengubah periode analisis tanpa menjalankan ulang program. |

## 4. Metodologi

Pengolahan data dilakukan secara terpisah untuk volume ekspor dan impor. Perhitungan statistik digunakan untuk menggambarkan karakteristik data, sedangkan tren linear digunakan untuk melihat kecenderungan perubahan volume berdasarkan urutan waktu.

### Penentuan Nilai dan Perhitungan

### 1. Rata-rata (*Mean*)

```text
X_bar = (Σ X_t) / n
```

Keterangan:
- X_bar = rata-rata volume ekspor atau impor.
- X_t = volume pada periode ke-t.
- n = jumlah periode pengamatan.

### 2. Pertumbuhan (*Growth*)

```text
G_t = [(X_t - X_(t-1)) / X_(t-1)] × 100%
```

Keterangan:
- G_t = persentase pertumbuhan volume.
- X_t = volume pada tahun berjalan.
- X_(t-1) = volume pada tahun sebelumnya.

### 3. Standar Deviasi (*Standard Deviation*)

```text
SD = √[Σ(X_t - X_bar)² / n]
```

Keterangan:
- SD = standar deviasi atau tingkat penyebaran data.
- X_t = volume pada periode ke-t.
- X_bar = rata-rata volume.
- n = jumlah periode pengamatan.

### 4. Koefisien Variasi (KV)

```text
KV = (SD / X_bar) × 100%
```

Keterangan:
- KV = koefisien variasi dalam persentase.
- SD = standar deviasi.
- X_bar = rata-rata volume.

### 5. Tren Linear (*Linear Trend*)

```text
Y_hat = a + bX

b = Σ[(X_i - X_bar)(Y_i - Y_bar)] / Σ(X_i - X_bar)²

a = Y_bar - bX_bar
```

Keterangan:
- Y_hat = nilai volume berdasarkan tren.
- a = konstanta garis tren.
- b = koefisien kemiringan garis tren.
- X_i = indeks urutan periode pengamatan.
- Y_i = volume aktual pada periode ke-i.
- X_bar = rata-rata indeks periode.
- Y_bar = rata-rata volume aktual.
  
Hasil persamaan tren digunakan untuk menghitung nilai kecenderungan pada periode pengamatan dan memperkirakan volume hingga tahun 2030. Nilai estimasi negatif dibatasi menjadi nol dalam program.

## 5. Struktur Repositori

```text
repository-MP-3A/
│
├── MP_3A.py
├── prokom_kel3A.csv
│
├── Dokumentasi/
│   └── LAPORAN MP 3A REVISI.docx
│
└── README.md
```

| File/Folder | Keterangan |
|---|---|
| `MP_3A.py` | Program utama untuk membaca, mengolah, dan menganalisis data. |
| `prokom_kel3A.csv` | Dataset volume ekspor dan impor. |
| `Dokumentasi/` | Berisi laporan mini project. |
| `README.md` | Dokumentasi penggunaan program. |

## 6. Persyaratan Sistem

| Komponen | Persyaratan |
|---|---|
| Bahasa Pemrograman | Python 3 |
| Library | `csv`, `statistics` |
| Format Dataset | CSV |
| Pemisah Kolom | Titik koma (`;`) |
| Encoding | UTF-8 / UTF-8-SIG |
| Koneksi Internet | Tidak diperlukan saat program dijalankan |

## 7. Cara Menjalankan Program

1. Pastikan Python 3 telah terinstal pada perangkat.
2. Unduh atau salin seluruh file proyek ke dalam satu folder.
3. Pastikan file CSV tersedia pada lokasi yang ditentukan dalam program.
4. Buka file `MP_3A.py` menggunakan editor kode atau terminal.
5. Sesuaikan lokasi dataset pada variabel `nama_file` di bagian awal kode.

Contoh penyesuaian lokasi file:

```python
nama_file = r"C:\Users\NamaPengguna\Documents\Mini Project 3A\prokom_kel3A .csv"
```

6. Jalankan program menggunakan perintah:

```bash
python MP_3A.py
```

7. Masukkan username dan password untuk mengakses program.

**Akun bawaan:**

| Keterangan | Nilai |
|---|---|
| Username | `kelompok3A` |
| Password | `1234` |

8. Masukkan rentang tahun ketika diminta oleh program setelah login berhasil
   
## 8. Panduan Penggunaan

Setelah berhasil login, program akan membaca dataset dan menampilkan seluruh kategori pelabuhan yang tersedia. Selanjutnya, pengguna diminta memasukkan tahun atau rentang tahun analisis.

Contoh input:
- `2020` untuk menganalisis satu tahun.
- `2015-2024` untuk menganalisis seluruh periode data.

Setelah rentang tahun berhasil dipilih, program menampilkan menu berikut:

| Pilihan | Menu | Fungsi |
|---|---|---|
| 1 | Tabel Ekspor dan Impor | Menampilkan volume ekspor, impor, dan total setiap pelabuhan serta jumlah keseluruhan. |
| 2 | Tabel Historis per Pelabuhan | Menampilkan data historis ekspor dan impor setiap pelabuhan beserta ringkasan perhitungannya. |
| 3 | Tabel Tren Linear | Menampilkan perbandingan volume aktual dengan nilai tren linear pada periode yang dipilih. |
| 4 | Perbandingan Tren Linear | Menampilkan estimasi volume ekspor dan impor untuk tahun setelah periode pengamatan hingga 2030. |
| 5 | Ganti Rentang Tahun | Mengubah periode analisis. |
| 0 | Keluar | Mengakhiri program. |

**Alur penggunaan:**
1. Login menggunakan akun yang tersedia.
2. Masukkan tahun atau rentang tahun analisis.
3. Pilih menu berdasarkan kebutuhan analisis.
4. Amati hasil perhitungan yang ditampilkan.
5. Pilih menu 5 jika ingin mengganti rentang tahun.
6. Pilih menu 0 untuk mengakhiri program.
   
## 9. Format Data

Dataset disimpan dalam format CSV dengan pemisah titik koma (`;`). Kolom yang digunakan oleh program adalah:

| Nama Kolom | Keterangan |
|---|---|
| `id_tabel` | Identitas tabel sumber data. |
| `kategori` | Nama pelabuhan. |
| `satuan` | Satuan pengukuran volume. |
| `tahun` | Tahun pengamatan. |
| `nilai` | Nilai volume barang. |

Program mengambil data dengan satuan `Ton`. Setiap tahun dan pelabuhan menyimpan dua nilai volume yang digunakan sebagai ekspor dan impor berdasarkan urutan kemunculannya dalam CSV.

Cakupan analisis dalam laporan meliputi:
- Pelabuhan Belawan.
- Pelabuhan Tanjung Priok.
- Pelabuhan Tanjung Perak.
- Pelabuhan Makassar.
- Periode pengamatan 2015–2024.
- Satuan volume: ton.

Sumber data: Kementerian Perhubungan Republik Indonesia melalui _Hub Network_ (HUBNET).

## 10. Keterbatasan

- Hasil analisis bergantung pada kelengkapan dan ketepatan dataset yang digunakan.
- Penentuan nilai ekspor dan impor pada kode saat ini bergantung pada urutan data dalam CSV, bukan identifikasi berdasarkan kolom jenis arus barang secara eksplisit.
- Data yang digunakan merupakan data akumulasi tahunan sehingga tidak memberikan rincian berdasarkan komoditas, perusahaan, terminal, biaya, maupun waktu tunggu.
- Tren linear hanya menggambarkan kecenderungan berdasarkan data historis dan tidak menjamin kondisi perdagangan pada periode berikutnya.
- Estimasi hingga tahun 2030 merupakan hasil ekstrapolasi model, bukan kepastian volume perdagangan aktual.
- Perhitungan tren linear memerlukan minimal dua tahun pengamatan.

## 11. Tim 

**Kelompok 3A – Teknik Industri, Universitas Andalas**

| No. | Nama | NIM |
|---|---|---|
| 1 | Zhafira Wafda | 2610931021 |
| 2 | Marsya Tri Ananda | 2610937004 |
| 3 | Iffah Astilah Rahmah Manik | 2610933010 |
| 4 | Husnul Khotimah Fadli | 2610931037 |
