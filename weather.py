# pylint: disable=missing-module-docstring

import sys
import urllib.parse
import requests

BASE_URI = "https://weather.lewagon.com"


def search_city(query):
    '''
    Look for a given city. If multiple options are returned, have the user choose between them.
    Return one city (or None)
    '''
    url = "https://weather.lewagon.com/geo/1.0/direct?q=" + query + "&limit=5"
    response = requests.get(url).json()
    if len(response) > 1:
        for i, city in enumerate(response, 1):
            print(f'{i}: {city["name"]}, {city["country"]}')
        idx = int(input("Multiple matches found, which city did you mean?: ")) - 1
        return response[idx]
    elif len(response) == 1:
        return response[0]
    else:
        return None

def weather_forecast(lat, lon):

    url = f"https://weather.lewagon.com/data/2.5/forecast?lat={lat}&lon={lon}"
    response = requests.get(url).json()
    new = response["list"]
    centigrade_symbol = '\u00b0'
    list1 = []
    dict = {}
    for i in range(33):
        if i % 8 == 0:
            list1.append({'weather':f'{new[i]["dt_txt"].split(" ")[0]} {new[i]["weather"][0]["description"]} ({round(float(new[i]["main"]["temp_max"]) - 273.15)}{centigrade_symbol}C)'})
    return list1

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    #need this to return a dict therefore we need to run the length check inside
    forecast = weather_forecast(city['lat'], city['lon'])
    print(forecast)
    for i in forecast:
        for key, value in i.items():
                print(f"{key} {value}")
    return city


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
