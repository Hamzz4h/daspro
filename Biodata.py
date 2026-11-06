biodata = {}

jalan = True

while jalan:
    print("MENU")
    print("1. Input biodata")
    print("2. Tampilkan biodata")
    print("3. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        print("Input Biodata")
        nama = input("Nama Lengkap: ")
        nim = input("NIM: ")
        kelas = input("Kelas: ")
        prodi = input("Program Studi: ")
        umur = input("Umur: ")
        telp = input("No Telepon: ")

        biodata = {
            "Nama Lengkap": nama,
            "NIM": nim,
            "Kelas": kelas,
            "Program Studi": prodi,
            "Umur": umur,
            "No Telepon": telp
        }
        print("Biodata berhasil disimpan!")

    elif pilihan == "2":
        print("Biodata")
        if len(biodata) == 0:
            print("Belum ada biodata. Silakan input biodata dulu.")
        else:
            print("Nama Lengkap:", biodata["Nama Lengkap"])
            print("NIM:", biodata["NIM"])
            print("Kelas:", biodata["Kelas"])
            print("Program Studi:", biodata["Program Studi"])
            print("Umur:", biodata["Umur"])
            print("No Telepon:", biodata["No Telepon"])

    elif pilihan == "3":
        print("Terima kasih!")
        jalan = False

    else:
        print("Pilihan tidak valid, coba lagi.")