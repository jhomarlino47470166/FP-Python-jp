import os
os.system("cls")

categoria = input("Ingrese la categoría del trabajador (A, B, C, D): ").upper()
horas = float(input("Ingrese las horas trabajadas: "))

if categoria == "A":
    tarifa = 21.00
elif categoria == "B":
    tarifa = 19.50
elif categoria == "C":
    tarifa = 17.00
elif categoria == "D":
    tarifa = 15.50
else:
    tarifa = 0

sueldo_bruto = horas * tarifa

if sueldo_bruto > 2500 :
    descuento = sueldo_bruto * 0.20 
else :
    descuento = sueldo_bruto * 0.15

sueldo_neto = sueldo_bruto - descuento

print(f"Sueldo bruto: S/. {sueldo_bruto:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Sueldo neto: S/. {sueldo_neto:.2f}")
