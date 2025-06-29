import os
os.system("cls")    

E1 = int(input("Nota Examen 1: "))
E2 = int(input("Nota Examen 2: "))
E3 = int(input("Nota Examen 3: "))

propina = 20
if E1 > 10 : propina += 5
if E2 > 10 : propina += 5  
if E3 > 10 : propina += 5

print(f"Propina: {propina} €")

