import os
os.system("cls")

productoA = int(input("Ingresa cantidad de prodcuto A : "))
productoB = int(input("Ingresa cantidad de prodcuto B : "))

costoA = 25
costoB = 30

importeA = productoA * costoA
importeB = productoB * costoB

t_importe = importeA + importeB

if productoA > 50 :
    descuentoA = importeA * 0.15
else :
    descuentoA = 0

if productoB > 60 :
    descuentoB = importeB * 0.10
else : 
    descuentoB = 0

t_descuento = descuentoA + descuentoB

t_pagar = t_importe - t_descuento

print("DETALLE DE COMPRA")
print(f"Importe de producto A : S/ {importeA}")
print(f"Importe de producto B : S/ {importeB}")
print(f"Importe total : S/ {t_importe}")
print(f"Descuento aplicado : S/ {t_descuento}")
print(f"Total a pagar : S/ {t_pagar}")







