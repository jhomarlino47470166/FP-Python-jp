

import os
os.system("cls")

numero = int(input("Ingrese numero de 4 cifras: "))

digito1 = numero // 1000
digito2 = numero // 100 % 10
digito3 = numero // 10 % 10
digito4 = numero % 10

mayor = max(digito1, digito2, digito3, digito4)
menor = min(digito1, digito2, digito3, digito4)

num1 = mayor * 10 + menor
num2 = menor * 10 + mayor

resultado = max(num1, num2)

print("El mayor número de dos cifras es:", resultado)




