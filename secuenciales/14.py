# Calcule el promedio de los 3 números mayores de 5 números ingresados.
# Usando listas y funciones de la clase math.

import os
import math
os.system("cls")

n1 = float(input("Ingrese el número 1: "))
n2 = float(input("Ingrese el número 2: "))
n3 = float(input("Ingrese el número 3: "))
n4 = float(input("Ingrese el número 4: "))
n5 = float(input("Ingrese el número 5: "))

mayores = [n1, n2, n3, n4, n5]

mayores.sort(reverse=True)

suma = math.fsum([mayores[0], mayores[1], mayores[2]])
promedio = suma / 3

print(f"\nEl promedio de los 3 números mayores es: {promedio:.2f}")
