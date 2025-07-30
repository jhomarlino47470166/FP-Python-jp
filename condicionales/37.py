import os
os.system("cls")

pamela = int(input("Votos para Pamela: "))
carol = int(input("Votos para Carol: "))
fanny = int(input("Votos para Fanny: "))

total_votos = pamela + carol + fanny
mayoria = total_votos / 2 + 1

if pamela >= mayoria:
    ganador = "Pamela gana en primera vuelta"
elif carol >= mayoria:
    ganador = "Carol gana en primera vuelta"
elif fanny >= mayoria:
    ganador = "Fanny gana en primera vuelta"
else:
    votos = [("Pamela", pamela), ("Carol", carol), ("Fanny", fanny)]
    votos.sort(key=lambda x: x[1], reverse=True)

    if votos[0][1] == votos[1][1] and votos[1][1] == votos[2][1]:
        ganador = "Elección anulada: empate entre las tres"
    elif votos[1][1] == votos[2][1]:
        ganador = "Elección anulada: empate en segundo puesto"
    else:
        ganador = f"Segunda vuelta: {votos[0][0]} y {votos[1][0]}"

print(ganador)
