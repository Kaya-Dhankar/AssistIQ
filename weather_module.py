import streamlit as st
import requests
from datetime import date

API_KEY = "ee1a1788d06e4817954172744252905"

def show_weather():
    st.title("🌤️ Weather Forecast App")
    st.write("Enter a city name and date to get the weather forecast.")

    city = st.text_input("City Name", placeholder="e.g. London, Mumbai, New York")
    selected_date = st.date_input("Select a Date", min_value=date.today())

    def get_weather(city_name, forecast_date):
        base_url = f"http://api.weatherapi.com/v1/forecast.json"
        params = {
            "key": API_KEY,
            "q": city_name,
            "dt": forecast_date.strftime('%Y-%m-%d'),
            "aqi": "yes"
        }

        try:
            response = requests.get(base_url, params=params)
            if response.status_code != 200:
                return None, f"❌ API Error: {response.status_code}"
            data = response.json()
            return data, None
        except Exception as e:
            return None, f"❌ Exception occurred: {e}"

    if st.button("Get Weather Forecast"):
        if city:
            data, error = get_weather(city, selected_date)
            if error:
                st.error(error)
            elif data and "forecast" in data:
                forecast_day = data["forecast"]["forecastday"][0]["day"]
                st.success(f"Weather on {selected_date} in {data['location']['name']}, {data['location']['country']}")
                st.write(f"🌡️ **Avg Temp:** {forecast_day['avgtemp_c']} °C")
                st.write(f"🌥️ **Condition:** {forecast_day['condition']['text']}")
                st.image(f"http:{forecast_day['condition']['icon']}", width=100)
            else:
                st.warning("No forecast data found for the selected date.")
        else:
            st.warning("Please enter a city name.")
