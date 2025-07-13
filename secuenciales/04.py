
import os
os.system ("cls")

Pies = float(input("Ingrese la cantidad de pies: "))
Pulgadas = float(input("Ingrese la cantidad de pulgadas: "))

pie_m = 0.3048 
pulgada_m = 0.0254


estatura_metros = Pies * pie_m + Pulgadas * pulgada_m

print(f"La estatura en metros es: {estatura_metros} m")

