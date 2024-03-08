#1--Eps. 50 *args pada fungsi--------------------------------------------------------------
"""
'''
    Contoh kasus:
    def info(datalist):
        data = datalist.copy()
        nama = args[0]
        tinggi = args[1]
        berat = args[2]
        print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    
    info(["dudu",150,50])
'''

def info(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

info("dudu",150,50)

# studi kasus
def tambah (*data):
    output = 0
    for angka in data:
        output += angka
    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(hasil)

#2--Eps. 51 **kwargs pada fungsi--------------------------------------------------------------
def fungsi (nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup",180,78)

def fungsi (**kwargs):
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs ["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama = "ucup", tinggi = 180, berat = 78)

def math(*args,**kwargs):
    penghitung = 0
    if kwargs["option"] == "tambah":
        print("Operasi Penjumlahan")
        for angka in args:
            penghitung += angka
    
    elif kwargs["option"] == "kali":
        print("Operasi Perkalian")
        penghitung = 1
        for angka in args:
            penghitung *= angka
    else:
        print("Tidak ada operasi")
    return penghitung

hasiltambah = math(1,2,3,4,5,6,option ="tambah")
hasilkali = math(1,2,3,4,5,6,option ="kali")

print("hasil tambah",hasiltambah)
print("hasil kali",hasilkali)
"""

# 3--Eps. 52 Anonymous dan Lambda function--------------------------------------------------------------
# Lambda Function
def f_kuadrat(angka):
    return angka**2
print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

# kalo pake lambda
# output = lambda argmuent: expression
kuadrat = lambda angka:angka**2
print(f"hasil lambda kuadrat = {kuadrat(5)}")
#panggil lambda kuadrat dengan input 3 (3 masuk ke angka) dan ekspresinya **2 dan otomatis ngereturn

pangkat = lambda num,pow : num**pow
print(f"hasil lambda pangkat = {pangkat(2,3)}")

## kegunaan
# sorting untuk list
datalist = ["Otong","Ucup","Dudung"]
datalist.sort()
print(datalist)

# sorting pake panjang
def panjangnama (nama):
    return len(nama)
datalist.sort(key=panjangnama)
print(datalist)

# sort pake lambda
datalist = ["Otong","Ucup","Dudung"]
datalist.sort(key = lambda nama:len(nama))
print("sort list pake lambda",datalist)

# filter
dataangka = [1,2,3,4,5,6,7,8,9,10,11,12]
def kurangdari5 (angka):
    return angka < 5
dataangkabaru = list(filter(kurangdari5, dataangka))
dataangkabaru = list(filter(lambda x:x<5,dataangka))
print (dataangkabaru)

datagenap = list(filter(lambda x:(x%2==0),dataangka))
print(datagenap)

# anonymous function (currying)
def pangkat(angka,n):
    hasil = angka**n
    return hasil

print(pangkat(5,2))

# pake currying
# kea gini kuadrat = lambda angka:angka**2
def pangkat (n):
    return lambda angka:angka**n
pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(5)}")

pangkat3 = pangkat(3)
print(f"pangkat 3 = {pangkat3(6)}")
print(f"pangkat bebas = {pangkat(4)(5)}")