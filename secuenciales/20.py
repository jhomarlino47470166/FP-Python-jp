import os
os.system("cls")

monto = int(input("Ingrese la cantidad de dinero en soles: "))

billetes200 = monto // 200
monto = monto % 200  # Lo que sobra

billetes100 = monto // 100
monto = monto % 100

billetes50 = monto // 50
monto = monto % 50

billetes20 = monto // 20
monto = monto % 20

billetes10 = monto // 10
monto = monto % 10

monedas5 = monto // 5
monto = monto % 5

monedas2 = monto // 2
monto = monto % 2

monedas1 = monto  # Lo que queda son monedas de 1 sol

print("\nDescomposición del monto en billetes y monedas:")
print(f"Billetes de 200: {billetes200}")
print(f"Billetes de 100: {billetes100}")
print(f"Billetes de 50: {billetes50}")
print(f"Billetes de 20: {billetes20}")
print(f"Billetes de 10: {billetes10}")
print(f"Monedas de 5: {monedas5}")
print(f"Monedas de 2: {monedas2}")
print(f"Monedas de 1: {monedas1}")
