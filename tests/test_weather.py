import unittest
from unittest.mock import patch
from weather_notifier.weather_notifier import get_weather  # Adjust if needed

class TestWeatherFetching(unittest.TestCase):
    
    @patch('weather_notifier.weather_notifier.requests.get')
    def test_fetch_weather_success(self, mock_get):
        # Mock API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "main": {"temp": 25},
            "weather": [{"description": "clear sky"}],
            "cod": 200
        }

        result = get_weather("New York")
        self.assertEqual(result["city"], "New York")
        self.assertEqual(result["temperature"], 25)
        self.assertEqual(result["description"], "clear sky")

    @patch('weather_notifier.weather_notifier.requests.get')
    def test_fetch_weather_failure(self, mock_get):
        # Simulate API failure
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {"message": "city not found", "cod": "404"}

        result = get_weather("UnknownCity")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
