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
                        5:220,
                        10:74,
                        20:32,
                        50:7,
                        100:8}
             },
}

# print(f"{DENOMINATIONS['JPY']['values']}")

class StockManager:
    def __init__(self,typekurs):
        self.typekurs = typekurs
        self.dict_stock = DENOMINATIONS.get(typekurs, [])
        if not self.dict_stock:
            raise ValueError(f"Mata uang {typekurs} tidak didukung.")
        else:
           #diarrange supaya pecahannya dict values yang dibaca urut dari terbesar ke terkecil
           self.dict_stock['values'] = dict(sorted(self.dict_stock['values'].items(), key=lambda x: x[0], reverse=True))

    def infostock(self):
        print(self.dict_stock['values'])
        # print(f"Stock change currency {self.typekurs}")
        # for denom in self.dict_stock['values']:
        #     print(f"{self.dict_stock['symbol']}{denom} : {self.dict_stock['values'][denom]}")

    def updatestock(self, minuschange):
        # next fitur bisa nambahin duit dari input uang yang masuk
        for denom in minuschange:
            self.dict_stock['values'][denom] -= minuschange[denom]