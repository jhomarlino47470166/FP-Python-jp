import os
os.system("cls")

numero = int(input("Número = "))

#if numero > 0 : print("Positivo")
#elif numero == 0 : print("Cero")
#else : print("Negativo")


print("positivo") if numero > 0 else print("Cero") if numero == 0 else print("Negativo")