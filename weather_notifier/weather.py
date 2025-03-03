import urllib.request
import json
from urllib.parse import quote  # Import quote for URL encoding

def get_weather(city):
    api_key = "e3680a015baa96049c985ab67bcecf50"  # Ensure this is the correct key
    encoded_city = quote(city)  # URL encode the city name
    url = f"http://api.openweathermap.org/data/2.5/weather?q={encoded_city}&appid={api_key}&units=metric"
    
    try:
        print(f"Making API request to: {url}")  # Debug print
        response = urllib.request.urlopen(url)
        data = json.load(response)
        return data
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None
