import random
from operator import itemgetter

times = []

##DEFININDO TIMES##
## [NOME, PONTOS, GOLS, JOGOS]  
times.append(["Caique cabeça rosada do parana", 0, 0, 0])
times.append(["igao sacudo do submundo", 0, 0, 0])
times.append(["uniao flasco", 0, 0, 0])
times.append(["david barba de pentelho da mangueira do norte", 0, 0, 0])
times.append(["pele comeu a xuxa", 0, 0, 0])
times.append(["meupirualado", 0, 0, 0])
times.append(["chapecoense vs aviao", 0, 0, 0])
times.append(["menino ney", 0, 0, 0])
times.append(["cidade do meu saco esquerdo", 0, 0, 0])
times.append(["cidade malhado", 0, 0, 0])

def partida(timeA, timeB):
    ##Sorteando gols de cada time na partida
    golsTimeADurantePartida = random.randint(0,3)
    golsTimeBDurantePartida = random.randint(0,3)

    ##Guardando os gols do time nas partidas
    timeA[2] += golsTimeADurantePartida
    timeB[2] += golsTimeBDurantePartida

    timeA[3] += 1
    timeB[3] += 1

    ##Distribuindo pontos do time vencedor ou de empates
    if golsTimeADurantePartida > golsTimeBDurantePartida:
        timeA[1] = timeA[1] + 3
    elif golsTimeADurantePartida < golsTimeBDurantePartida:
        timeB[1] = timeB[1] + 3
    else:
        timeA[1] = timeA[1]+1
        timeB[1] = timeB[1]+1

##Iniciando Partidas e verificando se sao jogos repetidos##
for i in range(len(times)):
    for j in range(i + 1, len(times)):
        if(times[i] == times[j]):
            continue
        else:
            partida(times[i], times[j])

##Listando final do campeonato##
def listaTimes():
    times.sort(key=itemgetter(1, 2), reverse=True)
    for x in times:
        print(x)

listaTimes()