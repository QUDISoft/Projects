from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen('http://www.nbrb.by/statistics/Rates/RatesDaily.asp')
soup = BeautifulSoup(page, 'html.parser')


def parsing():
    cur_name = soup.findAll("span", class_='text')
    cur_id = soup.findAll("td", class_='curAmount')
    cur_course = soup.findAll('td', class_='curCours')
    lists(cur_name, cur_id, cur_course)


def lists(cur_name, cur_id, cur_course):
    list1 = []
    list2 = []
    list3 = []
    for cur in cur_name:
        list1.append(cur.text)

    for div in cur_id:
        list2.append(div.text)

    for course in cur_course:
        list3.append(course.text)

    num = len(cur_name)
    for i in range(num):
        print(" Название валюты:", list1[i], '\n', "Идентификатор валюты:", list2[i], '\n', "Курс НБРБ:", list3[i], "BYN")
        print()


parsing()
