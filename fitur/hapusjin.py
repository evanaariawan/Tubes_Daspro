import config

def ilangin_jin():
    # found_name sebagai validator
    found_name = False
    # idx sebagai index untuk looping data matriks users
    idx = 2
    username = input("Masukkan username jin: ")
    while (idx < config.count_users - 1) and not found_name:
        idx += 1
        if config.users[idx][0] == username:
            found_name = True

    # Jika ada, proses dilanjutkan
    if found_name:
        # Konfirmasi
        answer = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ").upper()
        if answer == "Y":
            # Mengurangi jumlah jin yang bersangkutan pada variabel untuk count jin
            if config.users[idx][2] == "jin_pengumpul":
                config.count_jin_pengumpul -= 1
            else:
                config.count_jin_pembangun -= 1
            # data pada matriks index ke idx diubah menjadi list saat insisasi awal   
            config.users[idx] = ['', '', '']
            # Menghapus candi yang dibangun oleh jin yang dihapus
            for i in range(1, config.last_idx_candi):
                if config.candi[i][1] == username:
                    config.candi[i] = ['' for _ in range(5)]
                    config.sisa_candi += 1

            print("\nJin telah berhasil dihapus dari alam gaib.")
        
            # Menata ulang data matriks dengan menggeser semua data ke kiri
            for i in range(idx, config.count_users):
                config.users[i] = config.users[i+1]
        
            config.count_users -= 1
    # Tampilkan pesan jika        
    else:
        print("\nTidak ada jin dengan username tersebut.")
    

   
    