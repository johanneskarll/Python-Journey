class Car:
    
    def __init__(self,merk,harga,warna):
        self.merk = merk
        self.harga = harga
        self.warna = warna
        self.__speed = 0

    def nambahkecepatan(self,speed):
        self.__speed += speed

    def infospeed(self):
        return self.__speed

    
