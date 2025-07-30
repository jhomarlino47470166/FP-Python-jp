import os
os.system("cls")

ausencia = float(input("Ingrese horas de ausencia: "))
defectuosos = int(input("Ingrese tornillos defectuosos: "))
no_defectuosos = int(input("Ingrese tornillos no defectuosos: "))

cond1 = ausencia <= 1.5
cond2 = defectuosos < 300
cond3 = no_defectuosos > 10000

if cond1 and cond2 and cond3:
    grado = 20
elif cond1 and cond2:
    grado = 12
elif cond1 and cond3:
    grado = 13
elif cond2 and cond3:
    grado = 15
elif cond1:
    grado = 7
elif cond2:
    grado = 8
elif cond3:
    grado = 9
else:
    grado = 5

print(f"Grado de eficiencia: {grado}")
