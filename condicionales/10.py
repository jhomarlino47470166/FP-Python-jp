import os
os.system("cls")

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
n5 = float(input("Nota 5: "))

notas = [n1, n2, n3, n4, n5]

mayor = max(notas)
menor = min(notas)

notas.remove(mayor)
notas.remove(menor)

promedio = sum(notas) / 3

print(f"Nota mayor eliminada: {mayor}")
print(f"Nota menor eliminada: {menor}")
print(f"Promedio final: {promedio:.2f}")

if promedio >= 6.0:
    print("Resultado: ¡Aprobado!")
else:
    print("Resultado: Reprobado.")
