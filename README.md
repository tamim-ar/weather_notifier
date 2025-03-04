# Weather Notifier CLI

This is a simple Python project that fetches and displays weather data for a given city using the OpenWeatherMap API. The weather information is shown in the terminal.

## Features
- Fetch current weather data for any city
- Display temperature, weather condition, humidity, and wind speed
- Save the last city used in `config.txt`

## Requirements
- Python 3.x
- OpenWeatherMap API Key (free)

## Setup

1. Get your API Key from OpenWeatherMap: [Sign up here](https://openweathermap.org/api)
2. Replace `"your_api_key_here"` in `weather_notifier/weather.py` with your API key.
3. Run the application:
   ```bash
   python main.py

# Contributions
Feel free to fork the repository, report bugs, or add features!


### **How It Works**
1. The program checks `config.txt` for a saved city. If it exists, it uses that city for fetching weather data.
2. If no city is saved, the user is prompted to enter a city.
3. The weather data is fetched from OpenWeatherMap using Python’s built-in `urllib` module.
4. The weather information is displayed in a user-friendly format.

### **Running the Project**
1. Clone or download the project.
2. Install Python (if not already installed).
3. Get an API key from OpenWeatherMap and replace the placeholder in `weather_notifier/weather.py`.
4. Run the application with the following command:
   ```bash
   python main.py
