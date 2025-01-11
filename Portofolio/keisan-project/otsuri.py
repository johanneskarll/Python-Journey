class TransactionManager: 
    def __init__(self,stockdenom,totaltrans,totalpay):
        self.returnmoney = totalpay-totaltrans
        self.currencysymbol = stockdenom['symbol']
        self.stockreal = stockdenom['values']

    def idealcalculate (self,stockreallocal=[],returnmoneylocal=[]) :
        # notes: kenapa dibikin gini, karena siapa tau bakal kepake jika mau parameternya ga default, alias di override dengan data lain
        if not stockreallocal:
            stockreallocal = self.stockreal
        if not returnmoneylocal:
            returnmoneylocal = self.returnmoney

        idealchange = {denom: 0 for denom in stockreallocal}
        remaining = returnmoneylocal

        for denom in stockreallocal:
            while remaining >= denom:
                idealchange[denom] += 1
                remaining -= denom

        return idealchange
    
    def adjust_with_stock (self):
        idealchange = self.idealcalculate()
        sumchange = self.returnmoney #karena tetap ingin menghold informasi uang yg harus dikembalikan diawal
        debttemp = 0
        actual_change = {}

        for denom in self.stockreal:
            if sumchange <= 0:
                break

            if denom in idealchange: # apabila terdapat denom ini pada idealchange (dict)
                needed = idealchange[denom] + debttemp // denom# needed = berapa banyak lembar ideal yang dibutuhkan
                available = self.stockreal[denom] # berapa banyak lembar yang dimiliki

                if (available > needed):
                    to_give = needed
                    debttemp = 0
                else:                  #kekurangan
                    to_give = available
                    debttemp = denom * (needed-available)
                actual_change[denom] = to_give #jumlah yang ada itu
                self.stockreal[denom] -= to_give 
                sumchange -= denom * to_give
            
            if actual_change[denom] <= 0:
                del actual_change[denom]

        if sumchange > 0:
            raise ValueError("Stok tidak cukup untuk memberikan kembalian.")

        return actual_change

    def printreceipt (self):
        print("Your change is: ")
        custreceipt = self.adjust_with_stock()
        for denom in custreceipt:
            print(f"{self.currencysymbol}{denom} : {custreceipt[denom]}")
        