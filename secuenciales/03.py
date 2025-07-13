
import os
os.system ("cls")

kilometro = float(input("Ingrese tramo en km:"))
pies = float(input("Ingrese tramo en pies:"))
millas = float(input("Ingrese tramo en millas:"))

metro = kilometro *1000

pies_m = pies / 3.2808
millas_m = millas * 1609

total = metro + pies_m + millas_m
yardas = total / 0.9144

print(f"La longitud total recorrida en metros es: {total:.2f} m")
print(f"La longitud total recorrida en yardas es: {yardas:.2f} yd")    
