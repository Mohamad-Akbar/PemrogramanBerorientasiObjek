import sqlite3
import pathlib
import getpass

class DataManager:
    def __init__(self):
        database = str(pathlib.Path().absolute())+"/projek.db"
        self.connector = sqlite3.connect(database)
        self.cursor = self.connector.cursor()
        
    def executeQuery(self, query, retVal=False):
        self.cursor.execute(query)
        all_results = self.cursor.fetchall()
        self.connector.commit()
        if retVal:
            return all_results

class User(DataManager):
    def __init__(self):
        DataManager.__init__(self)
        self.id_user = None
        self.nik = None
        self.password = None
        self.username = None
        self.alamat = None
        self.luas = None
        self.bangun = None
        
    def login(self, nik, password):
        query = 'SELECT id_user, nik, password, username, alamat FROM user_data \
            where nik=\'%s\' and password=\'%s\' '
        query = query % (nik, password)
        data_login = self.executeQuery(query, True)
        konfirm_login = False
        for i in range(0,len(data_login)):
            if nik == data_login[i][1] and password == data_login[i][2]:
                konfirm_login = True
                self.id_user = data_login[i][0]
                self.nik = data_login[i][1]
                self.password = data_login[i][2]
                self.username = data_login[i][3]
                self.alamat = data_login[i][4]
                print("Masuk berhasil")
                print(f"Selamat datang {self.username}")
        if konfirm_login == False:
            print(f"Maaf, NIK atau password salah\n")

    def register(self, nik, password, username, alamat):
        query = 'INSERT INTO user_data (nik, password, username, alamat) \
                VALUES (\'%s\', \'%s\', \'%s\', \'%s\')'
        query = query % (nik, password, username, alamat)
        self.executeQuery(query)
        query = 'SELECT id_user, nik, password, alamat FROM user_data \
            where nik=\'%s\' and password=\'%s\' '
        query = query % (nik, password)
        data_login = self.executeQuery(query, True)
        for i in range(0,len(data_login)):
            if nik == data_login[i][1] and password == data_login[i][2]:
                self.id_user = data_login[i][0]
                self.nik = nik
                self.password = password
                self.username = username
                self.alamat = alamat
                print(f"Selamat datang {self.username}")

    def akun(self):
        print(f"nik: {self.nik}\npassword: {self.password}\nusername: {self.username}\nalamat: {self.alamat}")

class DPO():
    pertahun = 1000000
    def __init__(self, namaDPO, tinggi, berat, kulit, tahuncari):
        self.namaDPO = namaDPO
        self.tinggi = tinggi
        self.berat = berat
        self.kulit = kulit
        self.tahuncari = tahuncari
    def kelibatan(self, kasus):
        print("Nama:" ,self.namaDPO, "\nTinggi badan:" ,self.tinggi, "cm\nBerat badan:" ,self.berat, "kg\nWarna kulit:" ,self.kulit, "\nDicari selama sekitar", self.tahuncari, "tahun")
    def bio(self):
        print("Bio tidak diketahui")
        
class pembunuhan(DPO):
    bounty = 10000000     
    def semua(self):
        return (self.bounty + self.tahuncari*self.pertahun)
    def bio(self):
        print("\nTerkait pada kasus pembunuhan")
        
class narkoba(DPO):
    bounty = 15000000     
    def semua(self):
        return (self.bounty + self.tahuncari*self.pertahun)
    def bio(self):
        print("\nTerkait pada kasus narkoba")

class terorisme(DPO):
    bounty = 20000000
    def semua(self):
        return (self.bounty + self.tahuncari*self.pertahun)
    def bio(self):
        print("\nTerkait pada kasus terorisme")
        
class korupsi(DPO):
    bounty = 15000000     
    def semua(self):
        return (self.bounty + self.tahuncari*self.pertahun)
    def bio(self):
        print("\nTerkait pada kasus korupsi")
        
alfer = pembunuhan("Alfer Raidh", 190, 81, "Sawo", 1)
jumlahalfer = alfer.semua()
amon = narkoba("Amon Marijuana", 188, 75, "Putih", 2)
jumlahamon = amon.semua()
kamad = terorisme("Kamad Lahabian", 221, 165, "Hitam", 5)
jumlahkamad = kamad.semua()
mader = korupsi("Mader Melid Markos", 196, 70, "Putih", 2)
jumlahmader = mader.semua()
sevin = pembunuhan("Sevin Stern", 175, 60, "Putih", 2)
jumlahsevin = sevin.semua()
zackal = korupsi("Zackal Kol", 165, 50, "Sawo", 1)
jumlahzackal = zackal.semua()

u = User()
print("                    /*\ ")
print("                   /***\ ")
print("             <***************>")
print("                 ********* ")
print("                /**  ^  **\ ")
print("               /*         *\ ")
print("\nSelamat Datang pada DPO Satuan Kepolisian K.A.M.I. Silahkan tekan nomor sesuai menu yang diinginkan")

while True:
    print("\n1. Masuk ke akun      2. Membuat akun baru\n3. Periksa DPO        4. Cek akun\n5. Keluar\n")
    menu = input("Menu >").lower()
    
    if menu == '1':
        print("Silahkan input data untuk masuk\n")
        nik = input("Masukkan Nomor Induk Keluarga:")
        password = getpass.getpass ("Masukkan password:")
        u.login(nik,password)
        input("\n\nSilahkan tekan Enter untuk kembali:")
        
    elif menu == '2':
        print("Silahkan input data untuk daftar")
        nik = input("Masukkan Nomor Induk Keluarga:")
        password = input("Buat password untuk akun:")
        username = input("Masukkan nama lengkap:")
        Alamat = input("Masukkan alamat:")
        u.register(nik, password, username, Alamat)
        input("\n\nSilahkan tekan Enter untuk kembali:")

    elif menu == '3':
        if u.username != None:
            print("Masukkan nomor sesuai pada Daftar Pencarian Orang")
            print("1. Alfer Raidh\n2. Amon Marijuana\n3. Kamad Lahabian\n4. Mader Melid Markos\n5. Sevin Stern\n6. Zackal Kol\n")
            cari = input("Masukkan sebuah orang datar atau orang ruang : ")
            if cari == '1':
                alfer.kelibatan("pembunuhan")
                print("Bounty = Rp.", "{:,}".format(jumlahalfer))
                alfer.bio()
            elif cari == '2':
                amon.kelibatan("narkoba")
                print("Bounty = Rp.", "{:,}".format(jumlahamon))
                amon.bio()
            elif cari == '3':
                kamad.kelibatan("terorisme")
                print("Bounty = Rp.", "{:,}".format(jumlahkamad))
                kamad.bio()
            elif cari == '4':
                mader.kelibatan("korupsi")
                print("Bounty = Rp.", "{:,}".format(jumlahmader))
                mader.bio()
            elif cari == '5':
                sevin.kelibatan("pembunuhan")
                print("Bounty = Rp.", "{:,}".format(jumlahsevin))
                sevin.bio()
            elif cari == '6':
                zackal.kelibatan("korupsi")
                print("Bounty = Rp.", "{:,}".format(jumlahzackal))
                zackal.bio()
            else:
                print("Maaf, data yang diinputkan tidak sesuai. Masukkan nomor sesuai orang yang ingin diperiksa.")
        
        else:
            print("Maaf, Anda harus masuk ke akun dahulu")
               
    elif menu == '4':
        print("Akun yang sudah dimasukkan/didaftarkan")
        u.akun()
        input("\n\nSilahkan tekan Enter untuk kembali:")
        
    elif menu == '5':
        print("Terima kasih")
        break
        
    else:
        print("ketik menu untuk melihat daftar menu")