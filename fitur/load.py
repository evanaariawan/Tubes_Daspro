import config

# Fungsi load menerima masukan folder dengan melakukan parser delimeter ;
# idx sebagai index untuk setiap baris pada file dan untuk alamat index saat menambahkan ke matriks terkait
# word adalah elemen yang akan ditambahkan untuk setiap kata yang dipisahkan oleh ; pada tiap baris
# i adalah index pada list di dalam matriks
def load(folder):
    idx = 0
    # Load data user ke dalam matriks users
    with open(f"save/{folder}/user.csv") as f:
        for line in f:
            word = "" 
            i = 0
            for ch in line:
                if ch == ";" or ch == "\n":
                    config.users[idx][i] = word
                    word = ""
                    i += 1
                else:
                    word += ch
            idx += 1

        # Banyaknya user yaitu jumlah baris pada fike ini
        config.count_users = idx
        # Melakukan update count jin setelah load file
        for i in range(3, config.count_users):
            if config.users[i][2] == "jin_pengumpul":
                config.count_jin_pengumpul += 1
            else:
                config.count_jin_pembangun += 1

    idx = 0
    # Load data matriks bahan bangunan
    with open(f"save/{folder}/bahan_bangunan.csv") as f:
        for line in f:
            word = ""
            i = 0
            for ch in line:
                if ch == ";" or ch == "\n":
                    config.bahan[idx][i] = word
                    word = ""
                    i += 1
                else:
                    word += ch
            idx += 1

        # Set nilai pada bagian jumlah menjadi int agar mudah dalam melakukan operasi
        if config.bahan[1][2] == config.bahan[2][2] ==  config.bahan[3][2] == '':
            config.bahan[1][2] = config.bahan[2][2] =  config.bahan[3][2] = 0
        else:
            config.bahan[1][2] = int(config.bahan[1][2])
            config.bahan[2][2] = int(config.bahan[2][2])
            config.bahan[3][2] = int(config.bahan[3][2])

        # Set data yang konstan yaitu nama bahan dan dekripsi
        config.bahan[1][0], config.bahan[1][1] = 'pasir', 'pasir waktu'
        config.bahan[2][0], config.bahan[2][1] = 'batu', 'batu marmer'
        config.bahan[3][0], config.bahan[3][1] = 'air', 'air bersih'

    idx = 0
    # Load data matriks candi
    with open(f"save/{folder}/candi.csv") as f:
        for line in f:
            word = ""
            i = 0
            current_id = 0
            for ch in line:
                
                if ch == ";" or ch == "\n":
                    # Menyimpan data pada index sesuai dengan id candi tersebut
                    if idx > 0 and i == 0:
                        current_id = int(word)
                    # Menyimpan data jumlah bahan yang digunakan
                    if idx > 0 and i > 1 and word != '':
                        config.candi[current_id][i] = int(word) 
                    else:
                        config.candi[current_id][i] = word
                    word = ""
                    i += 1
                else:
                    word += ch
            idx += 1
            # Set index last candi sesuai id paling besar + 1
            config.last_idx_candi = current_id + 1
    # Mengurangi sisa candi dengan banyaknya candi -1 karena headernya ikut terload
    config.sisa_candi -= idx - 1
    
    
