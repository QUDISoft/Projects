from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.onliner.by')

soup = BeautifulSoup(page.text, 'html.parser')
news = soup.findAll('span', class_='text-i')
list1 = []
for q in news:
    list1.append(q.text)
i = 0
while i != len(list1):
    a = soup.find_all('a', class_='b-teasers-2__teaser-i')
    print(list1[i],"  ", a[i].get('href'))
    print("")
    i += 1
