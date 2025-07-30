import os
os.system("cls")

mes = int(input("Ingrese el número de mes (1-12): "))
anio = int(input("Ingrese el año: "))

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

if mes < 1 or mes > 12:
    print("Mes inválido")
else:
    if mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            dias = 29
        else:
            dias = 28
    elif mes in [1, 3, 5, 7, 8, 10, 12]:
        dias = 31
    else:
        dias = 30

    print(f"{meses[mes-1]} tiene {dias} días")
