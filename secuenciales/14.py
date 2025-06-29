# Calcule el promedio de los 3 números mayores de 5 números ingresados.
# Usando listas y funciones de la clase math.

import os
os.system("cls")

numeros = []
for i in range(5):
    n = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(n)

numeros.sort(reverse=True)  # ordenamos de mayor a menor
promedio = sum(numeros[:3]) / 3

print(f"El promedio de los 3 números mayores es: {promedio:.2f}")
