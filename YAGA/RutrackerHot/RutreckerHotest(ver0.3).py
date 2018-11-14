#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Main import Main
from Params import MainParams

url='https://rutracker.org/forum/viewforum.php?f=635'
f=MainParams(url)
g=Main()

def RutreckerHot(g, f):
    '''Это говно ещё улучшать и улучшать'''
    namEl=g.textCounter(f)
    datEl=g.dateCounter(f)
    maxLen=g.structure(f)
    colSpa=g.spases(maxLen, f)
    g.printAll(maxLen, namEl, datEl, colSpa)



RutreckerHot(g, f)
