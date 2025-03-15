import datetime

input_mahasiswa = {
    'nama' : 'nama',
    'nim' : '00000000',
    'nTugas' : 0,
    'nUTS' : 0,
    'nUAS' : 0,
    'nilai' : 0,
    'predikat' : 'A'
}

data_mahasiswa = {}

print(f"{'SELAMAT DATANG' : ^40}")
print('='*40)
print(f"{'DATA MAHASISWA' : ^10}")

#Membuat dictionary baru dengan key dari dictionary input_mahasiswa
mahasiswa = dict.fromkeys(input_mahasiswa.keys())

#Menambahkan value pada setiap key
mahasiswa['nama'] = input("Nama Mahasiswa : ")
mahasiswa['nim'] = input("NIM Mahasiswa : ")

#Menambahkan input nilai
mahasiswa['nTugas'] = float(input("Masukkan nilai Tugas: "))
mahasiswa['nUTS'] = float(input("Masukkan nilai UTS: "))
mahasiswa['nUAS'] = float(input("Masukkan nilai UAS: "))

# Menghitung nilai akhir 
mahasiswa['nilai'] = (mahasiswa['nTugas'] * 0.4) + (mahasiswa['nUTS'] * 0.3) + (mahasiswa['nUAS'] * 0.3)

# Menentukan predikat berdasarkan nilai akhir
if mahasiswa['nilai'] >= 80:
    mahasiswa['predikat'] = 'A'
elif mahasiswa['nilai'] >= 70:
    mahasiswa['predikat'] = 'B'
elif mahasiswa['nilai'] >= 60:
    mahasiswa['predikat'] = 'C'
elif mahasiswa['nilai'] >= 50:
    mahasiswa['predikat'] = 'D'
else:
    mahasiswa['predikat'] = 'E'

# Menampilkan hasil akhir
print("\nHasil Data Mahasiswa:")
for key, value in mahasiswa.items():
    print(f"{key}: {value}")