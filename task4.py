def ulang_program():

  # Masukkan angka
  angka = int(input("\nMasukkan angka: "))

  # Hitung jumlah semua nilai dari 1 hingga angka
  jumlah = sum(range(1, angka + 1))

  # Tampilkan hasil
  print("\nJumlah semua nilai dari 1 hingga", angka, "adalah:", jumlah, "\n")

while True:
    ulang_program()

    # Tanyakan kepada pengguna apakah ingin mengulangi atau keluar
    ulangi = input("Apakah Anda ingin mengulangi? (y/n): ").lower()
    if ulangi != 'y':
        break