# Desarrolle el programa que determine de un cilindro:
# Área base = πr², área lateral = 2πrh, área total = 2 x área base + área lateral.
# Siendo r el radio y h la altura.

import os
import math
os.system("cls")

radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

area_base = math.pi * radio**2
area_lateral = 2 * math.pi * radio * altura
area_total = 2 * area_base + area_lateral

print(f"Área base: {area_base:.2f}")
print(f"Área lateral: {area_lateral:.2f}")
print(f"Área total: {area_total:.2f}")
