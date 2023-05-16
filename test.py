import requests
import json

city = "Zaporizhzhia"
api_key = "acf1d8082e6dccbf5b9a72dd3c1f9cf8"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = json.loads(response.text)

print(
    f"The current temperature in {city} is {data['main']['temp']} degrees Celsius.")
