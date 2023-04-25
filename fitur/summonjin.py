import config
import time

def manggil_jin():
    # Periksa jika jin yang ada kurang dari 100
    if (config.count_jin_pengumpul + config.count_jin_pembangun) < 100:
        print("Jenis jin yang dapat dipanggil:")
        print("  (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("  (2) Pembangun - Bertugas membangun candi")

        # Inisiasi list kosong sebagai data jin yang dipanggil
        summoned_jin = ['' for _ in range(3)] 
        jenis_jin = ["jin_pengumpul", "jin_pembangun"]
        keterangan_jin = ["Pengumpul", "Pembangun"]
        # Proses memilih jenis jin yang akan dipanggil
        # milih_jin sebagai validator
        milih_jin = False
        while not milih_jin:
            nomor = input("\nMasukkan nomor jenis jin yang ingin dipanggil: ")
            if nomor == '1' or nomor == '2':
                milih_jin = True
            else:
                print(f'\nTidak ada jenis jin bernomor “{nomor}”!')
        print(f'\nMemilih jin "{keterangan_jin[int(nomor) - 1]}"')

        # Meminta dan memeriksa username yang digunakan harus unik
        found_name = False
        while not found_name:
            username = input("\nMasukkan username jin: ")
            idx = 1
            same_username = False
            while idx < config.count_users and not same_username:
                if username == config.users[idx][0]:
                    print(f'\nUsername "{username}" sudah diambil.')
                    same_username = True
                idx += 1
            if not same_username:
                found_name = True

        # Meminta dan memeriksa password dengan syarat yang ada
        right_pwd = False
        while not right_pwd:
            pwd = input("Masukkan password jin: ")
            if 5 <= len(pwd) <= 25:
                right_pwd = True
            else:
                print("\nPassword panjangnya harus 5-25 karakter!")

        # Semua syarat terpenuhi, simpan informasi yang diterima ke dalam summoned_jin
        summoned_jin[0] = username
        summoned_jin[1] = pwd
        summoned_jin[2] = jenis_jin[int(nomor) - 1]

        # Update data matriks user
        config.users[config.count_users] = summoned_jin
        config.count_users += 1

        # Menambahkan banyaknya jin yang bersangkutan pada count variabel
        if  summoned_jin[2] == "jin_pengumpul":
            config.count_jin_pengumpul += 1
        else:
            config.count_jin_pembangun += 1

        time.sleep(1)
        print("\nMengumpulkan sesajen...")
        time.sleep(1)
        print("Menyerahkan sesajen...")
        time.sleep(1)
        print("Membacakan mantra...", end="\n\n")
        time.sleep(1)
        print(f"Jin {username} berhasil dipanggil!")

    # Jika sudah 100, tampilkan pesan
    else:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu.")

    
            



