# class 
def otsuriokane (haittaokane,goukei) :
	jumlahkembalian = haittaokane - goukei
	print(f"Kembali {jumlahkembalian}\n")
	
	ichiman = gosen = issen = gohyaku = hyakuen = gojuu = juuen = goen = ichien = 0
	while (jumlahkembalian >= 10000):
		ichiman+=1
		jumlahkembalian -= 10000
	
	
	while (jumlahkembalian >= 5000):
		gosen+=1
		jumlahkembalian -= 5000
	
	
	while (jumlahkembalian >= 1000):
		issen+=1
		jumlahkembalian -= 1000
	
	
	while (jumlahkembalian >= 500):
		gohyaku+=1
		jumlahkembalian -= 500
	
	
	while (jumlahkembalian >= 100):
		hyakuen+=1
		jumlahkembalian -= 100
	
	
	while (jumlahkembalian >= 50):
		gojuu+=1
		jumlahkembalian -= 50
	
	
	while (jumlahkembalian >= 10):
		juuen+=1
		jumlahkembalian -= 10
	
    
	while (jumlahkembalian >= 5):
		goen+=1
		jumlahkembalian -= 5
	
    
	while (jumlahkembalian >= 1):
		ichien+=1
		jumlahkembalian -= 1
	
	
	print("okanenoshurui:")
	print(f"¥ 10.000 x {ichiman}")
	print(f"¥ 5.000 x {gosen}")
	print(f"¥ 1.000 x {issen}")
	print(f"¥ 500 x {gohyaku}")
	print(f"¥ 100 x {hyakuen}")
	print(f"¥ 50 x {gojuu}")
	print(f"¥ 10 x {juuen}")
	print(f"¥ 5 x {goen}")
	print(f"¥ 1 x {ichien}")