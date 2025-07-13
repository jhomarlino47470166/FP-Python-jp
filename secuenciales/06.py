
import os
import math
os.system("cls")

radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

area_total = 2 * math.pi * radio * (radio + altura)
volumen = math.pi * radio**2 * altura

print(f"Área total del cilindro: {area_total:.2f}")
print(f"Volumen del cilindro: {volumen:.2f}")
