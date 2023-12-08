import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather?q"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Change to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] != "404":
            weather_info = data["main"]
            temperature = weather_info["temp"]
            humidity = weather_info["humidity"]
            description = data["weather"][0]["description"]
            return f'Temperature: {temperature}°C\nHumidity: {humidity}%\nCondition: {description}'
        else:
            return "City not found."

    except Exception as e:
        return f"An error occurred: {str(e)}"

def get_weather_for_city():
    api_key = "74926d93ea6eb0c5d202b0e7d34fad00"  # Replace with your API key
    city = entry.get()
    weather_info = get_weather(api_key, city)
    messagebox.showinfo("Weather Information", weather_info)

# Create the GUI
window = tk.Tk()
window.title("Weather App")

label = tk.Label(window, text="Enter City:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=10)

button = tk.Button(window, text="Get Weather", command=get_weather_for_city)
button.pack(pady=20)

window.mainloop()
