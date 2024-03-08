#1 - Eps. 53 Global dan Local Scope--------------------------
"""
nama = "otong" # ini variabel global

#akses variabel global dalam fungsi
def fungsi():
    print(f"fungsi menampilkan {nama}")

fungsi()

#akses variabel global dalam loop
for i in range(0,5):
    print(f"loop{i} - {nama}")

#percabangan
if True:
    print(f"if menampilkan {nama}")

## variabel lokal
def fungsi2():
    namalokal = "Ucup" # ini variabel lokal

fungsi2()
#print(namalokal) <- gabisa karena dia lokal

#merubah variabel global
angka = 0

def ubahangka(nilaibaru):
    global angka # fungsi ini mendapat akses merubah angka
    angka = nilaibaru

print(angka)
ubahangka(10)
print(angka)

#2 - Eps. 54 Import Statement--------------------------
from Programprint import tambah as coco
# print(data)
plus = coco(1,2)
print(plus)

#3 - Eps.55 Module --------------------------
# # module matematika dengan import
# import matematika
# hasil_tambah = matematika.tambah(1,2,3,4,5)
# print("hasil tambah =",hasil_tambah)

# hasil_kali = matematika.kali(1,2,3,4,5)
# print("hasil tambah =",hasil_kali)

# pangkat3 = matematika.pangkat(3)
# print(f"hasil pangkat3 = {pangkat3(3)}")

# # module matematika dengan from
# from matematika import tambah,kali
# from matematika import *
# hasil_tambah = tambah(1,2,3,4,5)
# print("hasil tambah =",hasil_tambah)

# hasil_kali = kali(1,2,3,4,5)
# print("hasil tambah =",hasil_kali)

# # pake tambahan as
# from matematika import tambah as add
# from matematika import kali as k
# from matematika import pangkat as bebasaja
# hasil_tambah = add(1,2,3,4,5)
# print("hasil tambah =",hasil_tambah)

# hasil_kali = k(1,2,3,4,5)
# print("hasil tambah =",hasil_kali)


#4 - Eps.56 Membuat package --------------------------
from sains import fisika

hasilplus = fisika.gaya(90,10)
print(hasilplus)

# gaya = f.gaya(90,10)
# print(gaya)

#5 - Eps.57 _Init_.py package --------------------------
# import sains

# hasiltambah = sains.matematika.basic.tambah(1,2,3,4,5)
# print(hasiltambah)

from sains import *

hasiltambah = matematika.basic.tambah(1,2,3,4,5)
print(hasiltambah)

gaya = fisika.gaya(10,9)
print(gaya)


#6 - Eps.58 Standard Library --------------------------
# datetime
import datetime as blabla

datawaktu = blabla.datetime.now()
print(datawaktu)
print(f"tahun : {datawaktu.year}")
print(f"tahun : {datawaktu.strftime('%A')}")

# counter
from collections import Counter
data = ["a", "b", "c", "d", "a","d","e"]
datacount = Counter(data)
print(f"datacount = {datacount}")
print(f"jumlah a = {datacount['a']}")

# io
import io
file = io.open("filetext.txt","r")
print(file.read())
"""
