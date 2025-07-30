import os
os.system("cls")

peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))

imc = peso / (estatura ** 2)

if imc < 20:
    grado = "Delgado"
elif 20 <= imc <= 25:
    grado = "Normal"
elif 25 < imc <= 27:
    grado = "Sobrepeso"
else:
    grado = "Obesidad"

print(f"IMC: {imc:.2f} - {grado}")
