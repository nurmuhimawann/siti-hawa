import csv  # Import modul csv untuk mengolah file csv
import os   # Import modul os yang nantinya akan dimasukkan kedalam function untuk membersihkan terminal

# Variabel umum untuk menentukan file csv yang yang digunakan
csv_data = 'DataMahasiswa.csv'
csv_login = 'FormLogin.csv'

# Function untuk membersihkan terminal
def hapus_tampilan():
    os.system('cls')


# BARIS KODE UNTUK MENU LOGIN
# Function untuk menampilkan menu utama login Aplikasi
def menu_login():
    hapus_tampilan()
    # Menampilkan bar header dan menu utama login Aplikasi
    print("==============================================================")
    print("SELAMAT DATANG DI APLIKASI SITI HAWA UNEJ".center(62))
    print("--------------------------------------------------------------")
    print("Sistem Informasi Pengolahan Data Mahasiswa Universitas Jember")
    print("==============================================================")
    print(
        "Menu Aplikasi"
        "\n[1] Login"
        "\n[2] Register Akun"
        "\n[3] Tentang Aplikasi"
        "\n[0] Keluar"
        "\n\nHarap masuk dengan Akun yang sudah terdaftar."
        "\nJika belum mempunyai Akun. Harap Register terlebih dahulu.")
    print("==============================================================")

    # Percabangan untuk memilih menu
    pilih = input("Pilih menu>> ")
    if pilih == '1':
        login()
    elif pilih == '2':
        register()
    elif pilih == '3':
        tentang_aplikasi()
    elif pilih == '0':
        exit()
    else:
        print("Mohon maaf. Anda telah memilih menu yang salah!!!")
        kembali_login()


# Function untuk menampilkan perintah kembali ke halaman login
def kembali_login():
    print("\n")
    input("Tekan Enter untuk kembali ke halaman login...")
    menu_login()


# Function untuk menampilkan perintah masuk ke Aplikasi
def masuk_aplikasi():
    print("\n")
    input("Tekan Enter untuk masuk ke Aplikasi Siti Hawa UNEJ...")
    menu()


# Function untuk login ke Aplikasi
def login():
    hapus_tampilan()
    # Membuka file csv dengan mode Read/Baca
    data = []
    with open(csv_login) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    # Menampilkan bar header Aplikasi
    print('='*54)
    print('{0:^54s}'.format('LOGIN APLIKASI SITI HAWA UNEJ'))
    print('='*54)
    print("MASUK")
    print("-"*54)

    # Inputan user untuk masuk ke Aplikasi
    Username = input("Masukkan Username Anda>> ")
    Password = input("Masukkan Password Anda>> ")

    # Mencocokkan inputan user dengan data yang ada di file csv
    index0 = [x[0] for x in data]
    index1 = [x[1] for x in data]

    # Percabangan untuk cross check inputan dengan data di file csv
    if Username in index0:
        for i in range(0, len(index0)):
            if index0[i] == Username and index1[i] == Password:
                print("-"*54)
                print("Anda berhasil masuk")
                print("="*54)
                masuk_aplikasi()

    else:
        print("Username atau password yang Anda masukkan salah!!!")
        kembali_login()


# Function untuk melakukan pendaftaran Akun
def register():
    hapus_tampilan()
    # Menampilkan bar header Aplikasi
    print('='*58)
    print('{0:^58s}'.format('REGISTERASI AKUN SITI HAWA UNEJ'))
    print('='*58)
    print("Register Akun")
    print('-'*58)

    # Inputan user untuk mendaftarkan Akun
    username = input("Masukkan username yang Anda inginkan>> ")
    password = input("Masukkan password yang Anda inginkan>> ")

    # Menambahkan data ke dalam file csv dengan mode a/append
    with open(csv_login, mode='a', newline='') as csvfile:
        fieldnames = ['Username', 'Password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Username': username, 'Password': password})

    # Menampilkan output Akun user
    print('-'*58)
    print("Selamaaat Akun Anda telah berhasil dibuat")
    print(
        f"Username Anda adalah : {username} \nPassword Anda adalah : {password}")
    print("\nHarap untuk mengingat baik-baik Username & Password Anda")
    print('='*58)

    kembali_login()


# Function untuk menampilkan fitur Tentang Aplikasi
def tentang_aplikasi():
    hapus_tampilan()
    # Menampilkan bar header Aplikasi
    print('='*50)
    print('{0:^50s}'.format('TENTANG APLIKASI SITI HAWA UNEJ'))
    print('='*50)
    print("About")
    print('-'*50)

    # Menampilkan info tentang data perancang Aplikasi
    print(
        "Nama    : Nur Muhammad Himawan"
        "\nNIM     : 202410101070"
        "\nProdi   : Sistem Informasi")

    print('-'*50)

    print(
        "Nama    : Naufal Reza Pahlevi"
        "\nNIM     : 202410101120"
        "\nProdi   : Sistem Informasi")
    print('='*50)

    kembali_login()


# BARIS KODE UNTUK APLIKASI UTAMA
# Function untuk menampilkan menu
def menu():
    hapus_tampilan()
    # Menampilkan bar header dan menu utama Aplikasi
    print("==============================================================")
    print("SITI HAWA : APLIKASI DAFTAR DATA MAHASISWA".center(62))
    print("--------------------------------------------------------------")
    print("Sistem Informasi Pengolahan Data Mahasiswa Universitas Jember".center(62))
    print("==============================================================")
    print("DAFTAR MENU APLIKASI")
    print("-"*62)
    print("[1] Lihat Data Mahasiswa")
    print("[2] Buat Data Mahasiswa Baru")
    print("[3] Hapus Data Mahasiswa")
    print("[4] Cari Data Mahasiswa")
    print("[5] Edit Data Mahasiswa")
    print("[0] Keluar")
    print("==============================================================")

    # Percabangan bagi user untuk memilih menu
    menu_yang_dipilih = input("Pilih menu> ")
    if menu_yang_dipilih == '1':
        lihat_data()
    elif menu_yang_dipilih == '2':
        tambah_data()
    elif menu_yang_dipilih == '3':
        hapus_data()
    elif menu_yang_dipilih == '4':
        cari_data()
    elif menu_yang_dipilih == '5':
        edit_data()
    elif menu_yang_dipilih == '0':
        print('Terimakasih. \nAnda telah menggunakan Aplikasi Daftar Data Mahasiswa')
        kembali_login()
    else:
        print("Mohon Maaf. Kamu memilih menu yang salah!!!")

    kembali_ke_menu()


# Function untuk menampilkan perintah kembali ke menu
def kembali_ke_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    menu()


# Function untuk melihat daftar data mahasiswa
def lihat_data():
    hapus_tampilan()

    # Baris kode untuk menampilkan jumlah data
    Data = []
    with open(csv_data, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            Data.append(row)
    jumlah_data = sum(1 for row in Data)

    # Preview daftar data mahasiswa
    print("="*46)
    print("Daftar Data Mahasiswa".center(46))
    print("="*46)

    print('NO \t NIM \t\t Nama Mahasiswa')
    print("-"*46)

    # Looping untuk mengeluarkan datanya
    for data in Data:
        print(f"{data['NO']} \t {data['NIM']} \t {data['Nama Mahasiswa']}")
    print("-"*46)
    print("Total Data: ", jumlah_data)
    print("="*46)

    kembali_ke_menu()


# Function untuk menambahkan data ke dalam daftar data mahasiswa
def tambah_data():
    hapus_tampilan()
    # Membuka dan menambahkan data ke file csv dengan mode a/append
    with open(csv_data, mode='a', newline='') as csv_file:
        fieldnames = ['NO', 'NIM', 'Nama Mahasiswa']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        print('='*50)
        print('{0:^50s}'.format('Tambah Data Mahasiswa'))
        print('='*50)
        print("Dipersilakan untuk mengisi form data dibawah ini")

        # Baris kode untuk menambahkan data baru
        no = int(input("\nNO : "))
        nim = input("NIM Baru : ")
        nama = input("Nama Mahasiswa Baru : ")

        print('='*50)

        writer.writerow({'NO': no, 'NIM': nim, 'Nama Mahasiswa': nama})
    print("Data yang Anda masukkan telah sukses ditambahkan")

    kembali_ke_menu()


# Function untuk menghapus data mahasiswa
def hapus_data():
    hapus_tampilan()

    # Menampilkan preview daftar data mahasiswa
    # Membuka file csv dengan mode Read/Baca
    Data = []
    with open(csv_data, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Data.append(row)

    # Menampilkan bar header fitur Aplikasi
    print("="*60)
    print("Preview Daftar Data Mahasiswa".center(60))
    print("="*60)

    print('NO \t NIM \t\t Nama Mahasiswa')
    print("-"*60)

    # Looping untuk mengeluarkan datanya
    for data in Data:
        print(f"{data['NO']} \t {data['NIM']} \t {data['Nama Mahasiswa']}")

    print("="*60)
    print('{0:^60s}'.format('Hapus Data Mahasiswa'))
    print('='*60)

    # Baris kode untuk menghapus data
    nim = input("Masukkan NIM untuk data yang ingin Anda hapus : ")

    # Mencocokkan inputan user dengan data di file csv
    indeks = 0
    for data in Data:
        if (data['NIM'] == nim):
            Data.remove(Data[indeks])
        indeks = indeks + 1

    # Menulis data baru ke file csv
    with open(csv_data, mode='w', newline='') as csv_file:
        fieldnames = ['NO', 'NIM', 'Nama Mahasiswa']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in Data:
            writer.writerow(
                {'NO': new_data['NO'], 'NIM': new_data['NIM'], 'Nama Mahasiswa': new_data['Nama Mahasiswa']})

    # Menampilkan output sukses menghapus data
    print('')
    print('='*60)
    print("Data telah berhasil dihapus dari Daftar Data Mahasiswa")
    print("Anda bisa mengecek kembali di menu lihat data. Terimakasih.")
    kembali_ke_menu()


# Function untuk mencari data mahasiswa
def cari_data():
    hapus_tampilan()

    # Membuka file csv dengan mode Read / Baca
    Data = []
    with open(csv_data, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Data.append(row)

    # Menampilkan bar header fitur Aplikasi
    print('='*55)
    print('{0:^55s}'.format('Pencarian Data Mahasiswa'))
    print('='*55)

    # Inputan bagi user untuk mencari data yang diinginkan
    nim_nama = input("Cari berdasarkan NIM atau Nama Mahasiswa : ")

    data_ditemukan = []

    # Mencari data mahasiswa
    indeks = 0
    for data in Data:
        if (data['NIM'] == nim_nama):
            data_ditemukan = Data[indeks]
        if (data['Nama Mahasiswa'] == nim_nama):
            data_ditemukan = Data[indeks]

        indeks = indeks + 1

    # Percabangan untuk menampilkan output pencarian
    if len(data_ditemukan) > 0:
        print('-'*55)
        print("DATA MAHASISWA DITEMUKAN")
        print('')
        print(f"NAMA : {data_ditemukan['Nama Mahasiswa']}")
        print(f"NIM  : {data_ditemukan['NIM']}")
        print('='*55)
    else:
        print('-'*55)
        print("DATA MAHASISWA TIDAK DITEMUKAN")
        print('')
        print("Mohon Maaf. Data yang Anda cari tidak ditemukan")
        print('='*55)

    kembali_ke_menu()


# Function untuk mengubah data mahasiswa
def edit_data():
    hapus_tampilan()

    # Menampilkan preview daftar data mahasiswa
    # Membuka file csv dengan mode Read/Baca
    Data = []
    with open(csv_data, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            Data.append(row)

    jumlah_data = sum(1 for row in Data)

    # Menampilkan bar header fitur Aplikasi
    print("="*46)
    print("Preview Daftar Data Mahasiswa".center(46))
    print("="*46)

    print('NO \t NIM \t\t Nama Mahasiswa')
    print("-"*46)

    # Looping untuk mengeluarkan datanya
    for data in Data:
        print(f"{data['NO']} \t {data['NIM']} \t {data['Nama Mahasiswa']}")
    print("-"*46)
    print("Total Data :", jumlah_data, "Data Mahasiswa")

    # Baris kode untuk mengupdate data
    print('='*46)
    print('{0:^46s}'.format('Ubah Data Mahasiswa'))
    print('='*46)

    # Inputan bagi user untuk memilih data yang akan di update
    no = input("Pilih Nomor data yang ingin Anda ubah : ")

    print('-'*46)

    # Mencari dan Mengubah Data
    indeks = 0
    for data in Data:
        if (data['NO'] == no):
            Data[indeks]['Nama Mahasiswa'] = input("Masukkan Nama baru : ")
            Data[indeks]['NIM'] = int(input("Masukkan NIM baru  : "))
        indeks = indeks + 1

    # Menulis data baru ke file csv
    with open(csv_data, mode='w', newline='') as csv_file:
        fieldnames = ['NO', 'NIM', 'Nama Mahasiswa']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in Data:
            writer.writerow(
                {'NO': i['NO'], 'NIM': i['NIM'], 'Nama Mahasiswa': i['Nama Mahasiswa']})

    # Menampilkan output sukses mengupdate data
    print('')
    print('='*46)
    print("Data Anda telah berhasil di update")
    print("Anda bisa mengecek kembali di menu lihat data")
    print("Terimakasih")
    kembali_ke_menu()


# Looping menjalankan progamnya
while True:
    menu_login()  # memanggil fungsi menu
    break
