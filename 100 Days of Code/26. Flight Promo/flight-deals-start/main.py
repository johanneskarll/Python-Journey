#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from dotenv import load_dotenv
import os
load_dotenv()

MY_EMAIL = os.getenv("MYGMAIL")
MY_PASSWORD = os.getenv("EMAIL50PASS")

dmanager = DataManager()
fsearch = FlightSearch(dmanager.city)
fdata = FlightData(fsearch.resultlist, dmanager.result)

if fdata.searchcheapest():
    notif = NotificationManager(MY_EMAIL, MY_PASSWORD)
    notif.convertmsg(fdata.murmer)
else:
    print("There's no promo-promo")