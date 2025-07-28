"""Un padre ha decido dar una propina a su hijo en base a las notas en Matemáticas y Física. Si la 
nota de Matemáticas es  mayor a  17, le dará S/. 3, en caso contrario sólo le dará S/. 1 por cada 
punto. Si la nota de Física es mayor a S/. 15, le dará S/. 2, en caso contrario solo S/. 0.50. Además, 
si el promedio de las notas es mayor a 16, le obsequiará un reloj."""

import os
os.system("cls")

n_matematica = int(input("Ingresa la nota de Matemática: "))
n_fisica = int(input("Ingresa la nota de Física: "))


propina = n_matematica + n_fisica / 2
if n_matematica > 17 : propina = propina + ( n_matematica - 17) * 2
if n_fisica > 15 : propina = propina + ( n_fisica - 15) * 1.5

promedio = (n_matematica + n_fisica) / 2
reloj = "SI" if promedio > 16 else "NO"

print(f"Propina = {propina}")
print(f"Reloj = {reloj}")


