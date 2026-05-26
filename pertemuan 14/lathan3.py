def jumlah_ganjil(x, i=1):
    if (2 * i - 1) > x:
        return 0

    return (2 * i - 1) + jumlah_ganjil(x, i + 1)

angka = int(input("Masukkan batas bilangan ganjil: "))

hasil = jumlah_ganjil(angka)
print("Jumlah deret ganjil =", hasil)