'''En un supermercado hay una promoción según la cual el cliente raspa una tarjeta que contiene un 
número oculto. Si el número de la tarjeta es par no menor de 100, el cliente obtiene un descuento 
del 15 %, caso contrario será del 5 % sobre el importe de la compra.  Desarrolle el programa que 
muestre el número de la tarjeta, el monto de la compra y el descuento. '''


import os
os.system("cls")

compra = int(input("ingresar compra: "))
tarjeta = int(input("ingresar tarjeta: "))


#if tarjeta > 100 and tarjeta % 2 else  

#descuento = compra * (0.15 if tarjeta > 100 and tarjeta % 2 == 0 else 0.05)

#print(f"Tarjeta   = {tarjeta}")
#print(f"Compra    = {compra}")
#print(f"Descuento = {descuento:.2f}")
#print(f"Total = {compra - descuento:.2f}")


if tarjeta % 2 == 0 and tarjeta >= 100:
    descuento = compra * 0.15
else:
    descuento = compra * 0.05

total = compra - descuento

print("\nDETALLE DE COMPRA:")
print(f"Número de la tarjeta: {tarjeta}")
print(f"Monto de la compra: S/. {compra:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {total:.2f}")

