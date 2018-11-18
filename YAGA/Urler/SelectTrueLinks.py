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
    links = soup.find_all('a', href=True)
    http='http' 
    expns=len(exceptions)
    f=0
    trueLinks=[]
    for link in links:
        httpLink=link['href']
        if http and select in httpLink:
            f=0
            for exception in exceptions:
                if exception in httpLink:
                    break
                else:
                    f+=1
                
            if f==expns:
                trueLinks.append(httpLink)
    return trueLinks
            
#exceptions='facebook', 'vk.com', 'twitter', 'instagram'
#url='https://ub.com.ua/ru'

#select=select(url)
#findLinks(url, select, exceptions)
