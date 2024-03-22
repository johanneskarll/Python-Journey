##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv




import pandas as pd
import datetime as dt
import smtplib
import random
from dotenv import load_dotenv
import os
load_dotenv()

my_gmail = os.getenv("MYGMAIL")
password = os.getenv("EMAIL50PASS")

randomletter = ["./18. Birthday Wisher (SMTP+DT)/birthday-wisher/letter_templates/letter_1.txt",
                "./18. Birthday Wisher (SMTP+DT)/birthday-wisher/letter_templates/letter_2.txt",
                "./18. Birthday Wisher (SMTP+DT)/birthday-wisher/letter_templates/letter_3.txt"]

now = dt.datetime.now()

listultah = pd.read_csv("./18. Birthday Wisher (SMTP+DT)/birthday-wisher/birthdays.csv")
ludict = listultah.to_dict(orient="records")
for person in ludict:
# 2. Check if today matches a birthday in the birthdays.csv
    if person["day"] == now.day and person["month"] == now.month:
        print("hey its day and month match")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(random.choice(randomletter)) as rdletter:
            text = rdletter.read()
            hasiltext = text.replace("[NAME]",person["name"])
# 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com", 587) as connection: 
                connection.starttls()
                connection.login(user=my_gmail,password=password)
                connection.sendmail(from_addr=my_gmail, to_addrs=person["email"],
                                    msg=f"Subject:Happy Birthday!! {person['name']}\n\n {hasiltext}")


