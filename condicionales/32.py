import os
os.system("cls")

categoria = input("Ingrese la categoría del estudiante (A, B, C, D): ").upper()
promedio = float(input("Ingrese promedio ponderado: "))

if categoria == "A":
    pension = 550
elif categoria == "B":
    pension = 500
elif categoria == "C":
    pension = 450
elif categoria == "D":
    pension = 400
else:
    pension = 0

if promedio < 14:
    descuento = 0
elif 14 <= promedio <= 15.99:
    descuento = pension * 0.10
elif 16 <= promedio <= 17.99:
    descuento = pension * 0.12
else:
    descuento = pension * 0.15

nueva_pension = pension - descuento

print(f"Pensión original: S/. {pension:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Nueva pensión: S/. {nueva_pension:.2f}")
