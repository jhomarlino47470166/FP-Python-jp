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
