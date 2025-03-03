from weather_notifier.weather import get_weather
from weather_notifier.notifier import display_weather

def load_city():
    try:
        with open('config.txt', 'r') as file:
            city = file.read().strip()
            if city:
                return city
    except FileNotFoundError:
        return None

def save_city(city):
    with open('config.txt', 'w') as file:
        file.write(city)

def main():
    city = load_city()
    
    if city:
        print(f"Using saved city: {city}")
    else:
        city = input("Enter the city name: ")
        save_city(city)
    
    weather_data = get_weather(city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
