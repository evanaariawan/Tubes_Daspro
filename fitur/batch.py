import config
import random

def kumpul():
    # Periksa apakah ada jin pengumpul yang tersedia
    if config.count_jin_pengumpul > 0:
        print(f"Mengerahkan {config.count_jin_pengumpul} jin untuk mengumpulkan bahan.")
        # Inisiasi variabel bahan yang akan digunakan
        pasir_didapatkan = 0
        batu_didapatkan = 0
        air_didapatkan = 0

        # Melakukan loop sebanyak jin pengumpul untuk melakukan random angka dari 0 - 5
        for _ in range(config.count_jin_pengumpul):
            # Setiap loop variabel bahan ditambahkan dengan hasil random
            pasir_didapatkan += random.randint(0, 5)
            batu_didapatkan += random.randint(0, 5)
            air_didapatkan += random.randint(0,5)

        # Menambahkan bahan bangunan yang didapat pada matriks bahan bangunan
        config.bahan[1][2] += pasir_didapatkan
        config.bahan[2][2] += batu_didapatkan
        config.bahan[3][2] += air_didapatkan

        # Menampilkan pesan jumlah bahan yang didapatkan
        print(f"Jin menemukan total {pasir_didapatkan} pasir, {batu_didapatkan} batu, dan {air_didapatkan} air.")
        
    # Jika tidak ada jin pengumpul, tampilkan pesan
    else:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

def bangun():
    # Periksa apakah ada jin pembangun
    if config.count_jin_pembangun > 0:
        # Inisiasi variabel bahan yang akan digunakan
        total_pasir = 0
        total_batu = 0
        total_air = 0
        # Inisiasi data matriks candi yang dibangun dengan ukuran sebanyak jin pembangun
        candi_dibangun = [['' for _ in range(5)] for _ in range(config.count_jin_pembangun)]
        # idx sebagai index untuk mengakses matriks candi di atas
        idx = 0

        # Melakukan loop pada matriks user dimulai dari index ke 3
        for i in range(3, config.count_users):
            # Periksa jika user pada index i rolenya adalah jin_pembangun
            if config.users[i][2] == "jin_pembangun":
                # Setiap ditemukan mengenerate random angka untuk masing - masing bahan yang digunakan
                pasir_digunakan = random.randint(1, 5)
                batu_digunakan = random.randint(1, 5)
                air_digunakan = random.randint(1, 5)

                # Data berupa username jin dan bahan yang digunakan ditambahkan ke dalam matriks data candi yang dibangun
                candi_dibangun[idx] = ['', config.users[i][0], pasir_digunakan, batu_digunakan, air_digunakan]
                # idx ditambah untuk merubah data dengan index selanjutnya
                idx += 1
                # Menambahkan jumlah bahan bangunan yang digunakan pada variabel awal
                total_pasir += pasir_digunakan
                total_batu += batu_digunakan
                total_air += air_digunakan

        # Menampilkan informasi terkait pembangunan candi 
        print(f"Mengerahkan {config.count_jin_pembangun} jin untuk membangun candi dengan total bahan {total_pasir} pasir, {total_batu} batu, dan {total_air} air. ")
        # Periksa apakah bahan yang digunakan untuk membangun semua candi tersedia
        if (config.bahan[1][2] >= total_pasir) and (config.bahan[2][2] >= total_batu) and (config.bahan[3][2] >= total_air):
            # Jika ada, proses dilanjutkan
            # Melakukan looping sebanyak jumlah jin pembangun
            for i in range(config.count_jin_pembangun):
                # Data matriks candi yang dibangun ke i akan ditambahkan bila masih ada sisa candi yang perlu dibangun
                if config.sisa_candi > 0:
                    # Melakukan looping pada matriks candi utama (global) untuk memasukkan data candi yang dibangun pada index terkecil
                    for j in range(config.last_idx_candi + 1):
                        if config.candi[j][0] == '':
                            # Memberikan id candi sesuai dengan index dan menyimpannya pada index tersebut
                            candi_dibangun[i][0] = str(j)
                            config.candi[j] = candi_dibangun[i]
                            # Mengurangi sisa candi setiap penambahan data
                            config.sisa_candi -= 1
                            # Jika candi ditambahkan pada paling akhir, last_idx_candi ditambahkan 
                            if j == config.last_idx_candi:
                                config.last_idx_candi += 1
                            # Loop berhenti setelah menyimpan candi
                            break

                            
            # Mengurangi data matriks bahan dengan total bahan yang digunakan pada batch bangun di atas
            config.bahan[1][2] -= total_pasir
            config.bahan[2][2] -= total_batu
            config.bahan[3][2] -= total_air

            # Menampilkan informasi setelah melakukan batch bangun
            print(f"Jin berhasil membangun total {config.count_jin_pembangun} candi.")
            print(f"Sisa candi yang perlu dibangun : {config.sisa_candi}")

        # Jika bahan kurang, tampilkan pesan terkait kekurangan bahan
        else:

            kurang_pasir = (total_pasir -  config.bahan[1][2])  if (total_pasir -  config.bahan[1][2]) >= 0 else 0
            kurang_batu = (total_batu -  config.bahan[2][2])  if (total_batu -  config.bahan[2][2]) >= 0 else 0
            kurang_air = (total_air -  config.bahan[3][2])  if (total_air -  config.bahan[3][2]) >= 0 else 0

            print(f"Bangun gagal. Kurang {kurang_pasir} pasir, {kurang_batu} batu, dan {kurang_air} air.")
            
    # Jika tidak ada jin pembangun, tampilkan pesan
    else:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
        
                
