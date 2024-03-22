import requests
from datetime import datetime
import smtplib
import time
from dotenv import load_dotenv
import os
load_dotenv()

MY_EMAIL = os.getenv("MYGMAIL")
MY_PASSWORD = os.getenv("EMAIL50PASS")
MY_LAT = -6.147778 # Your latitude
MY_LONG = 106.910721 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LONG-5 <= iss_longitude <=  MY_LONG+5 and MY_LAT-5 <= iss_latitude <=  MY_LAT+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(600)
    if is_iss_overhead and is_night:
        with smtplib.SMPT("smpt.gmail.com",587) as connection:
            connection.startlls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr= MY_EMAIL,
                                to_addrs= MY_EMAIL, 
                                msg="Subject:Look Up\n\nThe ISS is above you in the sky.")



