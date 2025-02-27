# Program Menghitung Kembalian Udin

# Input
uang_awal = 100000
harga_rokok = 20000
harga_minyak = 25000
harga_gula = 11000
diskon = 10000

# Menampilkan daftar harga barang
print("Daftar harga barang:")
print(f"Rokok: Rp{harga_rokok}")
print(f"Minyak: Rp{harga_minyak}")
print(f"Gula: Rp{harga_gula}")
print(f"Diskon: Rp{diskon}")

# Menghitung total belanja sebelum diskon
total_belanja = harga_rokok + harga_minyak + harga_gula

# Menghitung total setelah diskon
total_setelah_diskon = total_belanja - diskon

# Menghitung kembalian
kembalian = uang_awal - total_setelah_diskon

# Menampilkan hasil perhitungan
print("\nHasil Perhitungan:")
print(f"Total belanja sebelum diskon: Rp{total_belanja}")
print(f"Total setelah diskon: Rp{total_setelah_diskon}")
print(f"Uang yang diberikan: Rp{uang_awal}")
print(f"Kembalian Udin: Rp{kembalian}")

# Hasil eksekusi program:
# Total belanja sebelum diskon: Rp56000
# Total setelah diskon: Rp46000
# Uang yang diberikan: Rp100000
# Kembalian Udin: Rp54000
