import sqlite3
import os


def create_table():
	conn = sqlite3.connect('testdb.sqlite')

	cursor = conn.cursor()

	query = '''
	    CREATE TABLE IF NOT EXISTS dpo(
	    	id INTEGER PRIMARY KEY, 
	    	roll INTEGER, 
	    	nama TEXT,
	        tinggi INTEGER,
            berat INTEGER,
            wrnkulit TEXT,
            kasus TEXT,
            bounty INTEGER
	    )
	'''

	cursor.execute(query)

	conn.commit()
	conn.close()


def add_dpo(roll,nama,tinggi,berat,wrnkulit,kasus,bounty):
	conn = sqlite3.connect('testdb.sqlite')

	cursor = conn.cursor()

	query = '''
	    INSERT INTO dpo( roll, nama, tinggi, berat, wrnkulit, kasus, bounty )
	    	        VALUES ( ?,?,?,?,?,?,? )
	'''

	cursor.execute(query,(roll,nama,tinggi,berat,wrnkulit,kasus,bounty))

	conn.commit()
	conn.close()



def get_dpo():
	conn = sqlite3.connect('testdb.sqlite')

	cursor = conn.cursor()

	query = '''
	    SELECT roll, nama, tinggi, berat, wrnkulit, kasus, bounty
	    FROM dpo
	'''

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

def get_dpo_by_roll(roll):
	conn = sqlite3.connect('testdb.sqlite')

	cursor = conn.cursor()

	query = '''
	    SELECT roll, nama, tinggi, berat, wrnkulit, kasus, bounty
	    FROM dpo
	    WHERE roll = {}
	''' .format(roll)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

def update_dpo(roll,nama,tinggi,berat,wrnkulit,kasus,bounty):
	conn = sqlite3.connect('testdb.sqlite')

	cursor = conn.cursor()

	query = '''
	    UPDATE dpo
	    SET nama = ?, tinggi = ?, berat = ?, wrnkulit = ?, kasus = ?, bounty = ?
	    WHERE roll = ?
	'''

	cursor.execute(query,(nama,tinggi,berat,wrnkulit,kasus,bounty,roll))

	conn.commit()
	conn.close()


def delete_dpo(roll):
	conn = sqlite3.connect('testdb.sqlite')

	cursor = conn.cursor()

	query = '''
	    DELETE
	    FROM dpo
	    WHERE roll = {}
	''' .format(roll)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows


create_table()


def add_data(id_,nama,tinggi,berat,wrnkulit,kasus,bounty):
	add_dpo(id_,nama,tinggi,berat,wrnkulit,kasus,bounty)
def get_data():
	return get_dpo()

def show_data():
	print("Data 1 ID, data 2 nama lengkap, data 3 tinggi badan (cm), data 4 berat badan (kg), data 5 warna kulit, data 6 kasus terkait, data 7 nilai bounty (Rp)\n")
	dpo = get_data()
	for dpo in dpo:
		print(dpo)

def show_data_by_id(id_):
	dpo = get_dpo_by_roll(id_)
	if not dpo:
		print("Maaf, tidak ditemukan data dengan nomor id",id_)
	else:
		print("Data 1 ID, data 2 nama lengkap, data 3 tinggi badan (cm), data 4 berat badan (kg), data 5 warna kulit, data 6 kasus terkait, data 7 nilai bounty (Rp)\n")
		print (dpo)

def select():
	os.system('cls||clear')
	print("                    /*\ ")
	print("                   /***\ ")
	print("             <***************>")
	print("                 ********* ")
	print("                /**  ^  **\ ")
	print("               /*         *\ ")
	sel = input("\nSelamat Datang pada DPO Satuan Kepolisian K.A.M.I. Silahkan tekan nomor sesuai menu yang diinginkan* \n*(Untuk menjaga keamanan, password diperlukan untuk menu 3, 4, dan 5)\n1. Tampilkan Data    2. Pencarian Data\n3. Tambahkan Data    4. Ubah Data\n5. Hapus Data        6. Keluar\n")

	
	if sel=='1':
		os.system('cls||clear')
		show_data()
		input("\n\nSilahkan tekan Enter untuk kembali:")
	elif sel=='2':
		os.system('cls||clear')
		id__ = int(input('Masukkan Id: '))
		show_data_by_id(id__)
		input("\n\nSilahkan tekan Enter untuk kembali:")
	elif sel=='3':
		os.system('cls||clear')
		password = input('Masukkan password: ')
		if password == '1234':
			os.system('cls||clear')
			id_ = int(input('Masukkan Id (data angka): '))
			nama = input('Masukkan nama lengkap: ')
			tinggi = int(input('Masukkan tinggi badan (cm): '))
			berat = int(input('Masukkan berat badan (kg): '))
			wrnkulit = input('Masukkan warna kulit: ')
			kasus = input('Masukkan kasus terkait: ')
			bounty = int(input('Masukkan nilai bounty (Rp): '))
			add_data(id_,nama,tinggi,berat,wrnkulit,kasus,bounty)
			input("\n\nData berhasil ditambahkan. Silahkan tekan Enter untuk kembali:")
		else:
			os.system('cls||clear')
			input("\n\nMaaf, password salah. Silahkan tekan Enter untuk kembali:")
	elif sel=='4':
		os.system('cls||clear')
		password = input('Masukkan password: ')
		if password == '1234':
			os.system('cls||clear')
			id__ = int(input('Masukkan Id: '))
			show_data_by_id(id__)
			print()
			nama = input('Masukkan nama lengkap: ')
			tinggi = input('Masukkan tinggi badan (cm): ')
			berat = input('Masukkan berat badan (kg): ')
			wrnkulit = input('Masukkan warna kulit: ')
			kasus = input('Masukkan kasus terkait: ')
			bounty = input('Masukkan nilai bounty (Rp): ')
			update_dpo(id__,nama,tinggi,berat,wrnkulit,kasus,bounty)
			input("\n\nData terkait berhasil diubah \nSilahkan tekan Enter untuk kembali:")
		else:
			input("\n\nMaaf, password salah. Silahkan tekan Enter untuk kembali:")
	elif sel=='5':
		os.system('cls||clear')
		password = input('Masukkan password: ')
		if password == '1234':
			os.system('cls||clear')
			id__ = int(input('Masukkan Id: '))
			show_data_by_id(id__)
			delete_dpo(id__)
			input("\n\nData terkait berhasil dihapus \nSilahkan tekan Enter untuk kembali:")
		else:
			input("\n\nMaaf, password salah. Silahkan tekan Enter untuk kembali:")
	else:
		return 0;
	return 1;

while(select()):
	pass