def kombinasi(x, y):
    if y == 0 or y == x:
        return 1
    elif y > x or y < 0:
        return 0
    else:
        return kombinasi(x-1, y-1) + kombinasi(x-1, y)

x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))

print("Hasil kombinasi C(", x, ",", y, ") =", kombinasi(x, y))