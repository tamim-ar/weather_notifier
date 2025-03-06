import requests

def get_weather(city):
    """Fetch weather data for a given city."""
    api_key = "e3680a015baa96049c985ab67bcecf50"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data.get("cod") != 200:
            print(f"Error fetching data for {city}: {data.get('message')}")
            return None
        
        weather = {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        return weather
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
