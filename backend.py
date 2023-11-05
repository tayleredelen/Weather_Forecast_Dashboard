import requests

API_KEY = "53b49c4058691d4c05ad801437dd0f70"


def get_data(place, forecast_days=None, weather_type=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
# url gives JSON data by city
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
# len(filtered_data) = 40 cuz there are values every 3 hours.
# 3 / 24 = 8 and it's for 5 days so 8 * 5 = 40
    num_values = 8 * forecast_days
    filtered_data = filtered_data[:num_values]
# : means from 0 to num_values
    if weather_type == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
# pulls list of all temp data from dict
    if weather_type == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
# pulls list of weather type data dict
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, weather_type="Temperature"))
