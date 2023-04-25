# Global variabel yang akan berganti seiring berjalannya program dengan mengimpor ke fungsi yang bersangkutan

# control login
logged_in = False

# users
users = [['' for _ in range(3)] for _ in range(103)] # Inisiasi matriks kosong. Keterangan idx 0 -> username, 1 -> pwd, 2 -> role
count_users = 0 # Batasan range untuk meloop nanti
logged_in_user = ['', ''] # Sebagai informasi username dan role akun yang login

# jin
count_jin_pengumpul = 0
count_jin_pembangun = 0


# bahan
bahan = [["" for _ in range(3)] for _ in range(4)]# Inisiasi matriks kosong. Keterangan idx 0 -> bahan, 1 -> deskripsi, 2 -> jumlah

# Candi
# Inisiasi matriks kosong. Keterangan idx 0 -> id, 1 -> pembuat, 2 -> pasir, 3 -> batu, 4 -> air
candi = [["" for _ in range(5)] for _ in range(105)]
last_idx_candi = 0 # Sebagai tracker untuk loop candi
sisa_candi = 100 
