def cek_bilangan_prima(x, y):
    if x <= 1:
        return False
    
    if y == 1:
        return True
    
    if x % y == 0:
        return False

    return cek_bilangan_prima(x, y - 1)

angka = int(input("Masukkan bilangan: "))

if cek_bilangan_prima(angka, angka - 1):
    print(angka, "adalah bilangan PRIMA")
else:
    print(angka, "bukan bilangan PRIMA")