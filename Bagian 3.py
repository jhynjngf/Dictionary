import random
import string

input_mahasiswa = {
    'nama': 'nama',
    'nim': '00000000',
    'nTugas': 0,
    'nUTS': 0,
    'nUAS': 0,
    'nilai': 0,
    'predikat': 'A'
}

data_mahasiswa = {}

while True:
    print(f"{'DATA MAHASISWA' : ^50}")
    print('='*50)
    
    # Membuat dictionary baru dengan key dari dictionary input_mahasiswa
    mahasiswa = dict.fromkeys(input_mahasiswa.keys())
    
    # Input data mahasiswa
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    
    # Input nilai
    mahasiswa['nTugas'] = float(input("Masukkan nilai Tugas: "))
    mahasiswa['nUTS'] = float(input("Masukkan nilai UTS: "))
    mahasiswa['nUAS'] = float(input("Masukkan nilai UAS: "))
    
    # Menghitung nilai akhir
    mahasiswa['nilai'] = (mahasiswa['nTugas'] * 0.4) + (mahasiswa['nUTS'] * 0.3) + (mahasiswa['nUAS'] * 0.3)
    
    # Menentukan predikat
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
    
    # Membuat random key
    KEY = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
    
    # Menambahkan data ke dictionary utama
    data_mahasiswa[KEY] = mahasiswa
    
    # Menampilkan seluruh data mahasiswa yang telah dimasukkan
    print(f"\n{'KEY':<10} {'NAMA':<15} {'NIM':<12} {'NILAI':<7} {'PREDIKAT':<10}")
    print('-'*60)
    for key, data in data_mahasiswa.items():
        print(f"{key:<10} {data['nama']:<15} {data['nim']:<12} {data['nilai']:<7.2f} {data['predikat']:<10}")
    
    print("\n")
    tambah = input("Ingin tambah data (y/n)? ")
    if tambah.lower() == "n":
        break

print("\nAkhir dari program, terima kasih!")
