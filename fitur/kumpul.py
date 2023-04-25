import config
import random


def ngumpulin_bahan():
    # Menggenerate angka random dari 0 - 5 untuk masing -  masing bahan
    pasir_didapatkan = random.randint(0, 5)
    batu_didapatkan = random.randint(0, 5)
    air_didapatkan = random.randint(0,5)

    # Menambahkan data bahan bangunan dengan hasil random angka di atas
    config.bahan[1][2] += pasir_didapatkan
    config.bahan[2][2] += batu_didapatkan
    config.bahan[3][2] += air_didapatkan

    print(f"Jin menemukan {pasir_didapatkan} pasir, {batu_didapatkan} batu , dan {air_didapatkan} air.")
