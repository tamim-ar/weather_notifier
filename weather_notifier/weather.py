import urllib.request
import json
from urllib.parse import quote

def get_weather(city):
    api_key = "e3680a015baa96049c985ab67bcecf50"  # Replace with your actual API key
    encoded_city = quote(city)  # URL encode the city name
    url = f"http://api.openweathermap.org/data/2.5/weather?q={encoded_city}&appid={api_key}&units=metric"
    
    try:
        print(f"Making API request to: {url}")  # Debug print
        response = urllib.request.urlopen(url)
        data = json.load(response)
        return data
    except urllib.error.HTTPError as e:
        if e.code == 401:
            print("Error: Unauthorized. Please check your API key.")
        elif e.code == 404:
            print(f"Error: City '{city}' not found.")
        else:
            print(f"Error fetching weather data: HTTP {e.code}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None