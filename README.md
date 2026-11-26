# MINI PROJECT KELOMPOK 3A
## ANALISIS DATA EKSPOR DAN IMPOR BERDASARKAN PELABUHAN

### 1. Deskripsi Program
Pernahkah kamu ingin mengetahui pelabuhan mana yang memiliki volume ekspor dan impor terbesar? Atau bagaimana perkembangan aktivitas ekspor dan impor dari tahun ke tahun?

Program ini dibuat untuk membantu menjawab pertanyaan tersebut.

Program Analisis Data Ekspor dan Impor merupakan aplikasi berbasis Python yang mengolah data perdagangan berdasarkan pelabuhan. Melalui program ini, pengguna dapat melihat perbandingan volume ekspor dan impor, mengetahui perkembangan setiap tahunnya, serta memperkirakan kecenderungan perdagangan hingga tahun 2030 menggunakan metode tren linear.

Dengan demikian, data yang awalnya berupa kumpulan angka dapat diolah menjadi informasi yang lebih mudah dipahami.

### 2. Input User
Untuk menggunakan program, pengguna hanya perlu memasukkan dua jenis input:

**A. Tahun atau Rentang Tahun**

Pengguna menentukan periode data yang ingin dianalisis, mulai dari tahun 2015 sampai 2025.

Contoh:
- `2020` untuk menganalisis satu tahun.
- `2015-2024` untuk menganalisis rentang tahun.

**B. Pilihan Menu**

Setelah memasukkan tahun, pengguna dapat memilih salah satu fitur berikut:

| Menu | Fungsi |
|---|---|
| 1 | Melihat tabel volume ekspor dan impor setiap pelabuhan. |
| 2 | Melihat perkembangan historis setiap pelabuhan. |
| 3 | Melihat perbandingan data aktual dengan hasil tren linear. |
| 4 | Melihat perbandingan perkiraan tren ekspor dan impor hingga 2030. |
| 5 | Mengganti rentang tahun analisis. |
| 0 | Mengakhiri program. |

### 3. Workflow Program

Program bekerja melalui tahapan berikut:

1. **Membaca Data:** Program mengambil data ekspor dan impor dari file CSV.
2. **Mengelompokkan Data:** Data disusun berdasarkan tahun dan kategori pelabuhan.
3. **Memilih Periode:** Pengguna memasukkan tahun atau rentang tahun yang ingin dianalisis.
4. **Memilih Analisis:** Pengguna menentukan jenis tabel atau analisis melalui menu.
5. **Mengolah Data:** Program menghitung total ekspor dan impor, rata-rata, standar deviasi, koefisien variasi, pertumbuhan tahunan, dan tren linear sesuai fitur yang dipilih.
6. **Menampilkan Hasil:** Hasil perhitungan disajikan dalam bentuk tabel agar mudah dibaca dan dibandingkan.
7. **Selesai:** Pengguna dapat melakukan analisis kembali, mengganti periode, atau keluar dari program.

### 4. Hasil yang Diperoleh
Melalui program ini, pengguna dapat memperoleh informasi mengenai:
- Total volume ekspor dan impor berdasarkan pelabuhan.
- Perkembangan ekspor dan impor dari tahun ke tahun.
- Tingkat variasi dan penyebaran data.
- Persentase pertumbuhan tahunan.
- Kecenderungan perkembangan ekspor dan impor melalui tren linear.
- Perbandingan perkiraan ekspor dan impor hingga tahun 2030.

### 5. Cara Menjalankan Program
1. Pastikan Python sudah terinstal di komputer.
2. Simpan file `MP_3A.py` dan file CSV dalam folder proyek.
3. Sesuaikan lokasi file CSV pada kode program.
4. Jalankan program melalui terminal dengan perintah:

```bash
python MP_3A.py
```

5. Masukkan tahun atau rentang tahun, kemudian pilih menu analisis yang tersedia.

---

**Kelompok 3A**

*Mengubah data menjadi informasi melalui pemrograman dan analisis statistik.*
