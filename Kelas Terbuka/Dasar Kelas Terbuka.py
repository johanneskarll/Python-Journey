"""a = 10
print (a)

b = 15
print(b)

b = a
print (b)

# tipe data : Angka satuan (integer)
data_integer = 1
print ("data: ",data_integer)
print ("- bertipe: ",type(data_integer))

# tipe data : Angka dengan koma (float)
data_float = 1.5
print ("\ndata: ",data_float)
print ("- bertipe: ",type(data_float))

# tipe data : Kumpulan karakter (string)
data_string = "mie babi"
print ("\ndata: ",data_string)
print ("- bertipe: ",type(data_string))

# tipe data : biner true/false (boolean)
data_bool = True
print ("\ndata: ",data_bool)
print ("- bertipe: ",type(data_bool))

## Tipe data khusus
# bilangan kompleks
data_complex = complex (5,6) #real didepan dan imaginernya dibelakang 
print ("\ndata: ",data_complex)
print ("- bertipe: ",type(data_complex))

# tipe data dari bahasa C (karena py dibuat dengan bahasa C jadi bisa pake tipe data c)
from ctypes import c_double
data_c_double = c_double(10.5)
print ("\ndata: ",data_c_double)
print ("- bertipe: ",type(data_c_double))

#--Eps. 6 Casting Tipe Data-----------------------------------------------------------------------
# merubah dari satu tipe ke tipe lain
# tipe data = int, float, str, bool

data_int = 9
print ("data = ", data_int, ", type =", type (data_int))

data_float = float(data_int)
print ("data = ", data_float, ", type =", type (data_float))

data_str = str(data_int)
print ("data = ", data_str, ", type =", type (data_str))

data_bool = bool(data_int) #klo 0 maka boolean akan jadi false, diluar 0 akan true
print ("data = ", data_bool, ", type =", type (data_bool))

#--Eps. 7 Mengambil input dari user-----------------------------------------------------------------------
#data yang dimasukan pasti str
data = input("Masukkan input: ")

print("data: ", data, "bertipe: ",  type(data))

#jika mau inputnya berupa int
data_int = int(input("Masukkan angka: "))
print("data: ", data_int, "bertipe: ",  type(data_int))

#bagaimana dengan boolean (jadi yang dimasukin hanya 0 dan 1)
biner = bool(int(input("Masukan nilai boolean")))
print("data: ", biner, " bertipe: ",  type(biner))

#--Eps. 8 Operasi Aritmatika-----------------------------------------------------------------------
a = 2
b = 3

# operasi eksponen (pangkat) **
hasil = a ** b
print (a, '**', b, '=', hasil)

# operasi modulus % (sisa)
hasil = a % b
print(a,'%',b,'=',hasil)

# operasi floor division (pembagian bulat (int) )
hasil = a // b
print(a,'//',b,'=',hasil) 

#--Eps. 9 Latian Konversi Temperatur-----------------------------------------------------------------------

# program konversi celcius ke satuan lain

print ("\nProgram Konversi Temperatur\n")
celcius = float(input('Masukan suhu dalam celcius: '))
print ("Suhu adalah ", celcius, " Celcius")

# reamur 4/5 Celcius
reamur = (4/5)*celcius
print ("Suhu dalam reamur adalah ", reamur, " Reamur")

# fahrenheit
fahrenheit = (9/5)*celcius + 32
print ("Suhu dalam fahrenheit adalah ", fahrenheit, " Fahrenheit")

# kelvin
kelvin = celcius + 273
print ("Suhu dalam kelvin adalah ", kelvin, " Kelvin")

# program konversi fahrenheit ke kelvin
print ("\nProgram Konversi Temperatur\n")
fahrenheit = float(input('Masukan suhu dalam fahrenheit: '))
print ("Suhu adalah ", fahrenheit, " Fahrenheit")

celcius = ((5/9)*(fahrenheit-32))
kelvin = celcius + 273
print ("Suhu dalam kelvin adalah ", kelvin, " Kelvin")

# program konversi kelvin ke fahrenheit
print ("\nProgram Konversi Temperatur\n")
kelvin = float(input('Masukan suhu dalam kelvin: '))
print ("Suhu adalah ", kelvin, " Kelvin")

celcius = kelvin-273
fahrenheit = (9/5)*celcius + 32
print ("Suhu dalam fahrenheit adalah ", fahrenheit, " fahrenheit")

#--Eps. 10 Operasi Komparasi-----------------------------------------------------------------------
# setiap hasil dari operasi komparasi adalah boolean (True/False)
# >,<,>=,<=,==,!=,is,is not

a = 4 #a (ada nilainya dan memakan memori) 
b = 2 #4 (adalah literal dan tidak memakan memori)
c = 4.1
hasil = a > b
print (a, '>', b, '=', hasil)
hasil = a > 4
print (a, '>', 4, '=', hasil)
#= disebutnya assignment kalo == membandingkan
hasil = a == c
print (a, "==", c, hasil)

# is = membandingkan memory / object identity
x = 5 # ini adalah assigment membuat object
y = 5
print("nilai x =", x , ' id = ', hex(id(x)))# id x dan y akan sama adressnya akan sama
print("nilai y =",y, ' id = ', hex(id(y)))
hasil = x is y #karena alamatnya sama maka akan true.
print("x is y = ", hasil)
'''

#--Eps. 12 latihan Komparasi dan Logika-----------------------------------------------------------------------
# membuat gabungan area rentang dari angka
#++++++++3---------10++++++++++
inputUser = int(input("masukkan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10 : "))

#+++++++3--------
#memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)

#-------10+++++++
#memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)

#+++++++3----------10+++++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan: ", isCorrect)

#--Eps. 13 Operator Bitwise, operasi biner, binary-----------------------------------------------------------------------

a = 9
b = 5

#bitwise OR (|) kalo di boolean pake "or"
c = a | b
print('\n===============OR===============')
print('nilai :', a,' , binary : ', format(a,'08b'))
print('nilai :', b,' , binary : ', format(b,'08b'))
print('-----------------------------------(|)')
print('nilai :', c,' , binary : ', format(c,'08b'))

#bitwise AND (&) kalo di boolean pake "and" 
c = a & b
print('\n===============AND===============')
print('nilai :', a,' , binary : ', format(a,'08b'))
print('nilai :', b,' , binary : ', format(b,'08b'))
print('-----------------------------------(&)')
print('nilai :', c,' , binary : ', format(c,'08b'))

#bitwise XOR(^)
c = a ^ b
print('\n===============XOR===============')
print('nilai :', a,' , binary : ', format(a,'08b'))
print('nilai :', b,' , binary : ', format(b,'08b'))
print('-----------------------------------(^)')
print('nilai :', c,' , binary : ', format(c,'08b'))

#bitwise NOT(~)
c = ~a
print('\n===============NOT===============')
print('nilai :', a,' , binary : ', format(a,'08b'))
print('-----------------------------------(~)')
print('nilai :', c,' , binary : ', format(c,'08b'))
print('-----------------------------------(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :', e^d,' , binary : ', format(e^d,'08b'))

# shifting

#shift right (>>) kayak cin di c++
c = a >> 1 #angkanya geser
print('\n===============>>===============')
print('nilai :', a,' , binary : ', format(a,'08b'))
print('-----------------------------------(>>)')
print('nilai :', c,' , binary : ', format(c,'08b'))

#shift left (<<) kayak cin di c++
c = a << 1 #angkanya geser
print('\n===============<<===============')
print('nilai :', a,' , binary : ', format(a,'08b'))
print('-----------------------------------(<<)')
print('nilai :', c,' , binary : ', format(c,'08b'))

#--Eps. 14 Operator Assignment-----------------------------------------------------------------------
# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a = 5 # adalah assignment
print("nilai a =", a)

a += 1 # adalah a = a + 1
print("nilai a =", a)

a *= 5
print("nilai a =", a)
#--Eps. 15 Pengenalan String-----------------------------------------------------------------------
'''
    1.bisa menggunakan single quote
    2.bisa menggunakan double quote 
'''

# 2 . menggunakan tanda \

# membuat tanda ' menjadi string
print('"hari ini hari jum\'at"') # ' dianggap menjadi string

# backslash
print("C:\\user\\johan")

#tab
print("ucup\t\t\t\totong, jauhan")

#backspace
print("ucup\botong, deketan")

# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed (unix, macos, linus)
print("baris pertama.\rbaris kedua.") # CR -> carriage return (commodore, acorn, lisp)
print("baris pertama.\r\nbaris kedua.") #CRLF -> line feed carriage return (windows)

# 3. String literal atau raw

# hati-hati
print('C:\new folder') #akan salah pathnya

# menggunakan raw string
print(r'C:\new \t\r\b\\folder')

# multiline literal string
print("""
# Nama : Ucup
# Kelas : 3 SD    
""")

# multiline literal string dan RAW
print(r"""
# Nama : Ucup      
# Kelas : 3\SD
# Website : www.ucup.com/newID            
""")


#--Eps. 16 Operasi dan manipulasi string-----------------------------------------------------------------------
# 1. concate
nama_pertama = "Johannes "
nama_tengah = "Karl "
nama_akhir = "W"

nama_lengkap = nama_pertama + nama_tengah + nama_akhir
print(nama_lengkap)

# 2. panjang string
panjang = len(nama_lengkap) # spasi dihitung
print("panjang = ", panjang)

# 3. operator untuk string

#mengecek apakah ada komponen char di string
d = "d"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + ' =',status)

status = d not in nama_lengkap
print("string " + d + " gak ada di " + nama_lengkap + ' =',status)

# mengulang string
print("wk"*10)
print(45*"-")

# indexing
print("index ke-0 : " + nama_lengkap[0]) # ky array
print("index ke-1 : " + nama_lengkap[1])
print("index ke-(-1) : " + nama_lengkap[-1]) # dari belakang
print("index ke-[0:3]: " + nama_lengkap[0:3]) # 0 sampai 3 (yang terakhir ga diikutin)

# item paling kecil dan besar
print("paling kecil :" + min(nama_lengkap)) #itu adalah spasi
print("paling besar :" + max(nama_lengkap)) #itu adalah spasi

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 115
print("char untuk ASCII 115 adalah " + chr(data))

# 4. operator dalam bentuk method

data = "otong sutorong paraotong"
jumlah = data.count("o") #data adalah objectnya dan count itu adalah objectnya
print("jumlah o pada " + data + " = " + str(jumlah))

#--Eps. 17 Operasi dan manipulasi string (part 2)----------------------------------------------------------------------
# operator dalam bentuk methods

# merubah case dari string 
# merubah ke uppercase
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah ke lowercase
alay = "aKu KeCe AbieeeZzZZZZz"
print("\nnormal = " + alay)
alay = alay.lower()
print("upper = " + alay)

# pengecekan dengan isX method
#contoh pengecekan lower case
salam = "\nsistt"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalpha () <-- untuk mengecek semuanya huruf dan ga kosong
# isalnum () <-- huruf dan angka alpha numeric
# isdecimal () <-- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle () <-- semua kata dimulai dengan huruf besar

judul = "\nIt Is Okay Not To Be Orkay" #kalo salah satunya aja kecil maka returnnya false
apakah_title = judul.istitle()
print(judul + " is title = " + str(apakah_title))

#ngecek kompenen startswith () dan endswith ()
cek_start = "Sanjangnim Oppa".startswith("Sanjangnim") #case-sensitive
print ("start = " + str(cek_start))

cek_end = "Sanjangnim Oppak".endswith("Oppak")
print ("end = " + str(cek_end))

# penggabungan komponen join() dan split ()
pisah = ['aku','sayang', 'kamu']
gabung = ' '.join
print (gabung)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm')) # dia akan menjadi data list lagi kebalikan dari join

# alokasi karakter rjust(), ljust(), center()
print (5*'=' + "data" + "="*5)
kanan = "kanan".rjust(10) #total ada 10 tempelin dikanan ky setw
print("'"+kanan+"'")

kiri = "kiri".ljust(10) #total ada 10 tempelin dikiri ky setw
print("'"+kiri+"'")

tengah= "tengah".center(20,"-") #total ada 10 tempelin ditengah ky setw
print("'"+tengah+"'")

# kebalikannya -> strip() (trim)
tengah = tengah.strip("-")
print("'"+tengah+"'")

kapital = "kapiTal".casefold()
print (kapital)


#--Eps. 18 Format string----------------------------------------------------------------------

#contoh generic
# string
nama = "marlene"
format_str = f"hello {nama}"

print (format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
#format_str = "angka = " + str(angka)
print (format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan ribuan
angka = 20000
format_str = f"ribuan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.2f}"
print (format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:9.3f}"
print (format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_minus:+d}" # buat ngeluarin tandanya (+)

print (format_minus)
print (format_plus)

# memformat persen
persen = 0.45
format_persen = f"persen = {persen:.1%}"# berapa angka blkg titik
print(format_persen)

#format angka lain (binary, octal, hexadecimal)

angka = 225
format_bin = f"bin = {bin(angka)}"
format_oct = f"oct = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print (format_bin)
print (format_oct)
print (format_hex)

#--Eps. 19 String width and Alignment----------------------------------------------------------------------

# Width and Multiline
# Data 
data_nama = "Johannes Karl"
data_umur = 18
data_tinggi = 180.1
data_nomor_sepatu = 47

#string standard
data_string = f"Nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi},\nsepatu = {data_nomor_sepatu}"
print(8*"="+"Data String"+"="*8)
print(data_string)

# mengatur lebar (rjust hanya bisa di string.)
data_string = f'''
nama   = {data_nama.rjust(10)} 
umur   = {data_umur:>13}
tinggi = {data_tinggi:>13}
sepatu = {data_nomor_sepatu:>13}
'''
print(data_string)


#--Eps. 20 Latihan Date and Time----------------------------------------------------------------------
import datetime as dt
# hari_ini = dt.date.today()
# print(hari_ini)
# print(f"Hari ini adalah hari = {hari_ini:%A}")

# tanggal = dt.date(2005,4,6)
# print(tanggal)
# print(f"Hari ini adalah hari = {tanggal:%A}")

print("\nSilahkan masukkan tanggal, \nbulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan  \t:"))
tahun = int(input("Tahun  \t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda = {tanggal_lahir}")
print(f"Anda lahir pada hari = {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari // 365
print(f"Umur anda adalah: {umur_tahun.days} tahun") # untuk ngambil 'daysnya' doang


#--Eps. 20 IF and Else Statement----------------------------------------------------------------------
nama = input("Siapa nama anda? ")

# 1. program if inline
# if (nama=="ucup"): print("kamu ucup yaaa")
# print(f"terima kasih {nama}")

# 2. program if indentation
# kalo program lain pake { } di python pakenya indentasi
if nama=="ucup":
    print("kamu ucup yaa")
print(f"Terima kasih {nama}")

#--Eps. 23 Latihan percabangan - Kalkulator----------------------------------------------------------------------
print(23*"=")
print("Kalkulator aja ni")
print(23*"="+ "\n")

angka_1 = float(input("masukkan angka 1 = "))
operator = input("operator (+,-,*,/) : ")
angka_2 = float(input("masukkan angka 2 = "))

if operator == "+":
    hasil = angka_1 + angka_2
    print (f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print (f"hasilnya adalah {hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print (f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print (f"hasilnya adalah {hasil}")
else:
    print ("operator yang anda masukan salah")

#--Eps. 24 For Loop----------------------------------------------------------------------
# for kondisi:
#     aksi

# angka_list = [0,1,2,3,4]
# print(angka_list)

# for i in angka_list:
#     print(f"i sekarang -> {i}")

# ini dengan range
angka_range = range (5) 
for i in angka_range:
    print(f"i sekarang -> {i}")

print (10*'-')

angka_range = range (1,10)  # 1 - 9
for i in angka_range:
    print(f"i sekarang -> {i}")

print (10*'-')

# menggunakan string
data_str = "saya ganteng abiez"
for huruf in data_str:
    print(huruf)

# ini bisa dilakukan di while bukan di for.
# for (int i=1 ; i<10; i++){
#     i = i + 1
#     print (i)
# }

#--Eps. 25 While Loop----------------------------------------------------------------------
angka = 0
while (angka < 5):
    print("loll")
    angka += 1

#--Eps. 26 Continue and Pass----------------------------------------------------------------------
# pass -> berfungsi sebagai dummy, tidak akan dieksekusi
angka = 0
# while angka < 5:
#     if angka == 3:
#         pass # ini tidak akan dieksekusi
#     angka += 1
#     print (angka)

#continue ->  berfungsi ketika program ketemu dia, bakal balik ke loop lagi
while angka < 5:
    angka +=1
    print (f"Angka skrg -> {angka}")

    if angka == 3:
        print("nice!")
        continue # karena ada continue whassupnya diskip lgnsg balik ke loop lagi 
                 # soalnya kalo di break dia gabakal ngeprint sampe 5 nya.
    print("whassup!")
print("pinish!")
"""
#--Eps. 28 Latihan perulangan----------------------------------------------------------------------
tinggi = int((input("Masukkan tinggi/alas segitiga :")))
# bintang 1
j = 5
for karl in range(tinggi):
    while j>karl:
        print(j*"*")
        j -= 1

print(15*"-")
# bintang 2
j = 0
for i in range (tinggi):
    while j<=i:
        print((j+1)*"*")
        j+=1

print(15*"-")
# bintang 3
j = 0
for i in range (tinggi):
    while j<=i:
        # print(j*" "+tinggi*"*")
        print(j*" ", end ='')
        print(tinggi*"*")
        tinggi -= 1
        j+=1


print(15*"-")
# bintang 4
tinggi = 5
j = 0
for i in range (tinggi):
    while j<=i:
        print((tinggi)*" "+(j+1)*"*")
        tinggi-=1
        j+=1