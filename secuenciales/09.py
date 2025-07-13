
import os
os.system("cls")

numero = int(input("Ingrese un número de 4 cifras: "))

millar = numero // 1000
centena = (numero // 100) % 10
decena = (numero // 10) % 10
unidad = numero % 10

suma_cifras = millar + centena + decena + unidad

print(f"\nLa suma de las cifras es: {suma_cifras}")
