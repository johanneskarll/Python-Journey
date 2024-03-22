import smtplib
import requests
from dotenv import load_dotenv
import os
load_dotenv()

MYGMAIL = os.getenv("MYGMAIL")
MYPASS = os.getenv("EMAIL50PASS")
STOCK = "BTC"
COMPANY_NAME = "bitcoin"
ALPHAKEY = os.getenv("ALPHAKEY")
NEWSKEY = os.getenv("NEWSKEY")
listemail = ["johanneskarl50@gmail.com","harleygeraldi@gmail.com","pitbullbon@gmail.com"]
newsparams = {
    "q": COMPANY_NAME,
    "sortBy": "relevancy",
    "apiKey": NEWSKEY
}

alpharesponse = requests.get(f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=IDR&apikey={ALPHAKEY}')
newsresponse = requests.get("https://newsapi.org/v2/everything", params= newsparams)

sisi = alpharesponse.json()
timedaily = [item for item in sisi['Time Series (Digital Currency Daily)'].items()]

yesterdaytuple = timedaily[0]
yesdate = yesterdaytuple[0]
yesclose = float(yesterdaytuple[1]['4b. close (USD)'])
daybeforetuple = timedaily[1]
daydate = daybeforetuple[0]
dayclose = float(daybeforetuple[1]['4b. close (USD)'])

percentage = round((yesclose - dayclose)/ (yesclose / 100), 2) # %
message = ""
subject = ""
if abs(percentage) > 4 :
    if percentage > 0:
        subject += f"{STOCK}: 🔺{percentage} %\n"
    else:
        subject += f"{STOCK}: 🔻{percentage} %\n"
    for i in range(4):
        news = newsresponse.json()["articles"][i]
        message += f"Berita-{i+1}: {news['title']}\n"
        message += f"{news['description']}\n"
        message += f"Baca selengkapnya disini : {news['url']}\n"
        message += "\n"

    subject = subject.encode('utf-8')
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MYGMAIL, password=MYPASS)
            for eachmail in listemail:
                connection.sendmail(
                        from_addr=MYGMAIL,
                        to_addrs=eachmail,  
                        msg=f"Subject:{subject.decode('utf-8')} \n\n{message}".encode('utf-8')
                )

# #NOTE: tadinya pake import datetime trus yesterday = float(timedaily[str(datetime.date.today() - datetime.timedelta(days=1))]["4. close"])
# #tapi keanya better kalo pake list aja
# #kalo semisal tutup bagaimana.