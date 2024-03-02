def ulang_program():
  # Masukkan gaji bulanan
  gaji = float(input("\nMasukkan gaji : "))

  # Gaji bulanan dibagi 12
  gaji_bulanan = gaji / 12

  # Hasil gaji bulanan dengan pembulatan 0 desimal
  print("Gaji bulanan :", round(gaji_bulanan))

while True:
    ulang_program()

    # Tanyakan kepada pengguna apakah ingin mengulangi atau keluar
    ulangi = input("\nApakah Anda ingin mengulangi? (y/n): ").lower()
    if ulangi != 'y':
        break