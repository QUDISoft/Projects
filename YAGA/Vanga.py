# -*- coding: utf-8 -*-
import time
qleKnut = 0
qleHabr = 0
rq = 0
while rq != 100:
    qe = 0
    leKnut = 0
    leHabr = 0
    while qe != 100:
        a = 3523525**400
        b = 2141245**400
        habr = time.time()
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        g = time.time() - habr
        r = 1
        m = 3523525**400
        n = 2141245**400
        Knut = time.time()
        while r != 0:
            r = m % n
            if r == 0:
                break
            m, n = n, r
        q = time.time() - Knut
        if g > q:
            leKnut += 1
        else:
            leHabr += 1
        qe += 1
    rq += 1
    qleKnut += leKnut
    qleHabr += leHabr

print('Кнут выиграл {0}% испытаний, а Хабр {1}% '.format(qleKnut / rq, qleHabr / rq))
