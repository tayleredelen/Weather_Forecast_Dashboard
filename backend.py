import requests

API_KEY = "53b49c4058691d4c05ad801437dd0f70"


def get_data(place, forecast_days=None, weather_type=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    # url gives JSON data by city
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_data(place="Tokyo"))
