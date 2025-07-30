import os
os.system("cls")

horas = float(input("Ingrese horas trabajadas: "))
tarifa = float(input("Ingrese pago por hora: "))

if horas <= 48:
    sueldo_bruto = horas * tarifa
else:
    sueldo_bruto = 48 * tarifa + (horas - 48) * tarifa * 1.2

descuento = sueldo_bruto * 0.11 if sueldo_bruto > 1500 else 0
total = sueldo_bruto - descuento

print(f"Horas trabajadas: {horas}")
print(f"Pago por hora: S/. {tarifa:.2f}")
print(f"Sueldo bruto: S/. {sueldo_bruto:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {total:.2f}")
