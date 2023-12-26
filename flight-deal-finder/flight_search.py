from flight_data import FlightData
from dotenv import dotenv_values
import requests

# Load variables from .env file
config = dotenv_values(".env")

# Access TEQUILA_API_KEY variable
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = config.get("TEQUILA_API_KEY") # YOUR TEQUILA API KEY


class FlightSearch:

    def get_destination_code(self, city_name):
        endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {
            'apikey': TEQUILA_API_KEY,
        }
        params = {
            'term': city_name,
            'location_types': 'city',
        }

        response = requests.get(endpoint, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            if data['locations']:
                iata_code = data['locations'][0]['code']
                return iata_code
            else:
                return "No IATA code found for this city."
        else:
            return f"Error: {response.status_code} - {response.text}"


    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 2,
            "curr": "USD"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["cityFrom"],
                origin_airport=data["flyFrom"],
                destination_city=data["cityTo"],
                destination_airport=data["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][-1]["local_departure"].split("T")[0]
            )
            print(f'{flight_data.destination_city} : {flight_data.price}')
            return flight_data

