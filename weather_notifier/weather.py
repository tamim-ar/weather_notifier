import urllib.request
import json

def get_weather(city):
    api_key = "your_api_key_here"  # Replace with your own API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = urllib.request.urlopen(url)
        data = json.load(response)
        return data
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None
