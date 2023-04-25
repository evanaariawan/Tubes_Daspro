import config

def help():
    # Menampilkan perintah yang dapat diakses sesuai dengan role saat ini
    role = config.logged_in_user[1]
    print("=========== HELP ===========")
    if role == "bandung_bondowoso":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang.")
        print("2. summonjin")
        print("   Untuk memanggil jin.")
        print("3. hapusjin")
        print("   Untuk menghapus jin")
        print("4. ubahjin")
        print("   Untuk mengubah tipe jin.")
        print("5. batchkumpul")
        print("   Untuk mengerahkan jin pengumpul mengumpulkan bahan bangunan.")
        print("6. batchbangun")
        print("   Untuk mengerahkan jin pembangun untuk membangun candi.")
        print("7. laporanjin")
        print("   Untuk mengetahui kinerja dari para jin. ")
        print("8. laporancandi")
        print("   Untuk mengetahui progress pembangunan candi.")
        print("9. save")
        print("   Untuk menyimpan progres data selama ini..")
    
    elif role == "roro_jonggrang":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang.")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi yang telah dibangun.")
        print("3. ayamberkokok")
        print("   Untuk menyelesaikan permainan.")
        print("4. save")
        print("   Untuk menyimpan progres data selama ini.")
    
    elif role == "jin_pengumpul":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang.")
        print("2. kumpul")
        print("   Untuk mengumpulkan bahan-bahan yang diperlukan.")
        print("3. save")
        print("   Untuk menyimpan progres data selama ini.")
    
    elif role == "jin_pembangun":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang.")
        print("2. bangun")
        print("   Untuk membangun candi dengan bahan-bahan yang ada.")
        print("3. save")
        print("   Untuk menyimpan progres data selama ini.")

    else:
        print("1. login")
        print("   Untuk masuk menggunakan akun.")
        print("3. save")
        print("   Untuk menyimpan progres data selama ini.")
        print("2. exit")
        print("   Untuk  keluar dari program dan kembali ke terminal.")
