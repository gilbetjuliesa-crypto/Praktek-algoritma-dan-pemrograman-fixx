def baca_kata(nama_file):
    try:
        file = open(nama_file, 'r')
        isi = file.read().lower().split()
        file.close()
        return isi
    except FileNotFoundError:
        print(f"Error: file '{nama_file}' tidak ditemukan!")
        return None
    except:
        print(f"Error: file '{nama_file}' tidak bisa dibaca!")
        return None

def cari_kata_sama(list1, list2):
    hasil = []
    for kata in list1:
        if kata in list2 and kata not in hasil:
            hasil.append(kata)
    return hasil

file1 = input("Masukkan nama file pertama: ")
file2 = input("Masukkan nama file kedua: ")

kata1 = baca_kata(file1)
kata2 = baca_kata(file2)

if kata1 is not None and kata2 is not None:
    hasil = cari_kata_sama(kata1, kata2)
    
    print("\nKata yang muncul di kedua file:")
    print(set(hasil))

