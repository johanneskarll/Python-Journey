# Soal UTS 2022 Funda ----------------------------------
'''
# no 1
tinggi = int(input("Masukkan tinggi segitiga : "))
i = 0
while i<tinggi:
    print(tinggi*"*")
    tinggi-=1

# no 2
hpj = 70
hpd = 100
i = 1;
while (hpj > 0) and (hpd > 0):
    print("\nGiliran",i,":")
    print("Karakter Yang Akan Anda Gunakan:")
    print("1. Superman")
    print("2. Batman")
    print("3. The Flash")
    print("4. Wonder Woman")
    pilihan = int(input("Masukkan pilihan anda: "))

    d1 = 10
    d2 = 15

    if pilihan == 1:
        if i%2 == 0:
            hpd-=20
            print("Superman attack! Darkseid got 20 damage")
        else :
            print("Superman blom bisa digunakan")

    if pilihan == 2:
        hpd-=10
        print("Batman attack! Darkseid got 10 damage")

    if pilihan == 3:
        if i%3 == 0:
            hpj+=10
        else:
            print("The flash blom bisa digunakan")

    if pilihan == 4:
        d1 = 5
        d2 = 7.5

    if (i%2 == 0):
        serangan = d2
    else:
        serangan = d1
    print(f"Darkseid attack! Jla got {serangan} damage")
    hpj -= serangan
    print(f"HP JLA = {hpj}, HP Darkseid = {hpd}")
    i+=1

# no 3
## funda
def hitung (datanasabah):
    if datanasabah[0].lower() == "silver":
        sm = 10000000 # sm = saldo minimum
        bunga = 0.01
        ba = 10000 # ba = biaya admin
    elif datanasabah[0].lower() == "gold":
        sm = 50000000
        bunga = 0.02
        ba = 25000
    else :
        print("Data nabasah salah")

dictnasabah = {}
datanasabah = []
print("Selamat datang")
bn=int(input("Ada berapa banyak nasabah? ")) # bn = banyak nasabah
for i in range(bn):
    datanasabah.insert(0,input("Nama nasabah"))
    datanasabah.insert(1,input("Jenis Tabungan:"))
    datanasabah.insert(2,input("Saldo Awal Tabungan: "))

    dictnasabah.update({i:datanasabah})
print(dictnasabah)



## algo
print("~~Selamat Datang~~")
namatamu = input("Masukkan nama tamu: ")
jumlahtamu = int(input("Masukkan jumlah tamu dalam 1 kamar: "))
print("Berikut Tipe Kamar:")
print("1. Single")
print("2. Double")
print("3. Keluarga")
print("4. VIP")
print("5. Vila")
tipekamar = input("Masukkan tipe kamar (1-5): ")
lama = int(input("Masukkan lama menginap: "))
breakfast = int(input("Berapa banyak breakfast? (Masukkan 0 jika tidak ada): "))

# Dictionary untuk tipe kamar
tipekamar_info = {
    1: {"tamumax": 1, "sewapermalam": 300000, "diskon": 50000},
    2: {"tamumax": 2, "sewapermalam": 400000, "diskon": 75000},
    3: {"tamumax": 4, "sewapermalam": 600000, "diskon": 100000},
    4: {"tamumax": 2, "sewapermalam": 600000, "diskon": 150000},
    5: {"tamumax": 4, "sewapermalam": 800000, "diskon": 150000}
}

# Mengecek apakah tipe kamar valid
if int(tipekamar) not in tipekamar_info:
    print("Tipe kamar tidak valid. Silakan masukkan tipe kamar yang benar (1-5).")
else:
    tipekamar = int(tipekamar)
    tamumax = tipekamar_info[tipekamar]["tamumax"]
    sewapermalam = tipekamar_info[tipekamar]["sewapermalam"]
    diskon = tipekamar_info[tipekamar]["diskon"]

    if jumlahtamu > tamumax:
        kelebihan = jumlahtamu - tamumax
        penalti = 100000 * kelebihan

    if lama > 2:
        dm = lama * diskon
    else:
        dm = 0

    total_biaya = (sewapermalam * lama + penalti - dm) * 1.15

    print(f"""
    Nama tamu : {namatamu}
    Lama menginap : {lama} hari
    Jumlah tamu : {jumlahtamu}
    Biaya tambahan : {penalti+dm}
    Diskon : {dm}
    Total biaya : {total_biaya}
    """)
'''

# no 4
n = int(input("Masukan angka "))
# Membuat pola
num = 1
for i in range(n, 0, -1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# no 5
'''
print ("Masukkan Tanggal Lahir Anda.")
Tanggal = int(input("Tanggal: "))
Bulan = int(input("Bulan: "))
Tahun = input("Tahun: ")

bulan = ["switch lives with","married to","handcuffed(for life) to"]
tanggal = ["your best friend","mickey mouse","maria"]
print("Hasil Name Generator:")
print(f"{bulan[Bulan-1]} {tanggal[Tanggal-1]}")
'''


# Soal UTS 2023 Funda ----------------------------------