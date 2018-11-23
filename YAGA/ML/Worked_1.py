# -*- coding: utf-8 -*-
import numpy as np
import os
import time
# Сигмоида 
def nonlin(x,deriv=False):
    fx=1/(1+np.exp(-x))
    if(deriv==True):
        return fx*(1-fx)
    return fx

# набор входных данных
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])

# выходные данные
print('Введите 4 числа, которые вы хотите получить в итоге')

y = np.array([[1,1,0,0]]).T


# сделаем случайные числа более определёнными
np.random.seed(1)

# инициализируем веса случайным образом со средним 0
syn0 = 2*np.random.random((3,1)) - 1

for iter in range(100):
    print('Эталон: ')
    print(y)
    
    # прямое распространение
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))
    print(l1)
    # насколько мы ошиблись?
    l1_error = (y - l1)
    # перемножим это с наклоном сигмоиды 
    # на основе значений в l1
    l1_delta = l1_error * nonlin(l1,True) # !!!
    # обновим веса
    syn0 += np.dot(l0.T,l1_delta) # !!!
    for x in range(4):
        if y.all(1)[x]==l1.all(1)[x]:
            ut=iter
            break
    time.sleep(0.2)
    os.system("cls")
print("За {0} итераций мы получили резльтат:".format(ut))
print(l1)
print('C эталоном:')
print(y)
input('Enter to EXIT')
#print(l1)
#print(l0)
#print(l1_error)