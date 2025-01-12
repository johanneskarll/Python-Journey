from otsuri import TransactionManager
from stock import StockManager
from copy import deepcopy

# typekurs = input("Input Currency (JPY/IDR): ").strip().upper()
# totaltrans = float(input("How much is your transaction? "))
# while True:
# 	totalpay = float(input("Input the money "))
# 	if totalpay >= totaltrans:
# 		break
# 	else:
# 		print("Please re-input your money")
		
stocker = StockManager("JPY")
stockfromstocker = deepcopy(stocker.dict_stock)
calculator = TransactionManager(stockfromstocker,5600,10000)

print(f"(di calculator) stockrealawal {calculator.stockreal}")
print(f"(di stocker) stockrealawal {stocker.infostock()}")
idealchange = calculator.idealcalculate()
receipt = calculator.adjust_with_stock(idealchange)
calculator.printreceipt(receipt)
print(f"(di calculator) stockrealakhir {calculator.stockreal}\n")
print(f"(di stocker) stockrealakhir {stocker.infostock()}\n")
stocker.updatestock(receipt)
print(f"(di stocker) stockrealakhir {stocker.infostock()}\n")


