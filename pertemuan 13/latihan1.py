game = eval(input("Masukkan data kategori Game: "))
edukasi = eval(input("Masukkan data kategori Edukasi: "))
sosial = eval(input("Masukkan data kategori Sosial: "))

kategori = [game, edukasi, sosial]

hitung = {}
for k in kategori:
    for app in k:
        hitung[app] = hitung.get(app, 0) + 1

hanya_satu = {app for app, jml in hitung.items() if jml == 1}
tepat_dua = {app for app, jml in hitung.items() if jml == 2}

print("Hanya satu kategori:", hanya_satu)
print("Tepat dua kategori:", tepat_dua)

# input:
# {'ml','pubg','coc','subway'}
# {'duolingo','ruangguru','subway','coc'}
# {'instagram','whatsapp','ml','coc'}

