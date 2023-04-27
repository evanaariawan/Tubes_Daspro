from fitur import load
import command
import argparse
import os
import time


# Membuat parser
parser = argparse.ArgumentParser(description='Mencari folder dan meload file di dalamnya.')
parser.add_argument("nama_folder")
args = parser.parse_args()

# Menentukan path folder yang akan diloadt
dir_data_awal = os.path.join(os.getcwd(),args.nama_folder) 
dir_data_save = os.path.join(os.getcwd(), 'save', args.nama_folder)

# Ada atau tidak folder yang dituju, jika ada jalankan program
if os.path.exists(dir_data_awal) or  os.path.exists(dir_data_save): 
    # Meload file - file pada folder tersebut ke dalam matriks
    load.load(args.nama_folder)

    print("Loading ...")
    time.sleep(2)
    print("Selamat Datang di Tubes Daspro!, Program Membangun Candi.")
    print('Ketik "help" untuk mengetahui perintah apa yang bisa Anda akses!')
    print()
    
    # Menjalankan main loop program
    while True:
        cmd = input(">>> ")
        command.run(cmd)
        print()
        
# Jika folder tidak ada, tampilkan pesan
else:
    print(f'Folder "{args.nama_folder}" tak ditemukan pada directory ini!')


