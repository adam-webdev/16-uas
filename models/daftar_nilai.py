from views import view_nilai
from tabulate import tabulate

dataMahasiswa = {
    'No': [],
    'Nim': [],
    'Nama': [],
    'Tugas': [],
    'Uts': [],
    'Uas': [],
    'Nilai Akhir': []
}

# fungsi mengembalikan dataMahasiswa


def index():
    return dataMahasiswa

# fungsi tambah data


def tambah_data(no, nim, nama, tugas, uas, uts):
    nilai_akhir = tugas * 30 / 100 + uts * 35 / 100 + uas * 35 / 100
    # menambahkan data
    dataMahasiswa['No'].append(no)
    dataMahasiswa['Nim'].append(nim)
    dataMahasiswa['Nama'].append(nama)
    dataMahasiswa['Tugas'].append(tugas)
    dataMahasiswa['Uts'].append(uts)
    dataMahasiswa['Uas'].append(uas)
    dataMahasiswa['Nilai Akhir'].append(nilai_akhir)
    print('Data berhasil ditambahkan.')


# fungsi untuk Mengedit data


def ubah_data():
    # print data untuk referensi nim pada data yang mau dihapus
    print(tabulate(dataMahasiswa, headers=[
        'No', 'NIM', 'Nama', 'Tugas', 'UTS', 'UAS', 'Nilai Akhir'], tablefmt="fancy_grid"))

    # cek jika ada nama  tersebut di dataMahasiswa
    nim = int(input('Masukan NIM yang mau diedit  :'))

    if nim in dataMahasiswa['Nim']:
        # cari posisi indexnya lalu disimpan di nimIndex
        nimIndex = dataMahasiswa['Nim'].index(nim)
        print("Pilih Data yang mau diedit")
        # perulangan mengedit data dalam bentuk pilihan
        while True:
            editApa = int(input(
                "(1) Nim, |  (2) Nama, | (3) Nilai Tugas, | (4) Nilai Uts, | (5) Nilai Uas, | (0) Save Perubahan & exit  : \n"))
            print("")

            if editApa == 1:
                # jika memilih opsi 1 merubah nim
                newNim = int(input("Masukan Nim :"))
                dataMahasiswa['Nim'][nimIndex] = newNim
            elif editApa == 2:
                # jika memilih opsi 2 merubah nama
                newNama = input("Masukan Nama :")
                dataMahasiswa['Nama'][nimIndex] = newNama
            elif editApa == 3:
                # jika memilih opsi 3 merubah nilai tugas & nilai akhir
                newTugas = int(input("Masukan Nilai Tugas :"))
                # memperbarui nilai akhir
                nilai_akhir = (newTugas * 30 / 100) + (dataMahasiswa['Uts'][nimIndex] * 35 / 100) + (
                    dataMahasiswa['Uas'][nimIndex] * 35 / 100)
                dataMahasiswa['Tugas'][nimIndex] = newTugas
                dataMahasiswa['Nilai Akhir'][nimIndex] = nilai_akhir
            elif editApa == 4:
                # jika memilih opsi 4 merubah nilai uts & nilai akhir
                newUts = int(input("Masukan Nilai Uts :"))
                # memperbarui nilai akhir
                nilai_akhir = (dataMahasiswa['Tugas'][nimIndex] * 30 / 100) + (newUts * 35 / 100) + (
                    dataMahasiswa['Uas'][nimIndex] * 35 / 100)
                dataMahasiswa['Uts'][nimIndex] = newUts
                dataMahasiswa['Nilai Akhir'][nimIndex] = nilai_akhir
            elif editApa == 5:
                # jika memilih opsi 5 merubah nilai uas & nilai akhir
                newUas = int(input("Masukan Nilai Uas :"))
                # memperbarui nilai akhir
                nilai_akhir = (dataMahasiswa['Tugas'][nimIndex] * 30 / 100) + (dataMahasiswa['Uts'][nimIndex] * 35 / 100) + (
                    newUas * 35 / 100)
                dataMahasiswa['Uas'][nimIndex] = newUas
                dataMahasiswa['Nilai Akhir'][nimIndex] = nilai_akhir
            elif editApa == 0:
                # jika memilih opsi 0 menyimpan perubahan dan keluar dari edit data
                print('Perubahan Data berhasil disimpan,')
                break

    else:
        print("data tidak ditemukan")

# fungsi untuk Mencari data


def cari_data():

    nama = input('Masukan Nama yang mau dicari  :')
    # cek jika nama ada di dataMahasiswa cari lokasi indexnya
    if nama in dataMahasiswa['Nama']:
        namaIndex = dataMahasiswa['Nama'].index(nama)
        # simpan data di variable hasiPencarin pada position index yang telah ditemukan
        hasilPencarian = {
            'No': [dataMahasiswa['No'][namaIndex]],
            'Nim': [dataMahasiswa['Nim'][namaIndex]],
            'Nama': [dataMahasiswa['Nama'][namaIndex]],
            'Tugas': [dataMahasiswa['Tugas'][namaIndex]],
            'Uts': [dataMahasiswa['Uts'][namaIndex]],
            'Uas': [dataMahasiswa['Uas'][namaIndex]],
            'Nilai Akhir': [dataMahasiswa['Nilai Akhir'][namaIndex]],
        }
        # memparsing parameter hasil pencarian ke modul cetak hasil pencarian
        view_nilai.cetak_hasil_pencarian(hasilPencarian)
    else:
        print("data tidak ditemukan")

# fungsi untuk Menghapus data


def hapus_data():
    # print data untuk referensi nim pada data yang mau dihapus
    print(tabulate(dataMahasiswa, headers=[
        'No', 'NIM', 'Nama', 'Tugas', 'UTS', 'UAS', 'Nilai Akhir'], tablefmt="fancy_grid"))
    nim = int(input('Masukan NIM yang mau dihapus  :'))
    # cek jika nim ada di dataMahasiswa cari lokasi indexnya
    if nim in dataMahasiswa['Nim']:
        nimIndex = dataMahasiswa['Nim'].index(nim)
        # menghapus data berdasarkan position index yang telah ditemukan
        del dataMahasiswa['No'][nimIndex]
        del dataMahasiswa['Nim'][nimIndex]
        del dataMahasiswa['Nama'][nimIndex]
        del dataMahasiswa['Tugas'][nimIndex]
        del dataMahasiswa['Uts'][nimIndex]
        del dataMahasiswa['Uas'][nimIndex]
        del dataMahasiswa['Nilai Akhir'][nimIndex]
        print("data berhasil dihapus.  ")
    else:
        print("data tidak ditemukan")
