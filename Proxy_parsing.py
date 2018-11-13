#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from lxml import html

class Proxxy():      
    proxy_url = 'https://www.ip-adress.com/proxy-list'     
    proxy_list = []      

    def __init__(self):       
        r = requests.get(self.proxy_url)      
        strd = html.fromstring(r.content)        
        result = strd.xpath(".//tbody/tr/td/a/text()")
        self.proxy_list = result
        print(result)
        
    def get_proxy(self):
        h=1
        
        for proxy in self.proxy_list:
            url = 'http://' + proxy
            try:
                r = requests.get('https://ub.com.ua/ru', proxies = {'http': url})
                if r.status_code ==200:
                    print(h, url)
                    h+=1
            except requests.exceptions.ConnectionError:
                print(h, url, 'DONT WORK!!!')
                h+=1

proxy=Proxxy()
