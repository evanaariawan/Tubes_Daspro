import config

# Berisi perintah yang dapat diakses oleh Roro Jonggrang
def hancurkan_candi():
    no_id = input("Masukkan ID candi: ")
    # ditemukan_candi sebagai validator looping
    ditemukan_candi = False
    # idx sebagai index untuk mengakses matriks candi
    idx = 0 

    # Mencari candi dari  yang diinput
    while idx < config.last_idx_candi - 1 and not ditemukan_candi:
        idx += 1
        if str(config.candi[idx][0]) == no_id and no_id != '':
            ditemukan_candi = True
    # Jika candi ada
    if ditemukan_candi:
        # Meminta konfirmasi 
        answer = input(f"Apakah anda yakin ingin menghancurkan candi ID: {no_id} (Y/N)? ").upper()
        # Jika iya, mengubah data matriks candi di idx menjadi seperti saat inisiasi awal
        if answer == "Y":
            config.candi[idx] = ['' for _ in range(5)]
            # Menambahkan jumlah candi yang perlu dibangun
            config.sisa_candi += 1
            print("\nCandi telah berhasil dihancurkan.")
    # Jika tak ada candi, tampilkan pesan
    else:
        print("Tidak ada candi dengan ID tersebut.")


def manggil_ayam():
    print("Kukuruyuk.. Kukuruyuk..")
    print(f"\nJumlah candi: {100 - config.sisa_candi}")
    # Jika masih ada sisa candi yang harus dibangun, Roro Jonggrang menang!
    if config.sisa_candi > 0:
        print("\nSelamat Roro Jonggrang memenangkan permainan!")
        print("\n*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
    # Jika tidak ada, Bondowoso menang!
    else:
        print("\nYah, Bandung Bondowoso memenangkan permainan!")
    # Kemudian keluar program
    exit()