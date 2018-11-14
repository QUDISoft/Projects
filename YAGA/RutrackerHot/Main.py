#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Main():  
    '''Логика программы'''
    def dateCounter(self, p):
        """ Структурируемы даты """
        for i in range(p.lenDateElemArray):
            p.preListDateElem.append(p.dateElem[i].getText())
        fa=0
        for i in p.preListDateElem:
            if fa%2==0:
                p.dateElemList.append(p.preListDateElem[fa])
                fa+=1
            else:
                fa+=1
                continue          
        return p.dateElemList[4:]
    
    def textCounter(self, p):
        """ Структурируем названия """
        for i in range(p.lenNameElemArray):
            p.nameElemList.append(p.nameElem[i].getText())
        return p.nameElemList[4:]
    
    def structure(self, p):
        for i in p.nameElemList[4:]:
            p.lenListOfname.append(len(i))
        maxLen=max(p.lenListOfname)
        return maxLen
        
    def spases(self, maxLen, p):
        colspa=[]
        for i in p.nameElemList[4:]:
            colspa.append((maxLen-len(i))*p.dot)
        return colspa
    
    def printAll(self, maxLen, namEl, datEl, colSpa):
        h=1
        for i in namEl:
            if h<10:
                print(' ',h,'. ',i, '...', colSpa[h-1], datEl[h-1], sep='')
                h+=1
            else:
                print(h,'. ',i, '...', colSpa[h-1], datEl[h-1], sep='')
                h+=1                