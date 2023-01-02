from models import daftar_nilai
from views import input_nilai
from views import view_nilai as nilai

if __name__ == '__main__':
    no = 0

    while True:
        # opsi input pilihan C,R,U,D,F,Q
        tanya = input(
            "(C) Menambah data, | (R) Melihat semua data, | (U) Update data, | (D) Menghapus data, | (F) Mencari data, | (Q) Keluar program : \n")
        if tanya in ("c", "C"):
            # melakukan perulangan hingga user memilih n maka perulangan akan berhenti
            while True:
                no += 1
                # memanggil fungsi tambahData dan memparsing data no
                input_nilai.input_data(no)
                print("y or more] Tambah data, n] stop ")
                tambahDataLagi = input("Tambah data lagi ? (y/n) :")
                if tambahDataLagi == 'n':
                    break
            # jika tanya == R maka lihat semua data
        elif tanya in("r", "R"):
            # menampilkan data dalam bentuk table menggunakan package tabulate
            nilai.cetak_daftar_nilai()
            # jika tanya == D maka edit data
        elif tanya in ("u", "U"):
            daftar_nilai.ubah_data()
            # jika tanya == D maka hapus data
        elif tanya in ("d", "D"):
            daftar_nilai.hapus_data()
            # jika tanya == F maka Cari data
        elif tanya in ("f", "F"):
            daftar_nilai.cari_data()
        # jika tanya == Q maka keluar dari program
        elif tanya in ("q", "Q"):
            print("")
            print("Anda telah keluar dari program.")
            break
