# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import bs4
import requests

def paramss():
    ''' Функция для хранения параметров всей(ну почти) программы '''
    url='https://people.onliner.by/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    news = soup.findAll('div', class_='news-tidings__speech')
    header = soup.select('.news-tidings__subtitle .news-helpers_hide_mobile-small')
    links = soup.select('.news-tidings__link')
    return header, links, news, url


def main(header, links, news, url):
    ''' Открываем сайт онлайнера, парсим блоки последних новостей ( с каждой новости мы берем ссылку и переходим в функцию req() ) '''
    d = 0
    col = len(news)
    while d != col:
        print(header[d].get_text(),'\n\n')
        s=links[d].get('href') # parsing links (without https://people.onliner.by/)
        tempUrl=url[:-1]+s  # make links (https://people.onliner.by/ + link)
        req(tempUrl) 
        d+=1
        
        
def req(tempUrl):
    ''' Парсинг каждой отдельной новости '''
    tempNews = requests.get(tempUrl)
    tempSoup = BeautifulSoup(tempNews.text, 'html.parser')
    text=tempSoup.select('.news-text p')
    a = 0
    s = len(text)
    while a != s-3:
        try:
            f = text[a].get_text()
            print('\n', f)
            a += 1
        except:
            print('\n Error: not a text contetn') # такая хуйня была, что в какой-то из новостей были объекты из инсты. Прога крашилась и наёбываоась. Короче, если что не так, то она теперь непонятную хуйню просто стороной обходить будет.
            break
    print('\n\n\n\n\n')




p=paramss()           #создаем массив из того, что дает нам функция
site=len(p[2])
d=0

while d != site:
    print(p[0][d].get_text(), '\n')   #выводим заголовки и при нажатии enter выводим заголовки и статьи
    d+=1
    
input('press ENTER to more info: ')
print('\n\n\n\n\n')
main(*p)
input('press ENTER to EXIT ')
