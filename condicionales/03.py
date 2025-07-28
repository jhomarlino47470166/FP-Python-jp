'''Los ángulos se clasifican de la siguiente manera: nulo (0°), Agudo (0°< x < 90°), Recto (90°),
Obtuso (90° < x <180°), Llano (180°), Cóncavo (180°< x < 360°), Completo (360°). Desarrolle
el programa que determine la clasificación de un ángulo dado en grados.'''

import os
os.system("cls")

angulo = float(input("Ingresa el angulo en grados°: "))

if angulo == 0 :
    print("El angulo es: nulo")

elif angulo > 0 and angulo < 90 :
    print("El angulo es: Agudo")

elif angulo == 90 :
    print("El angulo es: Recto")

elif angulo > 90 and angulo < 180 :
    print("El angulo es: Obtuso")

elif angulo == 180 :
    print("El angulo es: Llano")

elif angulo > 180 and angulo < 360 :
    print("El angulo es: Cóncavo")

elif angulo == 360 :
    print("El angulo es: Completo")

else:
    print("No tiene clasificacion")

