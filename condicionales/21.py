import os
os.system("cls")

codigo = int(input("Ingrese el número de 4 cifras: "))

estado = codigo // 1000
edad = (codigo % 1000) // 10
sexo = codigo % 10

if estado == 1:
    estadoCivil = "Soltero"
elif estado == 2:
    estadoCivil = "Casado"
elif estado == 3:
    estadoCivil = "Divorciado"
elif estado == 4:
    estadoCivil = "Viudo"
else:
    estadoCivil = "Desconocido"

sexoTexto = "Masculino" if sexo == 1 else "Femenino" if sexo == 2 else "Desconocido"

print(f"Estado civil: {estadoCivil}")
print(f"Edad: {edad}")
print(f"Sexo: {sexoTexto}")
