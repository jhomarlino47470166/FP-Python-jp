'''El promedio final de un curso se obtiene en base al promedio simple de tres prácticas calificadas. 
Para ayudar a los alumnos, el profesor del curso ha prometido incrementar en dos puntos la nota 
de la tercera práctica calificada, si es que esta no es menor que 10. Desarrolle el programa que 
determine el promedio final de un alumno conociendo sus tres notas.'''


import os
os.system("cls)")

nota1 = int(input("Ingresa tu primera nota: "))
nota2 = int(input("Ingresa tu segunda nota: "))
nota3 = int(input("Ingresa tu tercera nota: "))

p_simple = (nota1 + nota2 + nota3) / 3

if nota3 >= 10 :
    nota3 = nota3 + 2

p_final = (nota1 + nota2 + nota3) / 3

print(f"Mi primera nota es:{nota1} ")
print(f"Mi segunda nota es:{nota2} ")
print(f"Mi tercera nota es:{nota3} ")
print(f"Mi promedio simple es:{p_simple:.2f} ")
print(f"Mi promedio final es:{p_final:.2f} ")