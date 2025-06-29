import os
os.system("cls")

Varones = float(input("Ingrese la cantidad de varones:"))
Mujeres = float(input("Ingrese la cantidad de mujeres:"))

Total = Varones + Mujeres

pVarones = Varones / Total * 100
pMujeres = Mujeres / Total * 100

print(f"el porcentaje de varones es: {pVarones:.2f} %")
print(f"el porcentaje de mujeres es: {pMujeres:.2f} %")
