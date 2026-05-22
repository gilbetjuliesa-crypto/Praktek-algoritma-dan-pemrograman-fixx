def list_ke_set():
    data = eval(input("Masukkan List: "))
    print("Sebelum (List):", data)
    hasil = set(data)
    print("Sesudah (Set):", hasil)


def set_ke_list():
    data = eval(input("\nMasukkan Set: "))
    print("Sebelum (Set):", data)
    hasil = list(data)
    print("Sesudah (List):", hasil)


def tuple_ke_set():
    data = eval(input("\nMasukkan Tuple: "))
    print("Sebelum (Tuple):", data)
    hasil = set(data)
    print("Sesudah (Set):", hasil)


def set_ke_tuple():
    data = eval(input("\nMasukkan Set lagi: "))
    print("Sebelum (Set):", data)
    hasil = tuple(data)
    print("Sesudah (Tuple):", hasil)

list_ke_set()
set_ke_list()
tuple_ke_set()
set_ke_tuple()

