from otsuri import TransactionManager
from stock import StockManager
from copy import deepcopy

def calculate(typekurs, totaltrans,totalpay):
    stocker = StockManager(typekurs)
    stockfromstocker = deepcopy(stocker.dict_stock)
    calculator = TransactionManager(stockfromstocker,totaltrans,totalpay)

    idealchange = calculator.idealcalculate()
    receipt = calculator.adjust_with_stock(idealchange)
    calculator.printreceipt(receipt)

    stocker.updatestock(receipt)
    stocker.infostock()

# typekurs = input("Input Currency (JPY/IDR): ").strip().upper()
# totaltrans = float(input("How much is your transaction? "))
# while True:
# 	totalpay = float(input("Input the money "))
# 	if totalpay >= totaltrans:
# 		break
# 	else:
# 		print("Please re-input your money")
		
calculate("JPY",5875,10500)

