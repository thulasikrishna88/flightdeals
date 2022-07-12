from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager



data_manager=DataManager()
flight_data =FlightData()
notification_manager=NotificationManager()

sheet_data =data_manager.get_value()
user_data=data_manager.get_user_value()
user_data_list=user_data["users"]


if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()

    for dict in sheet_data:
        dict["iataCode"] = flight_search.get_destination_code(dict["city"])



data_manager.price=sheet_data
# data_manager.update_sheet()

for dict in sheet_data:
    flight_price = flight_data.get_price(dict["iataCode"])
    if flight_price < dict["lowestPrice"]:
        flight_url=f"https://www.google.co.uk/flights?hl=en#flt={flight_data.origin_airport}." \
                   f"{flight_data.destination_airport}.{flight_data.out_date}*{flight_data.destination_airport}." \
                   f"{flight_data.origin_airport}.{flight_data.return_date}"
        if flight_data.stop_overs>1:
            msg=f"Low price alert!only{flight_data.price}to fly from {flight_data.origin_city}-" \
                f"{flight_data.origin_airport} to{flight_data.destination_city}-{flight_data.destination_airport} " \
                f"from {flight_data.out_date} to {flight_data.return_date}" \
                f"Flight has 1 stop over,via {flight_data.via_city}\n{flight_url}"
        else:
            msg=f"Low price alert!only{flight_data.price}to " \
                f"fly from {flight_data.origin_city}-{flight_data.origin_airport} " \
                f"to{flight_data.destination_city}-{flight_data.destination_airport} " \
                f"from {flight_data.out_date} to {flight_data.return_date}\n{flight_url}"
        for user in user_data_list:
            notification_manager.send_email(msg,user["email"])







