import os
os.system("cls")

monto_vendido = float(input("Ingrese monto vendido: "))

sueldo_bruto = 600 + monto_vendido * 0.15
descuento = sueldo_bruto * 0.10 if sueldo_bruto > 1800 else sueldo_bruto * 0.05
sueldo_neto = sueldo_bruto - descuento
polos = 3 if monto_vendido > 1000 else 1

print(f"Sueldo bruto: S/. {sueldo_bruto:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Sueldo neto: S/. {sueldo_neto:.2f}")
print(f"Número de polos obsequiados: {polos}")
