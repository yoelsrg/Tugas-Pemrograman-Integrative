def ulang_program():

    # Masukkan angka
    angka = float(input("\nMasukkan angka: "))

    # Tentukan apakah angka kecil, sedang, atau besar
    if angka < 100:
        hasil = "Kecil"
    elif angka > 200:
        hasil = "Besar"
    else:
        hasil = "Sedang"

    # Tampilkan hasil
    print("Angka yang anda masukkan adalah angka", (hasil), "\n")

while True:
    ulang_program()

    # Tanyakan kepada pengguna apakah ingin mengulangi atau keluar
    ulangi = input("Apakah Anda ingin mengulangi? (y/n): ").lower()
    if ulangi != 'y':
        break