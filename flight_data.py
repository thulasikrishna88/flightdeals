import requests
import os
from pprint import pprint
from dotenv import load_dotenv
from datetime import datetime,timedelta
tomorrow=datetime(year=2022,month=7,day=12)
tomorrow_date=tomorrow.strftime("%d/%m/%Y")
six_month=datetime.now()+timedelta(days=180)
six_month_date=six_month.strftime("%d/%m/%Y")
load_dotenv()
TEQUIULA_URL=os.getenv("TEQUIULA_SEARCH_URL")
TEQUILA_API=os.getenv("TEQUILA_API")
FLY_FROM="LON"


class FlightData:
    def __init__(self):
        self.price = 0
        self.destination_city = " "
        self.origin_city = ""
        self.origin_airport = ""
        self.destination_airport = ""
        self.out_date = ""
        self.return_date = ""
        self.stop_overs=1
        self.via_city =""

    def get_price(self, city_code):
        flight_search_params={
            "fly_from":FLY_FROM,
            "fly_to":city_code,
            "date_from":tomorrow_date,
            "date_to":six_month_date,
            "nights_in_dst_from":7,
            "nights_in_dst_to":28,
            "flight_type":"round",
            "curr":"GBP",
            "max_stopovers":0,

        }
        flight_header={
            "apikey":TEQUILA_API
        }
        flight_data_response=requests.get(url=TEQUIULA_URL,params=flight_search_params,headers=flight_header)
        flight_data = flight_data_response.json()
        try:
            flight_data_first=flight_data["data"][0]
        except IndexError:
            flight_search_params["max_stopovers"]=2
            flight_data_response = requests.get(url=TEQUIULA_URL, params=flight_search_params, headers=flight_header)
            flight_data = flight_data_response.json()
            self.out_date = flight_data["data"][0]["local_departure"].split("T")[0]
            self.return_date = flight_data["data"][0]["route"][2]["local_departure"].split("T")[0]
            self.stop_overs=2
            self.via_city = flight_data["data"][0]["route"]["cityTo"]
        else:
            self.out_date = flight_data["data"][0]["local_departure"].split("T")[0]
            self.return_date = flight_data["data"][0]["route"][1]["local_departure"].split("T")[0]
        finally:
            self.price = flight_data["data"][0]["price"]
            self.destination_city = flight_data["data"][0]["cityTo"]
            self.origin_city = flight_data["data"][0]["cityFrom"]
            self.origin_airport = flight_data["data"][0]["flyFrom"]
            self.destination_airport = flight_data["data"][0]["flyTo"]
            return self.price



