'''Una institución benéfica recibe anualmente una donación y lo reparte de la siguiente manera: Si 
el monto es de $ 10000 o más, 30% se destina al centro de salud; 50% al comedor de niños, y el 
resto se invierte en la bolsa. Si el monto de la donación es menor a 10000, 25% se destina al centro 
de salud; 60% al comedor de niños, y el resto se invierte en la bolsa.'''

import os
os.system("cls")

donacion = float(input("Monto recibido de donacion: "))


if donacion >= 10000 :
    salud = donacion * 0.30
    comedor = donacion * 0.50

else :
    salud = donacion * 0.25
    comedor = donacion * 0.60

bolsa = donacion - (salud + comedor)

print(f"Donacion: $ {donacion:.2f}")
print(f"Centro de Salud: $ {salud:.2f}")
print(f"Comedor de Niños: $ {comedor:.2f}")
print(f"Bolsa de Valores: $ {bolsa:.2f}")




