import os
os.system("cls")

juan = float(input("Ingrese el aporte de Juan en dólares: "))
rosa = float(input("Ingrese el aporte de Rosa en dólares: "))
daniel_soles = float(input("Ingrese el aporte de Daniel en soles: "))

tipo_cambio = 3.00
daniel_dolares = daniel_soles / tipo_cambio

total = juan + rosa + daniel_dolares

p_juan = (juan / total) * 100
p_rosa = (rosa / total) * 100
p_daniel = (daniel_dolares / total) * 100

print(f"Capital total en dólares: {total:.2f}")
print(f"Juan aporta: {p_juan:.2f}%")
print(f"Rosa aporta: {p_rosa:.2f}%")
print(f"Daniel aporta: {p_daniel:.2f}%")
