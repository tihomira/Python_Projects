# smtplib.SMTP("smtp.gmail.com", port=587)
#
# Gmail: smtp.gmail.com
import random
import smtplib
import datetime as dt

MY_EMAIL = "re.mind.me.till.done@gmail.com"
MY_PASSWORD = "m8%u8kI(GU99KOo"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Monday Motivation\n\n{quote}")