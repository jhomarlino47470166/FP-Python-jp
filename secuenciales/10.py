# Dado un número natural de 4 cifras, desarrolle el programa que permite obtener el número al revés.
# Ejemplo: 1234 → 4321

import os
os.system("cls")

numero = input("Ingresar un numero de 4 cifras: ")

invertido = numero [::-1]

print(f"El número invertido es: {invertido}")




