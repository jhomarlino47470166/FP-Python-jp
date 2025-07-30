import os
os.system("cls")

cuota = float(input("Ingrese el monto de la cuota: "))
dia_pago = int(input("Ingrese el día de pago: "))

if 1 <= dia_pago <= 10:
    descuento = max(5, cuota * 0.02)
    total = cuota - descuento
elif 11 <= dia_pago <= 20:
    descuento = 0
    total = cuota
elif 21 <= dia_pago <= 31:
    recargo = max(10, cuota * 0.03)
    total = cuota + recargo
else:
    print("Día inválido")
    total = None

if total is not None:
    print(f"Total a pagar: ${total:.2f}")
