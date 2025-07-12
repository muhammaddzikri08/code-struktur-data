import csv
import os

FILE_NAME = 'data_siswa.csv'

# Inisialisasi file CSV
def inisialisasi_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['No', 'NISN', 'Nama', 'Alamat', 'No HP', 'Jenis Kelamin'])

# Fitur 1: Tambah data siswa
def tambah_siswa():
    nisn = input("Masukkan NISN: ")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    no_hp = input("Masukkan No HP: ")
    jenis_kelamin = input("Masukkan Jenis Kelamin (Laki-laki/Prempuan): ")

    with open(FILE_NAME, mode='r', newline='') as file:
        reader = list(csv.reader(file))
        no_urut = len(reader)

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([no_urut, nisn, nama, alamat, no_hp, jenis_kelamin])
    print("✅ Data siswa berhasil ditambahkan!\n")

# Fitur 2: Tampilkan seluruh data siswa
def tampilkan_data():
    with open(FILE_NAME, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print('\t'.join(row))
    print()

# Fitur 3: Edit data siswa berdasarkan NISN
def edit_data():
    nisn_edit = input("Masukkan NISN siswa yang akan diedit: ")
    updated = False

    with open(FILE_NAME, mode='r', newline='') as file:
        reader = list(csv.reader(file))

    for i in range(1, len(reader)):
        if reader[i][1] == nisn_edit:
            print("Data lama:", reader[i])
            reader[i][2] = input("Nama baru: ") or reader[i][2]
            reader[i][3] = input("Alamat baru: ") or reader[i][3]
            reader[i][4] = input("No HP baru: ") or reader[i][4]
            reader[i][5] = input("Jenis Kelamin baru (L/P): ") or reader[i][5]
            updated = True
            break

    if updated:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)
        print("✅ Data berhasil diperbarui!\n")
    else:
        print("❌ NISN tidak ditemukan.\n")

# Fitur 4: Hapus data siswa berdasarkan NISN
def hapus_data():
    nisn_hapus = input("Masukkan NISN siswa yang akan dihapus: ")
    deleted = False

    with open(FILE_NAME, mode='r', newline='') as file:
        reader = list(csv.reader(file))

    new_data = [reader[0]]
    no = 1
    for i in range(1, len(reader)):
        if reader[i][1] != nisn_hapus:
            reader[i][0] = str(no)
            new_data.append(reader[i])
            no += 1
        else:
            deleted = True

    if deleted:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_data)
        print("✅ Data berhasil dihapus!\n")
    else:
        print("❌ NISN tidak ditemukan.\n")

# Menu utama
def menu():
    inisialisasi_file()
    while True:
        print("=== APLIKASI PENDAFTARAN SISWA BARU ===")
        print("1. Tambah Siswa")
        print("2. Tampilkan Semua Data")
        print("3. Edit Data Siswa")
        print("4. Hapus Data Siswa")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tambah_siswa()
        elif pilihan == '2':
            tampilkan_data()
        elif pilihan == '3':
            edit_data()
        elif pilihan == '4':
            hapus_data()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("❌ Pilihan tidak valid. Coba lagi.\n")

# Jalankan program
if __name__ == '__main__':
    menu()
