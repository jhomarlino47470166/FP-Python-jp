# Una donación anual se reparte así:
# 25% centro de salud, 35% comedor infantil, 25% escuela infantil, el resto al asilo.

import os
os.system("cls")

donacion = float(input("Ingrese el monto total de la donación: "))

centro_salud = donacion * 0.25
comedor = donacion * 0.35
escuela = donacion * 0.25
asilo = donacion - (centro_salud + comedor + escuela)

print(f"Centro de salud: S/. {centro_salud:.2f}")
print(f"Comedor infantil: S/. {comedor:.2f}")
print(f"Escuela infantil: S/. {escuela:.2f}")
print(f"Asilo de ancianos: S/. {asilo:.2f}")
