from weather_notifier.weather_notifier import get_weather

def main():
    city = input("Enter the city name: ")
    weather_data = get_weather(city)
    
    if weather_data:
        print(f"Weather in {weather_data['city']}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Description: {weather_data['description']}")
    else:
        print("Could not retrieve weather data.")

if __name__ == "__main__":
    main()