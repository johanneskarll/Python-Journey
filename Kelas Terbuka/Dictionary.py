'''
#1--Eps. 38 Dictionary--------------------------------------------------------------------
# list -> array, mengakses data menggunakan index
datalist =['bubu','dudu','coco']
print(datalist[0])

# dicstionary (dict) -> associative array
# identifier -> key

#bedanya dengan list adalah saat mengakses data
data_dict = {
    'key1':'value1',
    'key2':'value2',
    'list':datalist
}
print(data_dict['key1'])
print(data_dict['list'])

#2--Eps. 39 Operasi Dictionary--------------------------------------------------------------------
#operasi dictionary
data_dict = {
        "bu":"bubu",
        "du":"dudu",
        "co":"coco"
}

#panjang dictionary (berapa banyak keynya)
LENDICT = len(data_dict)
print(f"ada {LENDICT} key di dalam dict")
#mengecek key
key = "bubu"
checkkey = key in data_dict
print(f"apakah {key} ada di datadict? {checkkey}")

#mengakses value (read) dengan get
print(data_dict["du"]) #cuman kan kita gatau nih ini list atau apa
print(data_dict.get("du")) #get menandakan bahwa data_dict itu dictionary bkn list
print(data_dict.get("ba","output yang kita mau kalo gada"))
#meskipun ba gada tapi karena pake get outputnya bukan error tapi None

#mengupdate dan menambah dict
data_dict["du"]="dudu ganteng"
print(data_dict)
data_dict["ba"]="baba"
print(data_dict)

data_dict.update({"du":"dudu"})
print(data_dict)
data_dict.update({"karl":"sikeren"})
print(data_dict)

#mendelete data pada dictionary
del data_dict["karl"]
print(data_dict)

#3--Eps. 40 Looping Dictionary--------------------------------------------------------------------
teman2 = {
    "bu":"bubu ucu",
    "du":"dudidudu",
    "babi":"babi enak",
    "je":"jajajajeje"
}
#kalo bukan dalam bentuk loop

print(15*"="+"ngeluarin key"+"="*15)
keys = teman2.keys()
print(keys)

print(15*"="+"ngeluarin value"+"="*15)
values = teman2.values()
print(values)

print(15*"="+"ngeluarin item (gabungan key & value)"+"="*15)
items = teman2.items()
print(items)

# looping first try (yang keluar adalah keynya)
print(15*"="+"loop ngeluarin key"+"="*15)
for teman in teman2:
    print(teman)

#operator untuk mengambil item/iterables
#versi 1
print(15*"="+"loop ngeluarin value (1)"+"="*4)
for teman in teman2.keys():
    print(teman2.get(teman))

#versi 2
print(15*"="+"loop ngeluarin value (2)"+"="*4)
for teman in teman2.keys():
    print(teman2[teman])

print(15*"="+" loop ngeluarin items "+"="*4)
for item in teman2.items():
    print(item)

print(15*"="+" loop ngeluarin key sm value dari item "+"="*4)
for key,value in teman2.items():
    print(f"key = {key}, value = {value}")

#4--Eps. 41 Copy & Pop Dictionary--------------------------------------------------------------------
pertemanan = {
    "har":"harley g",
    "james":"jeje kntl",
    "remon":"mon pokemon",
    "ray":"ray siapa ya?"
}

friends = pertemanan.copy()
print(f"pertemanan = {pertemanan}\n")
print(f"friends = {friends}\n")

print(20*"-")
pertemanan["har"] = "har geraldi"
print(f"pertemanan = {pertemanan}\n")
print(f"friends = {friends}\n")

# pop dictionary (mentransfer)
dataRemon = friends.pop("remon") 
print(f"data remon = {dataRemon}")
print(f"friends = {friends}\n")

# popitem (paling belakang)
dataterakhir = friends.popitem() 
print(f"data terakhir = {dataterakhir}")
print(f"friends = {friends}\n")


#5--Eps. 42 Multi keys & Nesting Dictionary--------------------------------------------------------------------
import datetime
mahasiswa1 = {
    "Nama" : "Johannes Karl",
    "NIM" : "535230043",
    "SKS_lulus" : 144,
    "Beasiswa" : True,
    "tgllahir" :datetime.datetime(2005,4,6)
}

mahasiswa2 = {
    "Nama" : "James Anderson",
    "NIM" : "535230065",
    "SKS_lulus" : 144,
    "Beasiswa" : False,
    "tgllahir" :datetime.datetime(2004,12,4)
}

mahasiswa3 = {
    "Nama" : "Raymond Euginio",
    "NIM" : "535230044",
    "SKS_lulus" : 144,
    "Beasiswa" : False,
    "tgllahir" :datetime.datetime(2005,9,8)
}

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3
}

print(f"{'KEY':<6} {'NAMA':<17} {'SKS':<3} {'Beasiswa':<8} {'Lahir':<10} ")
print("-"*60)

for key in data_mahasiswa:
    nama = data_mahasiswa[key]['Nama']
    nim = data_mahasiswa[key]['NIM']
    sks = data_mahasiswa[key]['SKS_lulus']
    beasiswa = data_mahasiswa[key]['Beasiswa']
    if (beasiswa == 0):
        status = 'False'
    else:
        status = 'True'
    lahir = data_mahasiswa[key]['tgllahir'].strftime('%x')
    print(f"{key:<6} {nama:<17} {sks:<3} {status:^8} {lahir:<10} ")
'''

#6&7--Eps. 43 Latihan Dictionary--------------------------------------------------------------------
import datetime
import os
import string
import random

# template mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim' : '000000000',
    'skslulus' : 0,
    'lahir':datetime.datetime(1111,1,11)
}
data_mahasiswa = {}

while True:
    os.system("cls")
    print(f"{'~~  SELAMAT DATANG  ~~':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    #membuat dictionary baru menggunakan key, key dari mahasiswa template
    mahasiswa = dict.fromkeys(mahasiswa_template.keys()) 
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    while mahasiswa['nim'] in data_mahasiswa:
         mahasiswa['nim'] = input("Masukkan lagi NIM Mahasiswa yang benar: ")
    mahasiswa['skslulus'] = int(input("SKS Mahasiswa: "))
    tahunlahir = int(input("Tahun lahir (YYYY): "))
    bulanlahir = int(input("Bulan lahir (MM): "))
    tanggallahir = int(input("Tanggal lahir (DD): "))
    mahasiswa['lahir'] = datetime.datetime(tahunlahir,bulanlahir,tanggallahir)
    
    # versi key dengan huruf random
    # bikin key dengan menggunakan random, memilih string dengan kodenya ascii uppercase mau bikin 6 kali
    # key = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    # data_mahasiswa.update({key:mahasiswa})
    # print(f"{'KEY':<6} {'NAMA':<17} {'SKS':<3}   {'Lahir':<10} ")
    # print("-"*40)

    # for key in data_mahasiswa:
    #     nama = data_mahasiswa[key]['nama']
    #     nim = data_mahasiswa[key]['nim']
    #     sks = data_mahasiswa[key]['skslulus']
    #     lahir = data_mahasiswa[key]['lahir'].strftime('%x')
    #     print(f"{key:<6} {nama:<17} {sks:<3}   {lahir:<10} ")

    # print("\n")
    # isdone = input("Sudah beres bro (y/n)? ")

    #versi key dengan nim
    nim = mahasiswa.pop('nim')
    data_mahasiswa.update({nim:mahasiswa})
    print(f"{'NIM':<8} {'NAMA':<17} {'SKS':<3}   {'Lahir':<10} ")
    print("-"*40)

    for nim in data_mahasiswa:
        nama = data_mahasiswa[nim]['nama']
        sks = data_mahasiswa[nim]['skslulus']
        lahir = data_mahasiswa[nim]['lahir'].strftime('%x')
        print(f"{nim:<8} {nama:<17} {sks:<3}   {lahir:<10} ")

    print("\n")
    isdone = input("Sudah beres bro (y/n)? ")
    if isdone == 'y':
        break

print("Akhir dari program, thanks~")
print(data_mahasiswa)
print(data_mahasiswa[nim])
