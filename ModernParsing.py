#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lxml import html
from lxml.html import html5parser
import requests
# а теперь хуясь, кодировочка установлена
#Тут я тестил, как отличается lxml от bs4. Понял только, что bs4 удобмнее
    
    
proxy_url = 'https://rutracker.org/forum/index.php'     
proxy_list = []      

r = requests.get(proxy_url)      
strd = html.fromstring(r.content)        

result = strd.xpath('''//*[@id="f-756"]/td/h4/a/text()''')
proxy_list = result
print(r)
print(strd)
print(result)