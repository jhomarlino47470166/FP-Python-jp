import os
os.system("cls")

cantA = int(input("Ingrese cantidad de producto A: "))
cantB = int(input("Ingrese cantidad de producto B: "))

precioA = 25
precioB = 30

importeA = cantA * precioA
importeB = cantB * precioB

descA = importeA * 0.15 if cantA > 50 else 0
descB = importeB * 0.10 if cantB > 60 else 0

importe_bruto = importeA + importeB
descuento = descA + descB
total = importe_bruto - descuento

print(f"Importe bruto: S/. {importe_bruto:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {total:.2f}")
