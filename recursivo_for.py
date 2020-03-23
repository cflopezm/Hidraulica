# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:00:30 2019

@author: Fabian Lopez
"""

print("---Este programa calcula el factorial de un numero y la posicion del numero de fibonacci---")

num = int(input("Escribe un numero: "))

print("\nFactorial")
fact = 1
for i in range(num):
    #print(i+1)
    fact *= i+1
    
print(f"El factorial de {num} -> {num}! = {fact}")
print("\nFibonacci")

fibo = [0,1]
for k in range(num):
    if(k>1):
        fibo.append(fibo[k-1]+fibo[k-2])
print(f"El numero de la serie de fibonacci en la posicion {num} es -> {fibo[-1]}")
        

