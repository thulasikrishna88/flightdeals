import requests
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()
SHEETY_GETAPI=os.getenv("SHEETY_GETAPI")
SHEETY_PUTAPI=os.getenv("SHEETY_PUTAPI")
SHEETY_USER_API=os.getenv("SHEETY_USER_API")
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.price=None
        self.user_data=None


    def get_value(self):
        sheety_response = requests.get(url=SHEETY_GETAPI)
        data = sheety_response.json()
        self.price = data["prices"]
        return self.price
    def get_user_value(self):
        sheety_user_respone=requests.get(url=SHEETY_USER_API)
        self.user_data=sheety_user_respone.json()
        return self.user_data


    def update_sheet(self):
       for dict in self.price:
            sheet_params= {
                "price":
                    {"iataCode": f"{dict['iataCode']}",
                    }
            }
            sheety_update_response = requests.put(url=f"{SHEETY_PUTAPI}/{dict['id']}", json=sheet_params)


