from twilio.rest import Client
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
ACCOUNT_SID=os.getenv("ACCOUNT_SID")
AUTH_TOKEN=os.getenv("AUTH_TOKEN")
FROM_NUMBER=os.getenv("FROM_NUMBER")
MY_EMAIL=os.getenv("MY_EMAIL")
PASSWORD=os.getenv("PASSWORD")
MY_NUMBER=os.getenv("MY_NUMBER")


class NotificationManager:

    def send_sms(self,message):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        message = client.messages \
            .create(
                body=message,
                from_=FROM_NUMBER,
                to=MY_NUMBER
        )
        print(message.status)

    def send_email(self,message,email):
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:FlightDeals\n\n{message}"
            )





