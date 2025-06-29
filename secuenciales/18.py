# Se aplica un 15% de descuento dos veces:
# Primero sobre el total de la compra, luego sobre el importe restante.

import os
os.system("cls")

unidades = int(input("Ingrese la cantidad de artículos: "))
precio_unitario = float(input("Ingrese el precio unitario: "))

importe_compra = unidades * precio_unitario
primer_descuento = importe_compra * 0.15
importe_intermedio = importe_compra - primer_descuento
segundo_descuento = importe_intermedio * 0.15
total_descuento = primer_descuento + segundo_descuento
importe_final = importe_compra - total_descuento

print(f"Importe de compra: S/. {importe_compra:.2f}")
print(f"Descuento total: S/. {total_descuento:.2f}")
print(f"Importe a pagar: S/. {importe_final:.2f}")
