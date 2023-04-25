import config

def ubah_jin():
    # found_name sebagai validator
    found_name = False
    # idx sebagai index loop dimulai dari 2 karena idx langsung ditambah 1 dan jin ada dari index 3
    idx = 2
    # Meminta nama jin yang ingin diubah dan periksa apakah jin tersebut ada
    username = input("Masukkan username jin: ")
    while (idx < config.count_users - 2 ) and not found_name:
        idx += 1
        if config.users[idx][0] == username:
            found_name = True
    # Jika ada, proses dilanjutkan
    if found_name:
        # Menentukan teks yang akan ditampilkan sesuai dengan role jin yang ingin diubah
        tipe_jin = "Pengumpul" if config.users[idx][2] == "jin_pengumpul" else "Pembangun"
        ubah_ke = "Pembangun" if tipe_jin == "Pengumpul" else "Pengumpul"
        # Meminta konfirmasi
        answer = input(f"Jin ini bertipe “{tipe_jin}”. Yakin ingin mengubah ke tipe “{ubah_ke}” (Y/N)? ").upper()
        if answer == "Y":
            # Update banyaknya jumlah jin pada variabel count sesuai role jin yang diubah
            if config.users[idx][2] == "jin_pengumpul":
                config.count_jin_pengumpul -= 1
                config.count_jin_pembangun += 1
            else:
                config.count_jin_pembangun -= 1
                config.count_jin_pengumpul += 1

            # Mengubah role jin tersebut
            config.users[idx][2] = "jin_pembangun" if ubah_ke == "Pembangun" else "jin_pengumpul"
            print("\nJin telah berhasil diubah.")

    # Tampilkan pesan, jika jin tidak ada
    else:
        print("\nTidak ada jin dengan username tersebut.")