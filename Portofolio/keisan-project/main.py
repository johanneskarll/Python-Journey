from otsuri import TransactionManager
from stock import StockManager


# typekurs = input("Input Currency (JPY/IDR): ").strip().upper()
# totaltrans = float(input("How much is your transaction? "))
# while True:
# 	totalpay = float(input("Input the money "))
# 	if totalpay >= totaltrans:
# 		break
# 	else:
# 		print("Please re-input your money")
		
# calculator = TransactionManager(typekurs,totaltrans,totalpay)
stocker = StockManager("JPY")
calculator = TransactionManager(stocker.dict_stock,5600,10000)

print(f"harus ngembalikan = {calculator.returnmoney}")
print(f"stockreal {calculator.stockreal}")
print(f"idealnya = {calculator.idealcalculate()}")
print(f"adjust_with_stock = {calculator.printreceipt()}")
