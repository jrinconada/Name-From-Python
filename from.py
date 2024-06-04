import requests
import tkinter as tk
import pycountry

def showInterface():
    global entry
    global window
    window = tk.Tk()
    window.config(width=400, height=400)    
    entry = tk.Entry()
    entry.insert(0, 'Tu nombre...')
    entry.pack(padx=20, pady=10)
    button = tk.Button(text='¿De dónde eres?', command=lambda: nationalizeRequest(entry.get()))
    button.pack(padx=20, pady=10)
    window.mainloop()

def showResults(countries):
    for country in countries:
        label = tk.Label(window, text=country)
        label.pack(padx=20, pady=10)

def nationalizeRequest(name):
    url = "https://api.nationalize.io/?name="

    request = requests.get(url + name)
    countries = jsonParser(request.json())
    showResults(countries)

def jsonParser(json):    
    return [toString(country) for country in json['country']]

def isoCodeToName(code):
    country = pycountry.countries.get(alpha_2=code)
    return country.name

def toString(country):
    return isoCodeToName(country['country_id']) + ' ' + str(round(country['probability'] * 100)) + '%'

showInterface()