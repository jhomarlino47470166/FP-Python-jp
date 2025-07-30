import os
os.system("cls")

hora = int(input("Ingrese la hora (0-23): "))
minutos = int(input("Ingrese los minutos (0-59): "))

if 0 <= hora < 24 and 0 <= minutos < 60:
    if hora == 0:
        h12 = 12
        periodo = "AM"
    elif hora < 12:
        h12 = hora
        periodo = "AM"
    elif hora == 12:
        h12 = 12
        periodo = "PM"
    else:
        h12 = hora - 12
        periodo = "PM"
    
    print(f"{h12}:{minutos:02d} {periodo}")
else:
    print("Hora inválida")
