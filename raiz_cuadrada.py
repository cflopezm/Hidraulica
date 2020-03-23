# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:12:15 2019

@author: Fabian Lopez
"""
import math
print("----Este programa calcula la raiz cuadrada de un numero----")

num = int(input("Introduce un numero aqui: "))

b = num
h = num/b

error = (b-h)/b

#16k = 0
#print(f"k = {k} ,h = {h},  b = {b},  error = {error}")
while(error > 0.000000001):
    b = round(0.5*(h+b),7)
    h = round(num/b,7)
    error = round((b-h)/b,7)
    #k += 1
    #print(f"k = {k} ,h = {h},  b = {b},  error = {error}")
print(f"La raiz cuadrada de {num} = {h}, con error de {error*100}%\n{math.sqrt(num)}")

    