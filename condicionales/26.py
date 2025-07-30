import os
os.system("cls")

monto = float(input("Ingrese el monto total de la compra: "))

if monto > 5000:
    prestamo = monto * 0.30
else:
    prestamo = monto * 0.20

interes = prestamo * 0.10
propio = monto - prestamo

print(f"Pago con préstamo: ${prestamo + interes:.2f}")
print(f"Pago con dinero propio: ${propio:.2f}")
