
import os
import math

os.system("cls")

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

discriminante = b**2 - 4 * a * c

raiz = math.sqrt(discriminante)  

x1 = (-b + raiz) / (2 * a)
x2 = (-b - raiz) / (2 * a)

print("La primera solución es:", x1)
print("La segunda solución es:", x2)
