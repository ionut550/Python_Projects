import time
import smtplib
import requests
from datetime import datetime

MY_LAT = 44.3305
MY_LNG = 26.0744
MY_EMAIL = "example@gmail.com"
PASSWORD = "password"


def iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    data = response.json()

    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    position = (float(latitude), float(longitude))
    return position


def night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
        "date": "today"
    }

    response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = f"{data['results']['sunrise'].split('T')[1].split(':')[0]}:{data['results']['sunrise'].split('T')[1].split(':')[1]}"
    sunset = f"{data['results']['sunset'].split('T')[1].split(':')[0]}:{data['results']['sunrise'].split('T')[1].split(':')[1]}"

    return (sunrise, sunset)


# Check if you can see the I.S.S. and send an email to notify.
while True:
    iss = iss_position()
    current_time = f"{datetime.now().hour}:{datetime.now().minute}"
    night = night_time()

    if (MY_LAT - 5 <= iss[0] <= MY_LAT + 5) and (MY_LNG - 5 <= iss[1] <= MY_LNG + 5) and (
            night[1] < current_time < night[0]):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: Look up in the sky\n\nThe I.S.S. is visible on the night sky"
            )

    time.sleep(60)
