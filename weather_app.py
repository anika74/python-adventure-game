import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get().strip()
    
    if city == "":
        messagebox.showwarning("warning", "please enter a city name!")
        return
    
    try:
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
        geo_response =requests.get(geo_url).json()
        
        if "results" in geo_response and len(geo_response["results"]) > 0:
            lat =geo_response["results"][0]["latitude"]
            lon = geo_response["results"][0]["longitude"]
            
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            response = requests.get(url)
            data =response.json()
            
            temp = data["current_weather"]["temperature"]
            result_text =f"City: {city.capitalize()}\n temp: {temp}C"
            result_label.config(text=result_text, fg="darkgreen")
        else:
            result_label.config(text="City not found!", fg="red")
            
    except Exception as e:
        print("Error:", e)
        result_label.config(text="Error connecting to internet!", fg="red")
        
root =tk.Tk()
root.title("Live Weather App") 
root.geometry("400x350")

title_label =tk.Label(root, font=("Arial, 12"), width=20, justify="center")
title_label.pack(pady=15)

city_entry = tk.Entry(root, font=("Arial", 12), width=20 , justify="center")
city_entry.pack(pady=10)
city_entry.insert(0, "Dhaka")

search_button = tk.Button(root, text ="search weather", bg="skyblue", fg="black", font=("Arial", 11, "bold"), command=get_weather)
search_button.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=15)

root.mainloop()
               