# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import math


print ("\n---Este programa calcula el factor de friccion de Darcy y las perdidas totales---")

k = float(input("Ingresa Aqui el coeficiente de rugosidad de la tuberia (mm): "))
d = float(input("Ingresa Aqui el diametro de la tuberia (mm): "))
q = float(input("Ingresa Aqui el caudal del agua (m3/s): "))
v = 1.01E-6 #Viscosidad cinematica del agua
l = float(input("Ingresa Aqui la longitud la tuberia (m): "))
pi = math.pi
u = q/(pi*((d/1000)**2)/4)
e = 0.001 #Error adminitido de f
#f = 0

re = (d/1000)*u/v #Numero de Reynolds

if (re<=2000):
    f = 64/re
else:
    f0 = ((-2)*math.log10((k/(3.7*d))+(5.74/(re**0.9))))**(-2)
    b = (-2)*math.log10((2.51/(re*math.sqrt(f0)))+(k/(3.71*d)))
    f = b**(-2)
    auxi= abs(f0-f)/f
    while(auxi > e):
        f0 = f
        b = (-2)*math.log10((2.51/(re*math.sqrt(f0)))+(k/(3.71*d)))
        f = round(b**(-2),5)
        print(f"\nEl factor de friccion es: {f}, con error:{auxi} ")
        auxi= round(abs(f0-f)/f,5)
        
print(f"\n\nEl factor de friccion es: {f}.\nEl error es de : {auxi}")
hr =round((f*8*l*(q**2)/(9.81*(pi**2)*((d/1000)**5))),5)
print(f"Las perdidas por friccion son: {hr} mca")






