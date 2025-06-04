#Desarrolle el programa que permite convertir una cantidad dada en metros a su equivalente en centímetros, pulgadas, pies y yardas. Considere los siguientes factores de conversión: 
#1 metro = 100 cm, 1 pie = 12 pulgadas, 1 yarda = 3 pies, 1 pulgada = 2.54 cm

import os
os.system ("cls")

metros = int( input("metros : " ) )

centimetros = metros * 100
pulgadas = centimetros / 2.54
pies = pulgadas / 12
yardas = pies / 3

print (f"centrimetros = {centimetros:.2f}")	
print (f"pulgadas = {pulgadas:.2f}")
print (f"pies = {pies:.2f}")
print (f"yardas = {yardas:.2f}")