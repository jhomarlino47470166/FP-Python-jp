# Desarrolle el programa que permita calcular el resultado de la ecuación de segundo grado 
# de la forma ax² + bx + c. Usando la fórmula general y la clase math.

import os
os.system("cls")

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

d = b**2 - 4 * a * c

x1 = (-b + d**0.5) / (2*a)
x2 = (-b - d**0.5) / (2*a)

print(f"x1 = {x1:.2f}")
print(f"x2 = {x2:.2f}")
