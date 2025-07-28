
import os
os.system("cls")

primera_edad = int(input("Ingresa la primera edad: "))
segunda_edad = int(input("Ingresa la segunda edad: "))
tercera_edad = int(input("Ingresa la tercera edad: "))

#mayor = max(primera_edad, segunda_edad, tercera_edad)
#menor = min(primera_edad, segunda_edad, tercera_edad)

#print(f"La edad mayor es: {mayor}")
#print(f"La edad menor es: {menor}")

if primera_edad <=0 or segunda_edad <= 0 or tercera_edad <=0 :
    print("Error: Las edades deben ser mayor a 0.")

else:
    
    if primera_edad >= segunda_edad and primera_edad >= tercera_edad :
        mayor = primera_edad
    
    elif segunda_edad >= primera_edad and segunda_edad >= tercera_edad :
        mayor = segunda_edad
    
    else :
        mayor = tercera_edad
    
    
    if primera_edad <= segunda_edad and primera_edad <= tercera_edad :
        menor = primera_edad
    
    elif segunda_edad <= primera_edad and segunda_edad <= tercera_edad :
     menor = segunda_edad

    else :
        menor = tercera_edad
    

    print(f"La Edad Menor es: {menor}")
    print(f"La Edad Mayor es: {mayor}")