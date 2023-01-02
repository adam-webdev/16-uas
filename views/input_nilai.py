# import module daftar nilai dari models
from models import daftar_nilai as daftar


def input_data(no):
    # input seluruh data
    while True:
        try:
            nim = int(input("Masukan NIM : "))
            if nim == '':
                print('Masukan Nim, Tidak boleh Kosong !')
        except ValueError:
            print('Masukan Nim dengan Angka !')
        else:
            break

    while True:
        nama = input("Masukan Nama : ")
        if nama == '':
            print("Nama tidak boleh kosong!")
        else:
            break

    while True:
        try:
            tugas = int(input("Masukan Nilai Tugas : "))
            if tugas == '':
                print("Nilai Tugas tidak boleh kosong!")
        except ValueError:
            print('Nilai tugas harus Angka !')
        else:
            break

    while True:
        try:
            uts = int(input("Masukan Nilai Uts : "))
            if uts == '':
                print("Nilai uts tidak boleh kosong!")
        except ValueError:
            print('Nilai uts harus Angka !')
        else:
            break

    while True:
        try:
            uas = int(input("Masukan Nilai Uas: "))
            if uas == '':
                print("Nilai uas tidak boleh kosong!")
        except ValueError:
            print('Nilai uas harus Angka !')
        else:
            break

    daftar.tambah_data(no, nim, nama, tugas, uas, uts)
