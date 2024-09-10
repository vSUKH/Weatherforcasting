''''import time
from tkinter import *
from tkinter import messagebox as mb
import requests
from plyer import notification

# Function to get notification of weather report
def getNotification():
    cityName = place.get()  # getting input of name of the place from user
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"  # base url from where we extract weather report
    apiKey = 'd850f7f52bf19300a9eb4b0aa6b80f0d'  # OpenWeatherMap API key (should be kept secure)
    try:
        # This is the complete url to get weather conditions of a city
        url = baseUrl + "appid=" + apiKey + "&q=" + cityName
        response = requests.get(url)  # requesting for the content of the url
        if response.status_code == 200:
            x = response.json()  # converting it into json
            y = x["main"]  # getting the "main" key from the json object

            # getting the "temp" key of y
            temp = y["temp"]
            temp -= 273.15  # converting temperature from Kelvin to Celsius

            # storing the value of the "pressure" key of y
            pres = y["pressure"]

            # getting the value of the "humidity" key of y
            hum = y["humidity"]

            # storing the value of "weather" key in variable z
            z = x["weather"]

            # getting the corresponding "description"
            weather_desc = z[0]["description"]

            # combining the above values as a string
            info = (
                f"Here is the weather description of {cityName}:\n"
                f"Temperature = {temp:.2f}°C\n"
                f"Atmospheric pressure = {pres} hPa\n"
                f"Humidity = {hum}%\n"
                f"Description of the weather = {weather_desc}"
            )

            # showing the notification
            notification.notify(
                title="YOUR WEATHER REPORT",
                message=info,
                # displaying time
                timeout=10
            )
        else:
            mb.showerror('Error', 'City not found or API request failed')

    except Exception as e:
        mb.showerror('Error', str(e))  # show pop up message if any error occurred

# creating the window
wn = Tk()
wn.title("Weather Desktop Notifier")
wn.geometry('700x200')
wn.config(bg='azure')

# Heading label
Label(wn, text="Weather Desktop Notifier", font=('Courier', 15), fg='grey19', bg='azure').place(x=100, y=15)

# Getting the place name
Label(wn, text='Enter the Location:', font=("Courier", 13), bg='azure').place(relx=0.05, rely=0.3)

place = StringVar(wn)
place_entry = Entry(wn, width=50, textvariable=place)
place_entry.place(relx=0.5, rely=0.3)

# Button to get notification
btn = Button(wn, text='Get Notification', font=7, fg='grey19', command=getNotification).place(relx=0.4, rely=0.75)

# run the window till the closed by user
wn.mainloop()
'''
import time
from tkinter import *
from tkinter import messagebox as mb
import requests
from plyer import notification

# Function to get notification of weather report
def getNotification():
    cityName = place.get()  # getting input of name of the place from user
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"  # base url from where we extract weather report
    apiKey = 'd850f7f52bf19300a9eb4b0aa6b80f0d'  # OpenWeatherMap API key (should be kept secure)
    try:
        # This is the complete url to get weather conditions of a city
        url = baseUrl + "appid=" + apiKey + "&q=" + cityName
        response = requests.get(url)  # requesting for the content of the url
        if response.status_code == 200:
            x = response.json()  # converting it into json
            y = x["main"]  # getting the "main" key from the json object

            # getting the "temp" key of y
            temp = y["temp"]
            temp -= 273.15  # converting temperature from Kelvin to Celsius

            # storing the value of the "pressure" key of y
            pres = y["pressure"]

            # getting the value of the "humidity" key of y
            hum = y["humidity"]

            # storing the value of "weather" key in variable z
            z = x["weather"]

            # getting the corresponding "description"
            weather_desc = z[0]["description"]

            # combining the above values as a string
            info = (
                f"Here is the weather description of {cityName}:\n"
                f"Temperature = {temp:.2f}°C\n"
                f"Atmospheric pressure = {pres} hPa\n"
                f"Humidity = {hum}%\n"
                f"Description of the weather = {weather_desc}"
            )

            # showing the notification
            notification.notify(
                title="YOUR WEATHER REPORT",
                message=info,
                # displaying time
                timeout=10
            )
        else:
            mb.showerror('Error', 'City not found or API request failed')

    except Exception as e:
        mb.showerror('Error', str(e))  # show pop up message if any error occurred

# creating the window
wn = Tk()
wn.title("Weather Desktop Notifier")
wn.geometry('500x300')
wn.config(bg='lightblue')

# Adding a frame for better layout management
frame = Frame(wn, bg='lightblue')
frame.pack(pady=20)

# Heading label
Label(frame, text="Weather Desktop Notifier", font=('Helvetica', 20, 'bold'), fg='darkblue', bg='lightblue').grid(row=0, columnspan=2, pady=10)

# Getting the place name
Label(frame, text='Enter the Location:', font=("Helvetica", 14), bg='lightblue').grid(row=1, column=0, pady=5, padx=10, sticky=E)

place = StringVar(wn)
place_entry = Entry(frame, width=30, textvariable=place, font=('Helvetica', 14))
place_entry.grid(row=1, column=1, pady=5, padx=10, sticky=W)

# Button to get notification
btn = Button(frame, text='Get Notification', font=('Helvetica', 14), bg='green', fg='white', command=getNotification)
btn.grid(row=2, columnspan=2, pady=20)

# run the window till the closed by user
wn.mainloop()
