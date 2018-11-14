# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from datetime import date
import sys
url = 'https://sinoptik.com.ru/погода-минск'
weather = requests.get(url)
soap_weather = BeautifulSoup(weather.text, 'html.parser')
def adad():
    way = '.temperature .p'   # создаем то, что у нас всегда одинаковое будет
    x=1   # теперь инкремент, который меняется
    degrees=[]  # сюда будем закидывать все результаты
    while x != 9:      # делаем до девяти, так как нам надо 8 говн
        f=way, str(x)     # тут финт, где мы делаем список из той одинаковой части и инкрементирующегося X, который мы делаем не цифрой и строкой
        s=''.join(f)       # галимо соединяем список в одну переменную (в первой итерации например .temperature .p1 получится)                      
        r=soap_weather.select(s) # weather_n1 = soap_weather.select('.temperature .p1')
        q=r[0].get_text() # weather_night1 = weather_n1[0].get_text()
        degrees.append(q) # добавляем полученые градус в массив и продолжаем заниматься всей этой хуйней до конца цикла
        x+=1
    return degrees # будем возвращать массив в какую-нибудь переменную (в этом случае D)

def qqqq(a1,a2,a3,a4,a5,a6,a7,a8,):  #пример того, что всё работает
    print('Погода ночью: ', a1, a2)
    print('Погода утром: ', a3, a4)
    print('Погода днем: ', a5, a6)
    print('Погода вечером: ', a7, a8)
D=adad()
qqqq(*D)


