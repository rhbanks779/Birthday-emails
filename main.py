import smtplib
import datetime as dt
import pandas
import random

MY_EMAIL = "test@gmail.com"
MY_PASSWORD = "password"
current_date = dt.datetime.now()
today_tuple = (current_date.month, current_date.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# print(birthday_dict)

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    pick = random.randint(1, 3)
    file_path = f"letter_templates/letter_{pick}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday\n\n{contents}")

