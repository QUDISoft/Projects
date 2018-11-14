#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, bs4
class MainParams():
    '''Ну короче типо тут всякие парпметры вроде деревьев элементов, массивов разных и прочей ..., котороую будем заимствовать'''
    def __init__(self, url):
        self.url=url
        self.get_url=requests.get(url)
        self.get_page=bs4.BeautifulSoup(self.get_url.text, "html.parser")
        self.nameElem=self.get_page.select('.hl-tr td.vf-col-t-title.tt .torTopic a')
        self.dateElem=self.get_page.select('.hl-tr td.vf-col-last-post.tCenter.small.nowrap p')
        self.lenNameElemArray=len(self.nameElem)-1
        self.lenDateElemArray=len(self.dateElem)
        self.nameElemList=[]
        self.preListDateElem=[]
        self.dateElemList=[]
        self.lenListOfname=[]
        self.dot='.' 