def ulang_program():

  # Masukkan bilangan bulat
  bilangan_bulat = int(input("\nMasukkan bilangan bulat: "))

  # Pembagian dengan 3
  hasil_pembagian = bilangan_bulat / 3

  # Hasil pembagian dengan tiga tempat desimal (dibulatkan)
  print("Hasil pembagian dengan 3:", format(hasil_pembagian, '.3f'))

while True:
    ulang_program()

    # Tanyakan kepada pengguna apakah ingin mengulangi atau keluar
    ulangi = input("\nApakah Anda ingin mengulangi? (y/n): ").lower()
    if ulangi != 'y':
        break