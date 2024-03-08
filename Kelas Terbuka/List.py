'''
#1--Eps. 29 List--------------------------------------------------------------------
# angka1 = 1
# angka2 = 2
# angka3 = 3

# array itu tidak ada kecuali pake numpy.
# kumpulan data numbers
data_angka = [1,2,3]
print(data_angka)

# kumpulan data string
data_string = ["ucup","otong","odah"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# kumpulan campuran
data_campuran = [1,"bala-bala",2,"cireng","ucup",True]
print(data_campuran)

##cara alternatif membuat list
data_range  = range(0,10,2) # range ( start, stop(brp banyak), step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i != 5] # 5nya diskip
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2== 0] # 5nya diskip
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2== 1] # 5nya diskip
print(list_pake_for_if)

#2--Eps. 30 Manipulasi List--------------------------------------------------------------------

# indexnya  0     1      2
data = ["Ucup","Otong","Dudu"]

# mengambil data dari list ini
data_0 = data[0] # variabel data_0 adalah list 'data' dengan index 0
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir (index -1) = {data_terakhir}")

# mengambil info jumlah data dalam list
panjang = len(data) # ada brp list?
print(panjang)

## manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"\ndata awal  \n{data}")

3#data.insert(posisi, itemnya)
data.insert(2,"Bubu")
print(f"data.insert  \n{data}")

#menambah diakhir data.append
data.append("bababab")
print(f"data.append (nambah diakhir) \n{data}")

# menambah list dengan list
data_baru =["Ujang","Usep","Darrel"]
data.extend(data_baru) #data. sebelum extend digabung dengan data_baru (sementara data_barunya ga berubah)
print(f"data.extend  \n{data}") # yang dipanggil buat print data yang sebelumnya 

# merubah data
# kita ubah data 2 (dari otong menjadi michael)
data[1] = "Michael"
print(f"data[i] rubah otong ke michael = \n{data}")

#meremove data
data.remove("Ujang")
print(f"data.remove \n{data}")

#meremove data paling belakang
data.pop()
print(f"data.pop \n{data}")

data_terakhir = data.pop()
print(f"ngeluarin data terakhir dengan data.pop = {data_terakhir}")


#3--Eps. 31 Operasi List--------------------------------------------------------------------
#Operasi List
#(count)menghitung ada berapa banyak 'anggota' di list
data_angka = [1,3,5,5,6,7,2,8,9,4,5,6,7,8]

jumlah_data5 = data_angka.count(5)
jumlah_data7 = data_angka.count(7)
print(f"Jumlah angka 5 pada data = {jumlah_data5}")
print(f"Jumlah angka 7 pada data = {jumlah_data7}")
print(f"Jumlah list 'anggota' ada = {len(data_angka)}")
#kalo info ada brp banyak anggota total pake len(data_angka)

#(index)ambil posisi data
data_nama = ["Ucup","Bubu","Dudu","Coco","Dudu"]
index_dudu = data_nama.index("Dudu")
print(f"posisi dudu pada list yaitu = {index_dudu}") 
#kalo dudunya berkali kali outputnya hanya Dudu yang pertama.

#mengurutkan list
print(f"data angka sebelum di sort {data_angka}")
data_angka.sort()#ga perlu variabel lgi skrg karena udah ketemu sort dia auto ke urut
print(f"data angka setelah sort {data_angka}")

print(f"data nama sebelum di sort {data_nama}")
data_nama.sort()
print(f"data nama setelah sort {data_nama}")

#membalikkan list
data_angka.reverse()
print(f"data angka setelah di reverse {data_angka}")


#4--Eps. 32 Copy List--------------------------------------------------------------------

a = ["Ucup","Otong","Dudu"]
print(f"a = {a}")

b =  a
print(f"b = {b}")

#kita akan merubah member dari a
a[1] = "Michael" 
# kita ngerubah a b nya juga ikutan
b.sort() # bahkan jika kita merubah b, a nya juga ikutan berubah
# ini terjadi karena adressnya sama.
print(f"a = {a}")
print(f"b = {b}")

#address dari kedua list a dan b (ternyata sama.)
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

print(13*"="+"contoh"+13*'=')

#menduplikat list dengan copy
print("membuat list c dengan a.copy()")
c = a.copy()
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

c[1]="Dadang" #maka tidak akan merubah a dan b karena adressnya berbeda.
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

#5--Eps. 33 Nested List--------------------------------------------------------------------
data_0 = [1,2]
data_1 = [3,4]

data_list_biasa =[1,2,3,4]
print(f"list biasa {data_list_biasa}")

list_2D = [data_0,data_1]
print(f"list 2D {list_2D}")

#contoh pengguna

peserta_0 = ["Ucup", 25,"Laki"]
peserta_1 = ["Otong", 10,"Laki"]
peserta_2 = ["Dedeh", 50,"Wanita"]

list_peserta = [peserta_0,peserta_1,peserta_2]
print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}\n")

# dengan reference

list_copy = list_peserta.copy()#yang kecopy hanya luarnya aja jadi peserta_0nya juga ikut berubah.
print(f"peserta = {list_copy}")
peserta_0[0] = "Michael" #dua duanya jadi keubah
print(f"peserta = {list_copy}")
print(f"peserta = {list_peserta}")


#--Eps. 34 Deep Copy Nested List--------------------------------------------------------------------
data_0 = [1,2]
data_1 = [3,4]

data_2D= [data_0, data_1,10]
data_2D_copy = data_2D.copy()
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

#mengambil data
data = data_2D[0][1]
print(f"data = {data}")

#address semuanya
print(f"address asli = {hex(id(data_2D))}")
print(f"address copy = {hex(id(data_2D_copy))}")

print("address dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_copy[0]))}")

data_2D[0][1] = 5
data_2D[2] = 9
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# kita gunakan deepcopy (untuk mengcopy si nested listnya)
from copy import deepcopy
data_2D= [data_0, data_1,10]
data_2D_deepcopy = deepcopy(data_2D) #mengcopy secara rekursif
print(f"\naddress asli = {hex(id(data_2D))}")
print(f"address deepcopy = {hex(id(data_2D_deepcopy))}")

print("\naddress dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_deepcopy[0]))}") # maka addressnya akan berbeda


#6--Eps. 35 Looping List dan Enumerate--------------------------------------------------------------------

# for loop
print("-"*8+"For Loop"+15*"-")
kumpulan_angka = [4,2,3,5,6,1]
for angka in kumpulan_angka: #si angka(variabel) ini ada di kumpulan_angka
    print(angka)

print ("setelah loop angka menjadi =",angka)

peserta = ["Karl","James","Remon","Dudu","Bubu"]
for nama in peserta:
    print(f"nama = {nama}")

# for loop dan range
# ini style lama pake c++
print("\n"+"-"*8+"For Loop dan Range"+8*"-")
kumpulan_angka = [10,5,4,2,6,5]
panjang = len(kumpulan_angka) 

for i in range(panjang):
    print(f"angka ={kumpulan_angka[i]}")

# while
print("\n"+"-"*8+"While Loop"+8*"-")
i = 0
while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i+=1;

# list comprehension
print("\n"+"-"*8+"List Comprehension"+8*"-")
data = ["Ucup", 1,2,3,"Otong"]
[print(i) for i in data] #print i untuk semua i yang ada di data.

angka = [10,5,4,2,6,5]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)# bikin list baru dari list yang di loop.
# enumerate
# ngambil indexnya dan datanya sekaligus coy
print("\n"+"-"*8+"Enumerate"+8*"-")
data_list = ["Ucup", 1,2,3,"Otong"]
for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")
'''

#7--Eps. 36 Latihan List--------------------------------------------------------------------
# daftar buku ada penulisnya ada judulnya.
list_buku = [] # list kosong
while True:
    print("\n-Masukkan data buku-")
    judul = input("Masukkan judul buku\t: ")
    penulis = input("Masukkan nama penulis\t: ")

    buku_baru =[judul,penulis]
    list_buku.append(buku_baru)

    print("No.| Judul | Penulis")
    for index,buku in enumerate(list_buku):
        print(f"{index}. | {buku[0]} | {buku[1]}")
    
    print("\n\n","="*20)
    isLanjut = input("Apakah dilanjutkan?(y/t)")
    
    if isLanjut == "t":
        break
print("Program Selesai")