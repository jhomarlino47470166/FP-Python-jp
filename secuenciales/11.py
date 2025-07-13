
import os
os.system("cls")

n1 = int(input("Ingrese el primer número de 3 cifras: "))
n2 = int(input("Ingrese el segundo número de 3 cifras: "))

a1 = n1 // 100         
a2 = (n1 // 10) % 10  
a3 = n1 % 10          

b1 = n2 // 100
b2 = (n2 // 10) % 10
b3 = n2 % 10

nuevo1 = b1 * 100 + a2 * 10 + a3
nuevo2 = a1 * 100 + b2 * 10 + b3

print(f"Nuevos números: {nuevo1} y {nuevo2}")
