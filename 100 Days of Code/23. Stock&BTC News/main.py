import smtplib
import requests
from dotenv import load_dotenv
import os
load_dotenv()

MYGMAIL = os.getenv("MYGMAIL")
MYPASS = os.getenv("EMAIL50PASS")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAKEY = os.getenv("ALPHAKEY")
NEWSKEY = os.getenv("NEWSKEY")
listemail = ["johanneskarl50@gmail.com","harleygeraldi@gmail.com","pitbullbon@gmail.com"]
alphaparams = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAKEY
}
newsparams = {
    "q": COMPANY_NAME,
    "sortBy": "relevancy",
    "apiKey": NEWSKEY
}

alpharesponse = requests.get("https://www.alphavantage.co/query?", params= alphaparams)
newsresponse = requests.get("https://newsapi.org/v2/everything", params= newsparams)

timedaily = alpharesponse.json()['Time Series (Daily)']
timedailylist = [value for(key,value) in timedaily.items()]
yesterday = timedailylist[0]["4. close"]
beforeyesterday = timedailylist[1]["4. close"]
percentage = round((yesterday - beforeyesterday)/ (yesterday / 100), 2) # %

message = ""
subject = ""
if percentage >= 5 or percentage <= -5:
    if percentage > 0:
        subject += f"TSLA: 🔺{percentage}%\n"
    else:
        subject += f"TSLA: 🔻{percentage}%\n"
    for i in range(3):
        news = newsresponse.json()["articles"][i]
        message += f"Headline: {news['title']}"
        message += "Brief: {news['description']}"
        message += "\n"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MYGMAIL, password=MYPASS)
        for eachmail in listemail:
            connection.sendmail(
                    from_addr=MYGMAIL,
                    to_addrs=eachmail,
                    msg=f"Subject:{subject} \n\n{message}"
            )

#NOTE: tadinya pake import datetime trus yesterday = float(timedaily[str(datetime.date.today() - datetime.timedelta(days=1))]["4. close"])
#tapi keanya better kalo pake list aja
#kalo semisal tutup bagaimana.