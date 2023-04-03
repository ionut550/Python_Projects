import requests
from twilio.rest import Client

MY_LAT = 44.3305
MY_LNG = 26.0744
API_KEY = "b8f5ea58ce70a82daf8f8d6a88d7c447"
ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

account_sid = 'Your sid'
auth_token = 'Your token'

parameters={
    "lat":MY_LAT,
    "lon":MY_LNG,
    "appid":API_KEY
}

response = requests.get(url=ENDPOINT,params=parameters)
response.raise_for_status()
data = response.json()["weather"][0]
print(data["main"])
if data["main"] in ("Thunderstorm", "Drizzle", "Rain", "Snow"):
    sms = "Bring an umbrella"
else:
    sms = "Have a nice day!"

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=f"{sms}",
                     from_='Twillio phone number',
                     to='Number you want to send a sms'
                 )

print(message.sid)
print(message.status)