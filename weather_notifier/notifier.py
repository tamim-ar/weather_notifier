def display_weather(data):
    if data:
        city_name = data['name']
        temp = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        print(f"\nWeather in {city_name}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather_description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s\n")
    else:
        print("Could not retrieve weather data.\n")
