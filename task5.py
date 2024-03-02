def ulang_program():

    # Inisialisasi variabel jumlah
    jumlah = 0

    # Inisialisasi string untuk menyimpan angka-angka
    angka_str = ""

    # Masukkan angka hingga -1 dimasukkan
    print("\nMasukkan angka (henti dengan -1):")
    while True:
        angka = int(input())
        if angka == -1:
            break
        jumlah += angka
        angka_str += str(angka) + " + "

    # Hapus tanda "+" dari belakang
    angka_str = angka_str[:-2]

    # Tampilkan hasil
    print(f"\nhasil dari {angka_str} adalah ({jumlah}) \n")

while True:
    ulang_program()

    # Tanyakan kepada pengguna apakah ingin mengulangi atau keluar
    ulangi = input("Apakah Anda ingin mengulangi? (y/n): ").lower()
    if ulangi != 'y':
        break