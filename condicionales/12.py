import os
os.system("cls")

numero = int(input("Número = "))

# if numero == 1 : print("Lunes")
# elif numero == 2 : print("Martes")
# elif numero == 3 : print("Miercoles")
# elif numero == 4 : print("Jueves")
# elif numero == 5 : print("Viernes")
# elif numero == 6 : print("Sabado")
# elif numero == 7 : print("Domingo")
# else : print("Error")

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
if numero >= 1 and numero <= 7 : print(dias[numero-1]) else : print("Error")

print("dias:")