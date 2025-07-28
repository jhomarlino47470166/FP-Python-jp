'''20. Desarrolle el programa que lea tres números a, b, c y determine si los números fueron ingresados 
en orden ascendente, descendente o en desorden.'''

import os
os.system("cls")

num_a = int(input("Ingresa primer numero: "))
num_b = int(input("Ingresa segundo numero: "))
num_c = int(input("Ingresa tercer numero: "))


if num_a < num_b and num_b < num_c :
    orden = "ascendente"

elif num_a > num_b and num_b > num_c :
    orden = "descendente"

else :
    orden = "en desorden"


numeros = (num_a, num_b, num_c)

print(f"\nLos numeros son : {numeros}")
print(f"El orden es : {orden}")
