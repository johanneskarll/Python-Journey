import logging
import pandas as pd
import datetime as dt

logging.basicConfig(level=logging.INFO)

class StockLoader:
    pass
    def __init__(self,file_path):
        self.file_path = file_path
        self.data = None #akan berbentuk data frame
    
    def loaddata(self):
        try:
            self.data = pd.read_csv(self.file_path)
            return self.data
        except FileNotFoundError:
            logging.error(f"File {self.file_path} tidak ditemukan.")
            raise
        except Exception as e:
            logging.error(f"Error saat memuat data: {e}")
            raise

    def get_stock_currency(self, currency):
        # Filter data berdasarkan mata uang
        if self.data is None:
            self.loaddata()
        if self.data[self.data['currency'] == currency].empty: # kalau dicek dari self.data currency tertentu gak ada maka hasilnya dataframe kosong
            raise ValueError(f"Mata uang {currency} tidak didukung.")
        return self.data[self.data['currency'] == currency]
    
    def converter_df_to_dict (self,curstock):
        converteddict = {}
        dictsemula = curstock.to_dict()
        converteddict['symbol'] = list(dictsemula['symbol'].values())[0]
        #ngeiterate supaya ngubah ke bentuk dict yg diinginkan dan diarrange supaya pecahannya dict values yang dibaca urut dari terbesar ke terkecil
        converteddict['values'] = dict(sorted({int(dictsemula['denomination'][denom]): dictsemula['stock'][denom] for denom in dictsemula['denomination']}.items(),key=lambda x: x[0],  reverse=True)) 
        return converteddict

    def update_csv(self, updated_dict, currency):

        if self.data is None:
            self.loaddata()
      
        for denom, stock in updated_dict['values'].items():
            self.data.loc[
                (self.data['currency'] == currency) & 
                (self.data['denomination'] == denom), 'stock'] = stock
        print("ini self data",self.data)
        self.data.to_csv(self.file_path, index=False)
        logging.info(f"CSV file updated for {currency}")


class StockManager:
    def __init__(self,typekurs):
        self.loader = StockLoader("data/stockuang.csv") #"C:/programming/python/portofolio/keisan-project/data/stockuang.csv"
        self.typekurs = typekurs
        self.dict_stock = self.loader.converter_df_to_dict(self.loader.get_stock_currency(typekurs))
        
    def checkemptydenom(self):
        for denom in self.dict_stock['values']:
            if self.dict_stock['values'][denom] <= 0:
                logging.info(f"{self.typekurs} denominator {denom} is empty")

    def infostock(self):
        print(f"Stock change currency {self.typekurs}")
        for denom in self.dict_stock['values']:
            print(f"{self.dict_stock['symbol']}{denom} : {self.dict_stock['values'][denom]}")
        self.checkemptydenom() # tiap kali check apakah ada yang kosong

    def updatestock(self, minuschange):
        # next fitur bisa nambahin duit dari input uang yang masuk
        for denom in minuschange:
            self.dict_stock['values'][denom] -= minuschange[denom]
        self.loader.update_csv(self.dict_stock, self.typekurs)
        self.checkemptydenom() # tiap kali ada perubahan check apakah ada yang kosong
            