# -*- coding: utf-8 -*-
from matplotlib import pylab as pl
#import math as m
from numpy import math as m


def output(x):
    e=m.e
    ex=e**-x
    y=1/(ex+1)
    return y
def nonlin(x,deriv=False):
    e=m.e
    ex=e**-x    
    fx=1/(1+ex)
    if(deriv==True):
        return fx*(1-fx)
    return fx
maxEpoch=5
trainSet=4

def inp(i1, i2, w1, w2):
    inp=i1*w1+i2*w2
    return inp


ideal=1
h1Inp=inp(1,0,0.45,-0.12)
h2Inp=inp(1,0,0.78,0.13)
h1Out=output(h1Inp)
h2Out=output(h2Inp)
O1Inp=inp(h1Out, h2Out, 1.5, -2.3)
O1Out=output(O1Inp)
O2Inp=inp(h1Out, h2Out, 1, 1)
O2Out=output(O2Inp)
Error=((ideal-O1Out)**2+(ideal-O2Out)**2)/2

print(m.sqrt(Error))