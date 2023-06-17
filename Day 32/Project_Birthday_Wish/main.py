import pandas
import random
import smtplib

MY_EMAIL = "abs@gmail.com"

MY_PASSWORD = "abcd1234"


# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
from datetime import datetime

date = (datetime.now().month, datetime.now().day)

birth = pandas.read_csv("birthdays.csv")

birthdays_dict = {(birth_row["month"], birth_row["day"]): birth_row for (index, birth_row) in birth.iterrows()}

if date in birthdays_dict:
    out = birthdays_dict[date]
    n_name = out["name"]
    file_path = f"letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        content = file.read()
        contents = content.replace("[NAME]", n_name)
        with smtplib.SMTP("smtp.gmail.com") as fun:
            fun.starttls()
            fun.login(user=MY_EMAIL, password=MY_PASSWORD )
            fun.sendmail(from_addr=MY_EMAIL, to_addrs=out["email"], msg=f"Subject:Happy Birthday\n\n{contents}")
# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true,
# pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp


# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
