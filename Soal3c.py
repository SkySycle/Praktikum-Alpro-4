try:
    bulan = int(input("Masukkan bulan (1-12): "))
    if bulan < 1 or bulan > 12:
        print("Bulan tidak valid! Harap masukkan angka antara 1-12.")
    else:
        hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        print(f"Jumlah hari: {hari_per_bulan[bulan - 1]}")
except ValueError:
    print("Input tidak valid! Harap masukkan angka antara 1-12.")
