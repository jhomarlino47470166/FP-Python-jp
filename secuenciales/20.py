# Dado un monto en soles, descomponer en billetes de 200, 100, 50, 20, 10
# y monedas de 5, 2 y 1 sol.

import os
os.system("cls")

monto = int(input("Ingrese la cantidad de dinero en soles: "))

b200 = monto // 200
monto %= 200

b100 = monto // 100
monto %= 100

b50 = monto // 50
monto %= 50

b20 = monto // 20
monto %= 20

b10 = monto // 10
monto %= 10

m5 = monto // 5
monto %= 5

m2 = monto // 2
monto %= 2

m1 = monto

print("Descomposición:")
print(f"Billetes de 200: {b200}")
print(f"Billetes de 100: {b100}")
print(f"Billetes de 50: {b50}")
print(f"Billetes de 20: {b20}")
print(f"Billetes de 10: {b10}")
print(f"Monedas de 5: {m5}")
print(f"Monedas de 2: {m2}")
print(f"Monedas de 1: {m1}")
