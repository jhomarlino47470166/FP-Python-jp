# Desarrolle el programa que lea un número entero de 4 cifras y determine la suma de sus cifras.
# Asumir que el número es positivo y tiene exactamente 4 cifras.

import os
os.system("cls")

numero = int(input("Ingrese un número de 4 cifras: "))

d1 = numero // 1000
d2 = (numero // 100) % 10
d3 = (numero // 10) % 10
d4 = numero % 10

suma = d1 + d2 + d3 + d4

print(f"La suma de las cifras es: {suma}")
