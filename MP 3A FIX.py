
import csv
import statistics

nama_file = r"C:\Users\LENOVO\Downloads\prokom_kel3A.csv"
data_tahunan = {}
kategori = []

print("=" * 15, "MINI PROJECT", "=" * 15)
print("=" * 15, "KELOMPOK 3A", "=" * 16)

def baca_data():
    with open(nama_file, "r", encoding="utf-8-sig") as file:
        data = csv.DictReader(file, delimiter=";")

        for row in data:
            tahun = int(row["tahun"])
            nama = row["kategori"].strip()

            if nama not in kategori:
                kategori.append(nama)
            if row["satuan"].strip() == "Ton":
                if tahun not in data_tahunan:
                    data_tahunan[tahun] = {}
                if nama not in data_tahunan[tahun]:
                    data_tahunan[tahun][nama] = []
                data_tahunan[tahun][nama].append(float(row["nilai"]))

def pilih_tahun():
    bagian = input("\nMasukkan tahun atau rentang tahun (2015-2024): ").split("-")
    awal = int(bagian[0])
    akhir = int(bagian[-1])

    if awal < 2015 or akhir > 2024 or awal > akhir:
        print("Rentang tahun tidak valid.")
        return []
    tahun = []

    for t in sorted(data_tahunan):
        if awal <= t <= akhir:
            tahun.append(t)
    if tahun == []:
        print("Data tahun tidak tersedia.")
    return tahun

def ambil_volume(tahun, nama):
    volume = data_tahunan[tahun].get(nama, [])
    ekspor = volume[0] if len(volume) > 0 else 0
    impor = volume[1] if len(volume) > 1 else 0
    return ekspor, impor

def hitung_total(tahun):
    ekspor = 0
    impor = 0

    for nama in kategori:
        e, i = ambil_volume(tahun, nama)
        ekspor += e
        impor += i
    return ekspor, impor

def trend_linear(data):
    n = len(data)
    rata_x = (n + 1) / 2
    rata_y = statistics.mean(data)
    pembilang = 0
    penyebut = 0

    for j in range(n):
        x = j + 1
        pembilang += (x - rata_x) * (data[j] - rata_y)
        penyebut += (x - rata_x) ** 2
    b = pembilang / penyebut
    a = rata_y - b * rata_x
    return a, b

def ringkasan(tahun, ekspor, impor):
    rata_e = statistics.mean(ekspor)
    rata_i = statistics.mean(impor)
    sd_e = statistics.pstdev(ekspor)
    sd_i = statistics.pstdev(impor)
    kv_e = sd_e / rata_e * 100 if rata_e != 0 else 0
    kv_i = sd_i / rata_i * 100 if rata_i != 0 else 0
    
    print()
    print("\nRINGKASAN HASIL PERHITUNGAN".center(75))
    print("=" * 75)
    print(f"{'KETERANGAN':<28} {'EKSPOR':>20} {'IMPOR':>20}")
    print("-" * 75)
    print(f"{'Rata-rata volume':<28} {rata_e:>20,.2f} {rata_i:>20,.2f}")
    print(f"{'Standar deviasi':<28} {sd_e:>20,.2f} {sd_i:>20,.2f}")
    print(f"{'Koefisien variasi (%)':<28} {kv_e:>20,.2f} {kv_i:>20,.2f}")
    print("\nPERTUMBUHAN TAHUNAN")
    print("-" * 75)
    print(f"{'TAHUN':<15} {'EKSPOR (%)':>25} {'IMPOR (%)':>25}")

    for j in range(len(tahun)):
        if j == 0:
            print(f"{tahun[j]:<15} {'-':>25} {'-':>25}")
        else:
            ge = (ekspor[j] - ekspor[j-1]) / ekspor[j-1] * 100 if ekspor[j-1] != 0 else 0
            gi = (impor[j] - impor[j-1]) / impor[j-1] * 100 if impor[j-1] != 0 else 0
            print(f"{tahun[j]:<15} {ge:>25.2f} {gi:>25.2f}")

    if len(tahun) >= 2:
        a_e, b_e = trend_linear(ekspor)
        a_i, b_i = trend_linear(impor)
        print("\nPERSAMAAN TREND LINEAR")
        print("Ekspor : Y =", round(a_e, 2), "+", round(b_e, 2), "X")
        print("Impor  : Y =", round(a_i, 2), "+", round(b_i, 2), "X")
    print("=" * 75)

def tabel_ekspor_impor(tahun):
    ekspor = []
    impor = []

    print("\n=== TABEL EKSPOR DAN IMPOR ===")

    for t in tahun:
        print("\nTAHUN:", t)
        print("-" * 75)
        print(f"{'PELABUHAN':<22} {'EKSPOR':>18} {'IMPOR':>18} {'TOTAL':>18}")

        e_total = 0
        i_total = 0

        for nama in kategori:
            e, i = ambil_volume(t, nama)
            e_total += e
            i_total += i
            print(f"{nama:<22} {e:>18,.0f} {i:>18,.0f} {e+i:>18,.0f}")
        print("-" * 75)
        print(f"{'TOTAL':<22} {e_total:>18,.0f} {i_total:>18,.0f} {e_total+i_total:>18,.0f}")
        ekspor.append(e_total)
        impor.append(i_total)
    ringkasan(tahun, ekspor, impor)

def tabel_historis(tahun):
    print("\n=== TABEL HISTORIS PER PELABUHAN ===")

    for nama in kategori:
        ekspor = []
        impor = []
        print("\nPELABUHAN:", nama)
        print("-" * 85)
        print(f"{'TAHUN':<22} {'EKSPOR':>18} {'IMPOR':>18} {'TOTAL':>18}")

        for t in tahun:
            e, i = ambil_volume(t, nama)
            ekspor.append(e)
            impor.append(i)
            print(f"{t:<22} {e:>18,.0f} {i:>18,.0f} {e+i:>18,.0f}")
        ringkasan(tahun, ekspor, impor)

def regresi(tahun, pilihan):
    if len(tahun) < 2:
        print("Minimal diperlukan dua tahun data.")
        return

    ekspor = []
    impor = []

    for t in tahun:
        e, i = hitung_total(t)
        ekspor.append(e)
        impor.append(i)
    a_e, b_e = trend_linear(ekspor)
    a_i, b_i = trend_linear(impor)

    if pilihan == "3":
        print("\n=== TABEL TREND LINEAR ===")
        print("-" * 95)
        print(f"{'TAHUN':<12} {'EKSPOR AKTUAL':>20} {'TREND EKSPOR':>20} {'IMPOR AKTUAL':>20} {'TREND IMPOR':>20}")
        for j in range(len(tahun)):
            x = j + 1
            e = a_e + b_e * x
            i = a_i + b_i * x
            print(f"{tahun[j]:<12} {ekspor[j]:>20,.2f} {e:>20,.2f} {impor[j]:>20,.2f} {i:>20,.2f}")

    else:
        print("\n=== PERBANDINGAN TREND LINEAR ===")
        print("-" * 85)
        print(f"{'TAHUN':<15} {'EKSPOR':>20} {'IMPOR':>20} {'SELISIH':>20}")

        for t in range(tahun[-1] + 1, 2031):
            x = len(tahun) + t - tahun[-1]
            e = max(0, a_e + b_e * x)
            i = max(0, a_i + b_i * x)
            print(f"{t:<15} {e:>20,.2f} {i:>20,.2f} {e-i:>20,.2f}")
    ringkasan(tahun, ekspor, impor)

def menu():
    tahun = pilih_tahun()

    if tahun == []:
        return
    while True:
        print("\n========== MENU OUTPUT ==========")
        print("1. Tabel Ekspor dan Impor")
        print("2. Tabel Historis per Pelabuhan")
        print("3. Tabel Trend Linear")
        print("4. Perbandingan Trend Linear")
        print("5. Ganti Rentang Tahun")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tabel_ekspor_impor(tahun)
        elif pilihan == "2":
            tabel_historis(tahun)
        elif pilihan == "3" or pilihan == "4":
            regresi(tahun, pilihan)
        elif pilihan == "5":
            tahun_baru = pilih_tahun()
            if tahun_baru != []:
                tahun = tahun_baru
        elif pilihan == "0":
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak tersedia.")

try:
    baca_data()
    print("\n=== SELURUH KATEGORI DATA ===")
    for j in range(len(kategori)):
        print(j + 1, ".", kategori[j])
    menu()

except FileNotFoundError:
    print("File CSV tidak ditemukan.")
except (ValueError, KeyError, ZeroDivisionError):
    print("Data CSV tidak valid atau kolom tidak sesuai.")