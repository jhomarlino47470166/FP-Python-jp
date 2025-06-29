# Desarrolle el programa que permita calcular el resultado de la ecuación de segundo grado 
# de la forma ax² + bx + c. Usando la fórmula general y la clase math.

import os
import math
os.system("cls")

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

discriminante = b**2 - 4 * a * c

if discriminante < 0:
    print("La ecuación no tiene soluciones reales.")
else:
    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x2 = (-b - math.sqrt(discriminante)) / (2 * a)
    print(f"Las soluciones son: x1 = {x1:.2f}, x2 = {x2:.2f}")
