# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests

def findLinks(url):
    try:
        soup = BeautifulSoup(site.content, 'html.parser')
        b=soup.find_all('a', href=True)
        for link in b:
            print(link['href'])
    except:
        print('Error: very difficult site, try another one')


findLinks('https://rutracker.org/forum/index.php') # просто вставляешь любую ссылку и оно ищет все ссылки на этой странице
