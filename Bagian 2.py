import string
import random

input_mahasiswa = {
    'nama' : 'nama',
}

data_mahasiswa = {}

while True :
    print(f"{'MEMBUAT NAMA DIINPUT BERULANG' : ^50}")

    #Membuat dictionary baru dengan key dari dictionary input_mahasiswa
    mahasiswa = dict.fromkeys(input_mahasiswa.keys())

    #Contoh menambah value pada kkey nama
    mahasiswa['nama'] = input("Nama Mahasiswa : ")

    #Membuat random key
    KEY = ''.join((random.choice(string.ascii_uppercase)for i in range(6)))

    #Menambahkan key dan value pada dictionary 
    data_mahasiswa.update({KEY :mahasiswa})

    #Membuat tampilan header
    print(f"\n{'KEY':<10} {'NAMA':<15}")
    print('-'*25)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]['nama']

        #Menampilkan isi dictionary
        print(f"{KEY:<10} {NAMA:<15}")
    
    print("\n")
    tambah = input("Mau tambah lagi bro (y/n)? ")
    if tambah == "n": #jika tida menambah data maka berhenti
        break
print("\nAkhir dari program, terima kasih")