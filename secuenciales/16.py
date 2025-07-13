
import os
os.system("cls")

horas = float(input("Ingrese el número de horas trabajadas: "))
tarifa = float(input("Ingrese la tarifa por hora: "))

sueldo_basico = horas * tarifa
sueldo_bruto = sueldo_basico * 1.20
sueldo_neto = sueldo_bruto * 0.90

print(f"Sueldo básico: S/. {sueldo_basico:.2f}")
print(f"Sueldo bruto: S/. {sueldo_bruto:.2f}")
print(f"Sueldo neto: S/. {sueldo_neto:.2f}")
