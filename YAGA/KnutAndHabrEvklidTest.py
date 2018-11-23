# -*- coding: utf-8 -*-
import time

qe = 0
leKnut = 0
leHabr = 0
while qe != 100:
    r = 1
    m = 30723843592912 ** 241
    n = 50723843313912 ** 241
    Knut=time.time()
    while n!=0 and m!=0:
        if n>m:
            n=n%m
        else:
            m=m%n
    q = time.time() - Knut
    a = 30723843592912 ** 241
    b = 50723843313912 ** 241
    habr = time.time()
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    g = time.time() - habr
    if g > q:
        leKnut += 1
    else:
        leHabr += 1
    qe += 1

print(g)
print(q)
print('Кнут выиграл {0}% испытаний, а Хабр {1}% '.format(leKnut, leHabr))
