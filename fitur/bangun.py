import config
import random

def bangun_candi():
    # Mengenerate angka random dari 1 - 5 untuk masing - masing bahan
    pasir_digunakan = random.randint(1, 5)
    batu_digunakan = random.randint(1, 5)
    air_digunakan = random.randint(1,5)

    # Periksa apakah bahan digunakan tersedia
    if (config.bahan[1][2] >= pasir_digunakan) and (config.bahan[2][2] >= batu_digunakan) and (config.bahan[3][2] >= air_digunakan):
        config.bahan[1][2] -= pasir_digunakan
        config.bahan[2][2] -= batu_digunakan
        config.bahan[3][2] -= air_digunakan

        # Data candi akan disimpan apabila masih ada sisa candi yang perlu dibangun
        if config.sisa_candi > 0:
            # Memasukkan data pembangunan candi ke matriks data candi pada index yang kosong yang pertama kali ditemukan
            for i in range(config.last_idx_candi + 1):
                if config.candi[i][0] == '':
                    config.candi[i][0] = str(i)
                    config.candi[i][1] = config.logged_in_user[0]
                    config.candi[i][2] = pasir_digunakan
                    config.candi[i][3] = batu_digunakan
                    config.candi[i][4] = air_digunakan
                    config.sisa_candi -= 1

                    # Jika candi ditambahkan pada paling akhir, last_idx_candi ditambahkan
                    if i == config.last_idx_candi:
                        config.last_idx_candi += 1
                    break

        print("Candi berhasil dibangun.")
        print(f"Sisa candi yang perlu dibangun: {config.sisa_candi}")
        
    # Jika bahan tidak mencukupi, tampilkan pesan
    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
    