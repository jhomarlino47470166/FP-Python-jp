'''Una empresa paga a sus vendedores un sueldo que es la suma del sueldo básico de S/. 250 más 
una comisión que es igual a un porcentaje del monto total vendido, el porcentaje depende de la 
categoría del vendedor como se muestra en la tabla. Además, si el sueldo excedo los S/. 3500 se 
efectúa un descuento del 15% en caso contrario del 8%. Desarrolle el programa que muestre el 
sueldo bruto y neto a pagar, como también el descuento y la comisión aplicada. 
Monto               Comisión 
... 5000               5 % 
5000 ... 10000         8 % 
10000 ... 20000        10 % 
20000 ....             15 % '''


import os
os.system("cls")

monto_vendido = int(input("Ingresa el monto: S/ "))

sueldo_basico = 250

if monto_vendido <= 5000 :
    comision = monto_vendido * 0.05

elif monto_vendido >= 5001 and monto_vendido <= 10000 :
    comision = monto_vendido * 0.08

elif monto_vendido >= 10001 and monto_vendido <= 20000 :
    comision = monto_vendido * 0.10

else :
    comision = monto_vendido * 0.15


sueldo_bruto = sueldo_basico + comision

if sueldo_bruto >= 3500 :
    descuento = sueldo_bruto * 0.15
else :
    descuento = sueldo_bruto * 0.08

sueldo_neto = sueldo_bruto - descuento

print(f"El sueldo bruto a pagar es: S/ {sueldo_bruto:.2f}")
print(f"La comision ganada es: S/ {comision:.2f}")
print(f"El descuento realizado es: S/ {descuento:.2f}")
print(f"El sueldo neto a pagar es: S/ {sueldo_neto:.2f}")



