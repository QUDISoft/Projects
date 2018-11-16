import requests
from bs4 import BeautifulSoup


def findLinks(url):
    substr = url
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    b = soup.find_all('a', href=True)
    global link
    for link in b:
        if link['href'].count(substr) == 0:
            links = substr + link['href']
            print(links)
        else:
            print(link['href'])







findLinks('https://www.youtube.com/') # просто вставляешь любую ссылку и оно ищет все ссылки на этой странице