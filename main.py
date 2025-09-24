import requests

def get_weather(city):
    api_key = 'b0e2621450cc537669fd785bfb2a7fcc'  # Replace with your OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        city_name = data.get('name')
        country = data.get('sys', {}).get('country')
        temp = data.get('main', {}).get('temp')
        feels_like = data.get('main', {}).get('feels_like')
        weather_desc = data.get('weather', [{}])[0].get('description')

        if city_name and country and temp is not None and feels_like is not None and weather_desc:
            print(f"\n📍 Weather in {city_name}, {country}:")
            print(f"🌡 Temperature: {temp}°C (Feels like {feels_like}°C)")
            print(f"⛅ Condition: {weather_desc.capitalize()}")
        else:
            print("❌ Could not retrieve complete weather data. Please check the city name or API key.")
    except requests.RequestException as e:
        print(f"❌ Network or API error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# -----------------------------
if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
