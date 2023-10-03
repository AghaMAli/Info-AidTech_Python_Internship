import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests

# OpenWeatherMap API key
API_KEY = '95f00ca96e2f6b24123fa17b88124225'

# Variables to store weather and forecast data, and a list of favourite locations
weather_data = None
forecast_data = None
favourite_locations = []

# Function to fetch current weather data from OpenWeatherMap API
def fetch_weather_data(location):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print("Error fetching weather data:", str(e))
        return None

# Function to fetch 5-day weather forecast data from OpenWeatherMap API
def fetch_weather_forecast(location):
    try:
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print("Error fetching weather forecast:", str(e))
        return None

# Function to display the current weather data in the GUI
def display_weather_data():
    global weather_data
    if weather_data and 'name' in weather_data and 'sys' in weather_data and 'main' in weather_data and 'weather' in weather_data:
        location_info = f"Weather in {weather_data['name']}, {weather_data['sys']['country']}"
        temperature_info = f"Temperature: {weather_data['main']['temp']}°C"
        humidity_info = f"Humidity: {weather_data['main']['humidity']}%"
        wind_info = f"Wind Speed: {weather_data['wind']['speed']} m/s"
        condition_info = f"Weather Condition: {weather_data['weather'][0]['description']}"
        
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "\n".join([location_info, temperature_info, humidity_info, wind_info, condition_info]))
    else:
        messagebox.showerror("Error", "Error fetching weather data or data structure is incomplete.")

# Function to display the 5-day weather forecast in the GUI
def display_weather_forecast():
    global forecast_data
    if forecast_data and 'list' in forecast_data:
        forecast_list = forecast_data['list']
        if forecast_list:
            forecast_message = "5-Day Weather Forecast:\n"
            for day in forecast_list[:5]:
                temperature = day['main']['temp']
                weather_description = day['weather'][0]['description']
                forecast_message += f"Temperature: {temperature}°C, Weather Condition: {weather_description}\n"
            
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, forecast_message)
        else:
            messagebox.showerror("Error", "No forecast data available.")
    else:
        messagebox.showerror("Error", "Error fetching weather forecast or data structure is incomplete.")

# Function to get and display the current weather data for the entered location
def get_weather():
    global weather_data
    location = location_entry.get()
    weather_data = fetch_weather_data(location)
    display_weather_data()

# Function to get and display the 5-day weather forecast for the entered location
def get_forecast():
    global forecast_data
    location = location_entry.get()
    forecast_data = fetch_weather_forecast(location)
    display_weather_forecast()

# Function to add the entered location to the list of favourite locations
def add_to_favourites():
    global favourite_locations
    location = location_entry.get()
    if location not in favourite_locations:
        favourite_locations.append(location)
        messagebox.showinfo("Info", f"{location} added to favourite cities.")
    else:
        messagebox.showinfo("Info", f"{location} is already in favourite cities")

# Function to view and display the list of favourite locations
def view_favourites():
    global favourite_locations
    if favourite_locations:
        favourites_message = "\n".join(favourite_locations)
        favourites_window = tk.Toplevel(app)
        favourites_window.title("Favourite Locations")
        favourites_label = scrolledtext.ScrolledText(favourites_window, wrap=tk.WORD, width=40, height=10)
        favourites_label.insert(tk.INSERT, favourites_message)
        favourites_label.pack()
    else:
        messagebox.showinfo("Info", "No favourite locations added yet.")

# Creating the main GUI window
app = tk.Tk()
app.title(" IAT Weather App")

# GUI components: Label, Entry, Buttons, and ScrolledText for output
label = tk.Label(app, text="Enter a location along with its country:")
location_entry = tk.Entry(app, width=30)
get_weather_button = tk.Button(app, text="Show current weather", command=get_weather)
get_forecast_button = tk.Button(app, text="Show 5 days forecast", command=get_forecast)
add_to_favourites_button = tk.Button(app, text="Add to favourite cities", command=add_to_favourites)
view_favourites_button = tk.Button(app, text="View favourite cities", command=view_favourites)

# Packing GUI components
label.pack(pady=5)
location_entry.pack(pady=5)
get_weather_button.pack(pady=5)
get_forecast_button.pack(pady=5)
add_to_favourites_button.pack(pady=5)
view_favourites_button.pack(pady=5)

output_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=40, height=10)
output_text.pack()

# Running the main event loop
app.mainloop()