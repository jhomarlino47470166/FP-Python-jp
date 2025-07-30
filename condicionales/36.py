import os
os.system("cls")

cuadernos = int(input("Ingrese número de cuadernos: "))

if cuadernos < 12:
    lucas = faber = pilot = 0
elif cuadernos < 24:
    lucas = cuadernos // 4
    faber = pilot = 0
elif cuadernos < 36:
    faber = (cuadernos // 4) * 2
    lucas = pilot = 0
else:
    pilot = (cuadernos // 4) * 2
    faber = (cuadernos // 6)
    lucas = (cuadernos // 12)

total = lucas + faber + pilot

print(f"Lucas: {lucas}, Faber: {faber}, Pilot: {pilot}")
print(f"Total lapiceros: {total}")
