import os
os.system("cls")

ingresoMensual = int(input("Ingreso su ingreso mensual mensual: "))
costoCasa = int(input("Ingrese el costo de la casa: "))


if ingresoMensual < 1250:
    numeroCuotas = 120
    cuotaInicial = costoCasa * 0.15
    cuotaMensual = (costoCasa - cuotaInicial) / numeroCuotas
else: 
    numeroCuotas = 75
    cuotaInicial = costoCasa * 0.30
    cuotaMensual = (costoCasa - cuotaInicial) / numeroCuotas
    
print(f"Cuota inicial: {cuotaInicial:.2f}")
print(f"Cuota mensual: {cuotaMensual:.2f}")
print(f"Número de cuotas: {numeroCuotas}")

