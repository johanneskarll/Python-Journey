# import csv
# with open ("wd_for_notes.csv") as file:
#     variabel = csv.reader(file)
#     for row in variabel: print(row)

DENOMINATIONS = {
    'JPY': {'symbol': '¥', 
            'values': {10000: 160,
                       5000: 57,
                       1000: 2,
                       500: 9,
                       100: 66,
                       50: 67,
                       10: 67,
                       5: 7,
                       1: 78}
            },

    'IDR': {'symbol': 'Rp. ',
             'values': {100000:89,
                        50000:89,
                        20000:89,
                        10000:4,
                        5000:86,
                        2000:9,
                        1000:3,
                        500:23,
                        200:62,
                        100:12}
             },

    'USD': {'symbol': '$',
             'values': {0.01:7,
                        0.05:10,
                        0.1:3,
                        0.25:16,
                        1:71,
                        2:12,
                        5:22,
                        10:74,
                        20:32,
                        50:7,
                        100:54}
             },
}

# print(f"{DENOMINATIONS['JPY']['values'][10000]}")

class StockManager:
    def __init__(self,typekurs):
        self.typekurs = typekurs
        self.dict_stock = DENOMINATIONS.get(typekurs, [])
        if not self.dict_stock:
            raise ValueError(f"Mata uang {typekurs} tidak didukung.")

    def infostock(self):
        pass

    def updatestock(self):
        pass