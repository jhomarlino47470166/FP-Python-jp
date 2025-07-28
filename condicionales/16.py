import os
os.system("cls")

ingresoMensual = float(input("Ingrese su ingreso mensual: "))
costoCasa = float(input("Ingrese el costo de la casa: "))

if ingresoMensual < 1250:
    numeroCuotas = 120
    cuotaInicial = costoCasa * 0.15
else:
    numeroCuotas = 75
    cuotaInicial = costoCasa * 0.30

cuotaMensual = (costoCasa - cuotaInicial) / numeroCuotas

print(f"Cuota inicial: S/. {cuotaInicial:.2f}")
print(f"Cuota mensual: S/. {cuotaMensual:.2f}")
print(f"Número de cuotas: {numeroCuotas}")
