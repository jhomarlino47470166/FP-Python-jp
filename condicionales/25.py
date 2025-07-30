import os
os.system("cls")

sueldo_bruto = float(input("Ingrese sueldo bruto: "))
hijos = int(input("Ingrese número de hijos: "))

if hijos > 1:
    bonificacion = sueldo_bruto * 0.125 + (40 * hijos)
else:
    bonificacion = sueldo_bruto * 0.10

sueldo_neto = sueldo_bruto + bonificacion

print(f"Bonificación: S/. {bonificacion:.2f}")
print(f"Sueldo neto: S/. {sueldo_neto:.2f}")
