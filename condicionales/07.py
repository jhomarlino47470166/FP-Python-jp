'''Desarrolle el programa que lea tres números enteros y determine el número intermedio. No use operadores lógicos en la solución. '''

import os
os.system("cls")



num1 = int(input("Ingresa numero 1: "))
num2 = int(input("Ingresa numero 2: "))
num3 = int(input("Ingresa numero 3: "))


if num1 > num2 :
    if num1 < num3 :
        intermedio = num1

    elif num2 > num3 :
        intermedio = num2

    else :
        intermedio = num3



else :
    if num1 > num3 :
        intermedio = num1

    elif num2 < num3 :
        intermedio = num2

    else :
        intermedio = num3


print(f"El numero intermedio es: {intermedio}")
