
from bs4 import BeautifulSoup
import requests
from datetime import date


def main():

    first = 'https://sinoptik.com.ru/погода-'
    city_name = str(input("Введите названия города для получения информации о погоде: "))
    url = first+city_name
    souping(url)


def souping(url):
    weather=requests.get(url)
    soap_weather = BeautifulSoup(weather.text, 'html.parser')
    parsing(soap_weather)


def parsing(soap_weather):
    name = soap_weather.find("span").text
    name.strip()
    date1 = date.today()
    date2 = date1.strftime('%m.%d.%Y')
    weather_n1 = soap_weather.select('.temperature .p1')
    weather_night1 = weather_n1[0].get_text()
    weather_n2 = soap_weather.select('.temperature .p2')
    weather_night2 = weather_n2[0].get_text()
    w_mor1 = soap_weather.select('.temperature .p3')
    w_mor2 = soap_weather.select('.temperature .p4')
    weather_morning1 = w_mor1[0].get_text()
    weather_morning2 = w_mor2[0].get_text()
    w_day1 = soap_weather.select('.temperature .p5')
    w_day2 = soap_weather.select('.temperature .p6')
    weather_day1 = w_day1[0].get_text()
    weather_day2 = w_day2[0].get_text()
    w_ev1 = soap_weather.select('.temperature .p7')
    w_ev2 = soap_weather.select('.temperature .p8')
    weather_evening1 = w_ev1[0].get_text()
    weather_evening2 = w_ev2[0].get_text()
    description = soap_weather.find('div', class_="description").text

    printing(weather_evening2, weather_evening1, weather_day2, weather_day1,
             weather_morning2, weather_morning1, weather_night2, weather_night1, name, date2, description)


def printing(weather_evening2, weather_evening1, weather_day2, weather_day1,
             weather_morning2, weather_morning1, weather_night2, weather_night1, name, date2, description):
    print("")
    print("Погода", name, "по состоянию на ", date2, ':', sep="")
    print("")
    print("Погода ночью: от", weather_night1, "до",  weather_night2)
    print("Погода утром: от", weather_morning1, "до",  weather_morning2)
    print("Погода днём: от", weather_day1, "до",  weather_day2)
    print("Погода вечером: от", weather_evening1, "до",  weather_evening2)
    print("")
    print(description, sep="")


main()
