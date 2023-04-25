from fitur import info, keluar, log, summonjin, hapusjin, ubahjin, batch, kumpul, bangun, roro, laporan, save
import fitur.config as config


# Menerima masukan command dan menjalankan prosedur sesuai perintah yang dimasukan.
# Pada perintah tertentu, diperiksa role akun yang login terlebih dahulu
def run(cmd):
    if cmd == "login":
        log.login()
    elif cmd == "logout":
        log.logout()
    elif cmd == "help":
        info.help()
    elif cmd == "summonjin":
        if config.logged_in_user[1] == "bandung_bondowoso":
            summonjin.manggil_jin()
        else:
            print("Tidak dapat mengakses perintah tersebut!")
    elif cmd == "hapusjin":
        if config.logged_in_user[1] == "bandung_bondowoso":
            hapusjin.ilangin_jin()
        else:
            print("Tidak dapat mengakses perintah tersebut!")
    elif cmd == "ubahjin":
        if config.logged_in_user[1] == "bandung_bondowoso":
            ubahjin.ubah_jin()
        else:
            print("Tidak dapat mengakses perintah tersebut!")
    elif cmd == "batchkumpul":
        if config.logged_in_user[1] == "bandung_bondowoso":
            batch.kumpul()
        else:
            print("Tidak dapat mengakses perintah tersebut!")
    elif cmd == "batchbangun":
        if config.logged_in_user[1] == "bandung_bondowoso":
            batch.bangun()
        else:
            print("Tidak dapat mengakses perintah tersebut!")
    elif cmd == "laporanjin":
        if config.logged_in_user[1] == "bandung_bondowoso":
            laporan.jin()
        else:
            print("Tidak dapat mengakses perintah tersebut!")
    elif cmd == "laporancandi":
        if config.logged_in_user[1] == "bandung_bondowoso":
            laporan.candi()
        else:
            print("Tidak dapat mengakses perintah tersebut!")
    elif cmd == "kumpul":
        if config.logged_in_user[1] == "jin_pengumpul":
            kumpul.ngumpulin_bahan()
        else:
            print("Tidak dapat mengakses perintah tersebut!")
    elif cmd == "bangun":
        if config.logged_in_user[1] == "jin_pembangun":
            bangun.bangun_candi()
        else:
            print("Tidak dapat mengakses perintah tersebut!")
    elif cmd == "hancurkancandi":
        if config.logged_in_user[1] == "roro_jonggrang":
            roro.hancurkan_candi()
        else:
            print("Tidak dapat mengakses perintah tersebut!")
    elif cmd == "ayamberkokok":
        if config.logged_in_user[1] == "roro_jonggrang":
            roro.manggil_ayam()
        else:
            print("Tidak dapat mengakses perintah tersebut!")
    elif cmd == "save":
        save.save()
    elif cmd == "exit":
        keluar.keluar()
    else:
        print('Perintah tak dimengerti, silahkan ketik help untuk mengetahui perintah yang dapat diakses!')
