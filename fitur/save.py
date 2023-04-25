import config
import os
import time

def save():
    folder = input("Masukkan nama folder: ")
    # Menentukan path folder save
    folder_save_path = os.path.join(os.getcwd(),'save')

    # Periksa apakah folder ada, jika tidak buat foldernya
    if not os.path.exists(folder_save_path):
        print("Membuat save folder...")
        os.mkdir(folder_save_path)
        time.sleep(2)

    # Membuat path folder save baru di dalam folder save sebelumnya
    new_save_folder = os.path.join(folder_save_path, folder)
    os.mkdir(new_save_folder)
    print(f"Membuat folder save/{folder}...")
    time.sleep(2)

    # Menyimpan user.csv
    file_user = os.path.join(new_save_folder, 'user.csv')
    with open(file_user, 'w') as f:
        for i in range(config.count_users):
            words = ''
            for j in range(3):
                words += config.users[i][j]
                if j < 2:
                    words += ';'

            f.write(words + '\n')
        f.close()

    # Menyimpan bahan_bangunan.csv
    file_bahan = os.path.join(new_save_folder, 'bahan_bangunan.csv')
    with open(file_bahan,'w') as f:
        for i in range(4):
            words = ''
            for j in range(3):
                words += str(config.bahan[i][j])
                if j < 2 :
                    words += ';'
            f.write(words + '\n')
        f.close()
    
    # Menyimpan file candi.csv
    file_candi = os.path.join(new_save_folder, 'candi.csv')
    with open(file_candi,'w') as f:
        for i in range(config.last_idx_candi):
            words = ''
            if config.candi[i][0] != '':
                for j in range(5):
                    words += str(config.candi[i][j])
                    if j < 4:
                        words += ';'
                f.write(words + '\n')
        f.close()
    print(f'Berhasil menyimpan data di folder save/{folder}1')