import requests
import tkinter as tk

root = tk.Tk()

root.title("City Statistics")
root.geometry("500x500")
root.configure(background="white")

city_name_prompt = tk.Label(root,text="Enter your city name: ", font=("Arial", 12))
city_name_prompt.pack(pady=20)

city_name = tk.Entry(width=40)
city_name.pack(pady=20)

def get_weather():

    if not city_name.get().replace(" ", "").isalpha():
        result.config(text="Please enter a valid city name using letters only.")

    else:
        geo_params = {
        "name": city_name.get(), "count": 1
        }

        name = requests.get("https://geocoding-api.open-meteo.com/v1/search", params=geo_params)

        response_name = name.json()


        if "results" not in response_name:
            result.config(text="City not in database.")

        else:
            city = response_name["results"][0]["name"]
            country = response_name["results"][0]["country"]
            lat = str(response_name["results"][0]["latitude"])
            lng = str(response_name["results"][0]["longitude"])


            weather_params = {
                "latitude": lat,
                "longitude": lng,
                "current_weather":True
            }

            weather = requests.get("https://api.open-meteo.com/v1/forecast", params=weather_params)
            response_weather = weather.json()
            temp = str(response_weather["current_weather"]["temperature"])
            weather_unit = response_weather["current_weather_units"]["temperature"]
            result.config(text=f"{city}, a city in {country}. Its geographical location is {lat}, {lng}. The current weather there is {temp}{weather_unit}.")


result = tk.Label(root, text="", wraplength=400, bg="white", font=("Arial", 12))
result.pack(pady=20)

stats_btn = tk.Button(root,text="Get Statistics of City",command=get_weather)
stats_btn.pack(pady=20)

root.mainloop()