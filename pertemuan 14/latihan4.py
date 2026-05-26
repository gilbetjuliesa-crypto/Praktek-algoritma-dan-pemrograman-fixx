def jumlah_digit(x):
    if x < 10:
        return x
    else:
        return (x % 10) + jumlah_digit(x // 10)

angka = int(input("Masukkan angka: "))
print("Jumlah digit:", jumlah_digit(angka))