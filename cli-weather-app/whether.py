from dotenv import load_dotenv
import os
import requests
# loading environment variable   
load_dotenv()
API_key = os.environ.get("API_Key")
while True:
    city = input("enter your city name(or 'quit' to exit): ")
    if city.lower() == "quit":
        break
    #using the requests library to get the weather data from OpenWeatherMap API
    response = requests.get("https://api.openweathermap.org/data/2.5/weather",
                        params={"q": city, "appid": API_key, "units": "metric", "lang": "en"})
    # Using error handling to check if the city is found or not
    if response.status_code == 200:
        response_j = response.json()
        tem = response_j["main"]["temp"]
        feels_like = response_j["main"]["feels_like"]
        description = response_j["weather"][0]["description"]

        print(f"Temperature: {tem}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Condition: {description}")
    else:
        print("City not found or error occurred.")