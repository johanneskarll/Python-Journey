lator = TransactionManager(stockfromstocker,1568,2500)

idealchange = calculator.idealcalculate()
print(idealchange)
receipt = calculator.adjust_with_stock(idealchange)
calculator.printreceipt(receipt)
