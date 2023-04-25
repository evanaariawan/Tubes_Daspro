from . import save

def keluar():
    # input_valid sebagai validator
    input_valid = False
    # Meminta validasi input sampai benar
    while not input_valid:
        konfirmasi = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N) ').upper()
        if konfirmasi == "Y" or konfirmasi == "N":
            input_valid = True
    # Melakukan prosedur save
    if konfirmasi == "Y":
        save.save()
    # Keluar program
    exit()