import os
os.system("cls")

curso = input("Ingrese el curso (Matemática, Física, Química): ").lower()

pc1 = float(input("Ingrese nota PC1: "))
pc2 = float(input("Ingrese nota PC2: "))
pc3 = float(input("Ingrese nota PC3: "))
ep = float(input("Ingrese nota Examen Parcial: "))
ef = float(input("Ingrese nota Examen Final: "))

if curso == "matemática":
    promedio = pc1 * 0.10 + pc2 * 0.20 + pc3 * 0.10 + ep * 0.30 + ef * 0.30
elif curso == "física":
    promedio = (pc1 + pc2 + pc3 + ep + ef) / 5
elif curso == "química":
    promedio = pc1 * 0.10 + pc2 * 0.30 + pc3 * 0.10 + ep * 0.25 + ef * 0.25
else:
    promedio = 0

condicion = "Aprobado" if promedio >= 13 else "Desaprobado"

print(f"Promedio final: {promedio:.2f} - {condicion}")
