import datetime as dt
import random
import pandas
import smtplib

MY_EMAIL = "example@gmail.com"
PASSWORD = "password"
PLACEHOLDER = "[NAME]"

# 1. Check if today matches a birthday in the birthdays.csv
current_date = dt.datetime.now()
list_of_friends = pandas.read_csv("birthdays.csv")
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
sort_by_month = list_of_friends[list_of_friends.month == current_date.month]
birthday = sort_by_month[sort_by_month.day == current_date.day]

# 2. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if not birthday.empty:
    with open(f"letter_templates/{random.choice(letters)}") as data_file:
        data = data_file.read()
        final_letter = data.replace(PLACEHOLDER,birthday.name.item())
# 3. Send the letter generated in step 3 to that person's email address.
    print(final_letter)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday.email.item(),
            msg=f"Subject: Happy birthday {birthday.name.item()}!\n\n{final_letter}"
        )



