'''En  una  oficina  de  empleos  categorizan  a  los  postulantes  en  función  del  sexo  y  de  la  edad  de 
acuerdo a lo siguiente: Si la persona es de sexo femenino: categoría FA, si tiene menos de 23 años 
y FB, en caso contrario. Si la persona es de sexo masculino: categoría MA si tiene menos de 25 
años y MB, en caso contrario.'''

import os
os.system("cls")

genero = input("ingresa tu genero (masculino/femenino) : ").lower()
edad = int(input("Ingresa tu edad : "))

if edad <= 23 and genero == "femenino" :
    categoria = "FA"

elif edad > 23 and genero == "femenino" :
    categoria = "FB"

elif edad <= 25 and genero == "masculino" :
    categoria = "MA"

elif edad > 25 and genero == "masculino" :
    categoria = "MB"

else :
    categoria = "Genero no valido"


print(f"Genero : {genero}")
print(f"Edad : {edad}")
print(f"Categoria : {categoria}")
