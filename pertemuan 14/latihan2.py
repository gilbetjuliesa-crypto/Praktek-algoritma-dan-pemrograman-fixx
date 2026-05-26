def palindrom(teks):
    if len(teks) <= 1:
        return True
    
    kata_depan = teks[0]
    kata_belakang = teks[-1]
    
    if kata_depan == kata_belakang:
        return palindrom(teks[1:-1])
    else:
        return False

kalimat = input("Masukkan kalimat: ")

kalimat_baru = kalimat.lower()
kalimat_baru = kalimat_baru.replace(" ", "")
hasil = palindrom(kalimat_baru)

if hasil:
    print("Kalimat tersebut adalah PALINDROM")
else:
    print("Kalimat tersebut BUKAN PALINDROM")