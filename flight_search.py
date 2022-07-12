import requests
import os
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()
TEQUILA_API=os.getenv("TEQUILA_API")
TEQUILA_ENDPOINT=os.getenv("TEQUILA_ENDPOINT")


class FlightSearch:
    def get_destination_code(self,cityname):
        flight_params={
            "term":cityname,
            "location_types":"airport",
        }
        headers={"apikey":TEQUILA_API}
        flight_response=requests.get(url=f'{TEQUILA_ENDPOINT}/locations/query', params=flight_params,headers=headers)
        data=flight_response.json()
        code=data['locations'][0]["city"]["code"]
        return code


