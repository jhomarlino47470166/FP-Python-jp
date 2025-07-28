"""Una empresa paga a sus vendedores un sueldo igual al 10% del monto total vendido más S/. 25 
por cada S/. 500 de venta en exceso sobre S/. 5000. Desarrolle el programa que permita calcular 
el sueldo de un vendedor. """

import os
os.system("cls")

m_total = float(input("ingresa el monto total vendido: "))

sueldo = m_total /100 * 10 


if m_total > 5000 : 
    sueldo += ((m_total - 5000 ) // 500 ) * 25

print(f"Sueldo = {sueldo:.2f}")

