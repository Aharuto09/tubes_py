import re


class dataMahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi


def display():
    for i in mahasiswa:
        print("-------------------------")
        print("Nama  : ", i.nama)
        print("Nim   : ", i.nim)
        print("Prodi : ", i.prodi, "\n")


def edit(nama):
    for i in mahasiswa:
        if i.nama == nama:
            print("-------------------------")
            print("Ubah data ", i.nama)
            print("1. Nama")
            print("2. Nim")
            print("3. Prodi")
            print("0. Kembali")
            pilihedit = 1
            while pilihedit != 0:
                pilihedit = float(input("Pilih Edit : "))
                if pilihedit == 1:
                    ubahdata = input("Masukkan Data Baru : ")
                    i.nama = ubahdata
                elif pilihedit == 2:
                    ubahnim = input("Masukkan Data Baru : ")
                    i.nim = int(ubahnim)
                elif pilihedit == 3:
                    ubahprodi = input("Masukkan Data Baru : ")
                    i.prodi = ubahprodi
                else:
                    break


def delete(nama):
    for i in mahasiswa:
        if i.nama == nama:
            mahasiswa.remove(i)


def search(nama):
    for i in mahasiswa:
        if i.nama == nama:
            print("-------------------------")
            print("Nama  : ", i.nama)
            print("Nim   : ", i.nim)
            print("Prodi : ", i.prodi, "\n")


pilih = 1
mahasiswa = []
mahasiswa.append(dataMahasiswa("Abraham Samuel R",
                 1202200089, "Teknologi Informasi"))
while pilih < 5:
    print("Menu\n1. Tambah data baru\n2. hapus data\n3. ubah data\n4. tampilkan data")
    pilih = float(input("Pilih Menu "))
    if pilih == 1:
        print("tambah data baru")
        addnama = input("Masukkan Nama : ")
        addnim = int(input("Masukkan Nim : "))
        addprodi = input("Masukkan Prodi : ")
        mahasiswa.append(dataMahasiswa(addnama, addnim, addprodi))
        print("Data Mahasiswa Ditambahkan")
    elif pilih == 2:
        print("Data Mahasiswa")
        hapus = input("Masukkan Nama yang ingin di hapus : ")

    elif pilih == 3:
        print("Ubah Data")
        ubah = input("Masukkan Nama yang ingin di ubah : ")
        edit(ubah)

    elif pilih == 4:
        display()
    else:
        break
