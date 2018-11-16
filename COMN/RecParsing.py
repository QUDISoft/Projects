# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def findLinks(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    b = soup.find_all('a', href=True)
    for link in b:
        print(link['href'])



findLinks('https://pikabu.ru') # просто вставляешь любую ссылку и оно ищет все ссылки на этой странице
