# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def select(a):
    ''' Короче, чё делает эта функция. Она берет адрес сайта и вырезает из него корень(трохец криво, но работает) 
    Пример:
           https://ub.com.ua/ru/news
           я запас, что все ссылки имеют похожий корень(://корень/) ну и типо спиздил с ченчИксПасАлгоритма основной код.
           только тут я не удалял нужный промежуток, а наооборт добавлял.
           Если ссылка вида https://ub.com.ua (без слэша на конце, то заканчиваем работу с выделением корня тогда, когда закончатся элементы 
           в строке)'''
    mlist=[]
    q = 0
    while q != len(a):
        if a[q] == '/' and a[q-1] == '/':
            q+=1
            while a[q] != '/' and q != len(a)-1:
                mlist.append(a[q])
                q+=1
            else:
                break
        q+=1
            
    my_string = ''.join(mlist)
    return my_string  
    
def findLinks(url, select, exceptions):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    b = soup.find_all('a', href=True)
    ada='http://'  
    f=0 # это пустая переменная. У меня какой-то дики затуп случился и я хз как сделать подругому continue, pass и break не помогают, проблема с OR описана ниже
    for link in b:        #тут проверяем, подходит ли наша ссылка параметрам ada, select и не является ли исключением
        q=link['href']
        if ada and select in q:
            if exceptions[0] in q:
                f+=1
            elif exceptions[1] in q:
                f+=1
            elif exceptions[2] in q:    # вот где я тупой? какого хуя exceptions[0] or exceptions[1]....in q не работает
                f+=1
            elif exceptions[3] in q:
                f+=1            
            else:
                print(q)
            
exceptions='facebook', 'vk.com', 'twitter', 'instagram'
url='https://ub.com.ua/ru'

select=select(url)
findLinks(url, select, exceptions)
