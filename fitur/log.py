import config


def login():
    # Memeriksa apakah sudah login
    if not config.logged_in:
        # user_index sebagai index saat looping dan digunakan untuk validasi pwd
        user_index = 0
        # found_name sebagai validator
        found_name = False

        username = input("Username: ")
        pwd = input("Password: ")

        # Mencari username pada data matriks user dimulai dari index 1 karena index 0 adalah header
        while (user_index < config.count_users - 1) and not found_name: 
            user_index += 1
            if username == config.users[user_index][0]:
                found_name = True
        
        # Jika ada, memeriksa apakah passwordnya sesuai
        if found_name: 
            if pwd == config.users[user_index][1]:
                # Jika password benar, simpan informasi username dan role. Kemudian tandai sudah login
                config.logged_in_user = [username, config.users[user_index][2]]
                config.logged_in = True 
                print(f"\nSelamat datang, {config.logged_in_user[0]}!")
                print(
                    "Masukkan command “help” untuk daftar command yang dapat kamu panggil."
                )
            # Tampilkan pesan salah
            else:
                print("\nPassword salah!")
        # Tampilkan pesan username tak terdaftar
        else:
            print("\nUsername tidak terdaftar!")

    # Tampilkan pesan bahwa sudah login dan logout terlebih dahulu
    else:
        print("Login gagal!")
        print(
            f"Anda telah login dengan username {config.logged_in_user[0]}, silahkan lakukan “logout” sebelum melakukan login kembali."
        )


def logout():
    # Periksa apakah sudah login
    if config.logged_in:
        print("Anda telah keluar.")
        config.logged_in = False
        config.logged_in_user = ["", ""]
    # Jika belum, tampilkan pesan untuk login terlebih dahulu
    else:
        print("Logout gagal!")
        print(
            "Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout"
        )


