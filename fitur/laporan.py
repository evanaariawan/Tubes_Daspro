import config

def jin():
    # Inisaisi varibel yang akan ditampilkan
    terajin = "-"
    termalas = "-"
    count_terbanyak = 0
    count_tersedikit = config.last_idx_candi # tersedikit diser dengan id candi terbesar

    # Melakukan looping pada matriks users untuk semua jin
    for i in range(3, config.count_users):
        # Setiap loop data pembangun dan jumlah candi yang dibangun diinisiasi
        pembangun = config.users[i][0]
        count = 0
        # Melakukan looping pada matriks candi dan melakukan penambahan variabel count jika pembuat candi == pembangun
        for j in range(config.last_idx_candi):
            if config.candi[j][1] == pembangun:
                count += 1
        # Melakukan perbandingan jika sudah ada candi yang dibangun
        # Semua kondisi periksa terbanyak atau tersedikit
        if config.sisa_candi < 100:
            # Membandingkan count terbanyak dengan count candi jin di atas
            # Mengubah terajin menjadi pembangun jika candi jin lebih banyak
            if count > count_terbanyak:
                count_terbanyak = count
                terajin = pembangun
            # Jika jumlahnya sama dengan count terbanyak, teranjin dengan leksikografis terbesar
            if count == count_terbanyak:
                if pembangun < terajin:
                    terajin = pembangun
            #Mengubah termalas menjadi pembangun jika candi jin lebih sedikit dari count tersedikit
            if count < count_tersedikit:
                if (count > 0 or config.users[i][2] == "jin_pembangun"):
                    count_tersedikit = count
                    termalas = pembangun
             # Jika jumlahnya sama dengan count tersedikit, termalas dipilih dengan leksikografis terkecil
            if count == count_tersedikit:
                if count > 0 or config.users[i][2] == "jin_pembangun":
                    if pembangun > termalas:
                        termalas = pembangun

    # Menampilkan seluruh informasi terkait
    print(f"> Total Jin: {config.count_jin_pengumpul + config.count_jin_pembangun}")
    print(f"> Total Jin Pengumpul: {config.count_jin_pengumpul}")
    print(f"> Total Jin Pembangun: {config.count_jin_pembangun}")
    print(f"> Jin Terajin: {terajin}")
    print(f"> Jin Termalas: {termalas}")  
    print(f"> Jumlah Pasir: {config.bahan[1][2]} unit")
    print(f"> Jumlah Batu: {config.bahan[2][2]} unit")
    print(f"> Jumlah Air: {config.bahan[3][2]} unit")



def candi():
    # Inisasi variabel yang akan akan ditampilkan
    total_pasir = 0
    total_batu = 0
    total_air = 0
    termahal = 0
    id_termahal = '-'
    termurah = 487_500 # termurah diset dengan harga candi termahal yang mungkin
    id_termurah = '-'

    # Melakukan looping pada matriks candi
    for i in range(1, config.last_idx_candi):
        if config.candi[i][0] != '':
            # Menambahkkan jumlah bahan yang digunakan pada tiap candi pada masing - masing variabel yang berkaitan
            total_pasir += config.candi[i][2]
            total_batu += config.candi[i][3]
            total_air += config.candi[i][4]
            # Menghitung harga tiap candi
            harga = (10000 * config.candi[i][2]) + (15000 * config.candi[i][3]) + (7500 * config.candi[i][4])
            # Menentuka id dan harga termahal
            if harga > termahal:
                termahal = harga
                id_termahal = i
            # menentuka id dan harga termurah
            if harga < termurah:
                termurah = harga
                id_termurah = i
                
    # Jika candi masih 0 maka termurah = 0
    termurah = 0 if id_termurah == '-' else termurah

    # Menampilkan seluruh informasi terkait candi
    print(f"> Total Candi: {100 - config.sisa_candi}")
    print(f"> Total Pasir yang digunakan: {total_pasir}")
    print(f"> Total Batu yang digunakan: {total_batu}")
    print(f"> Total Air yang digunakan: {total_air}")
    print(f"> ID Candi Termahal: {id_termahal} (Rp{termahal})")
    print(f"> ID Candi Termurah: {id_termurah} (Rp{termurah})")