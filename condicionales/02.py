import os
os.system("cls")

precio = 20
unidades = int(input("Unidades: "))
compra = precio * unidades

#descuento = 0
# if compra <= 500 : descuento = compra * 0.12
# elif compra > 500 and compra <= 700: descuento = compra * 0.14
# else : descuento = compra * 0.16

# descuento = compra * 0.14
# if compra <= 500: descuento = compra * 0.12
# elif compra <= 700: descuento = compra * 0.16

descuento = compra * (0.12 if compra <= 500 else 0.16 if compra > 700 else 0.14)
caramelo = 5 if unidades <= 50 else 15 if unidades > 100 else 10

print(f"Compra: {compra:.2f} €")
print(f"Descuento: {descuento:.2f} €")
print(f"Total: {compra - descuento:.2f} €")
print(f"Caramelo: {caramelo} unidades")



