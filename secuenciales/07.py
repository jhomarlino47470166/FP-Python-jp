#Desarrolle el programa que permite convertir una cantidad dada en metros a su equivalente en centímetros, pulgadas, pies y yardas. Considere los siguientes factores de conversión: 
#1 metro = 100 cm, 1 pie = 12 pulgadas, 1 yarda = 3 pies, 1 pulgada = 2.54 cm

import os
os.system ("cls")

base = int( input ("Base = ") )
altura = int (input ("Altura = ") )

area = base * altura
perimetro = 2 * ( base + altura )

print (f"Area = {area:.2f}")	
print (f"Perimetro = {perimetro:.2f}")