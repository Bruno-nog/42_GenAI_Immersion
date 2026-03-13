import requests
import sys

def latitude_longitude(city: str):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    response = requests.get(url)
    data = response.json()

    if "results" not in data:
        print("City not found")
        sys.exit(1)
    
    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]
    name = data["results"][0]["name"]
    country = data["results"][0]["country"]

    return latitude, longitude, name, country

def temperature(lat: float, lon: float):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
    response = requests.get(url)
    data = response.json()

    return data["current"]["temperature_2m"]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("need an argument")
        sys.exit(1)
    city = sys.argv[1]
    lat, lon, name, country = latitude_longitude(city)
    temp = temperature(lat, lon)
    print(f"Current temperature in {name}, {country} is {temp} °C")
    