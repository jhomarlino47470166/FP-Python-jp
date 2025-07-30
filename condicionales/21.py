import os
os.system("cls")

numero = int(input("Ingresa el numero de 4 digitos: "))

estado = numero // 1000
edad = (numero % 1000) // 10
sexo = numero %10

if estado == 1 : 
    estado = "soltero"
elif estado == 2 :
    estado = "casado"
elif estado == 3 :
    estado = "divorciado"
elif estado == 4 :
    estado = "viudo"
else :
    estado = "no identificado"


if sexo == 1 :
    sexo = "masculino"
elif sexo == 2 :
    sexo = "femenino"
else :
    sexo = "desconocido" 

print(f"Tu estado civil es : {estado} ")
print(f"Tu edad es : {edad}")
print(f"Tu sexo es : {sexo} ")
