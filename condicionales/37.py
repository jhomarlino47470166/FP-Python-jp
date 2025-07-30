import os
os.system("cls")

pamela = int(input("Votos para Pamela: "))
carol = int(input("Votos para Carol: "))
fanny = int(input("Votos para Fanny: "))

total = pamela + carol + fanny
mayoria = total / 2 + 1

if pamela >= mayoria:
    print("Pamela gana en primera vuelta")
elif carol >= mayoria:
    print("Carol gana en primera vuelta")
elif fanny >= mayoria:
    print("Fanny gana en primera vuelta")
else:
    if pamela == carol == fanny:
        print("Elección anulada: empate entre las tres")
    elif pamela == carol and pamela > fanny:
        print("Segunda vuelta: Pamela y Carol")
    elif pamela == fanny and pamela > carol:
        print("Segunda vuelta: Pamela y Fanny")
    elif carol == fanny and carol > pamela:
        print("Segunda vuelta: Carol y Fanny")
    elif pamela > carol and carol == fanny:
        print("Elección anulada: empate en segundo puesto")
    elif carol > pamela and pamela == fanny:
        print("Elección anulada: empate en segundo puesto")
    elif fanny > pamela and pamela == carol:
        print("Elección anulada: empate en segundo puesto")
    elif pamela > carol and carol > fanny:
        print("Segunda vuelta: Pamela y Carol")
    elif pamela > fanny and fanny > carol:
        print("Segunda vuelta: Pamela y Fanny")
    elif carol > pamela and pamela > fanny:
        print("Segunda vuelta: Carol y Pamela")
    elif carol > fanny and fanny > pamela:
        print("Segunda vuelta: Carol y Fanny")
    elif fanny > pamela and pamela > carol:
        print("Segunda vuelta: Fanny y Pamela")
    else:
        print("Segunda vuelta: Fanny y Carol")
