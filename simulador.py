#Play-In
import random

pool1 = ["LGD Gaming" ,"MAD Lions" ,"Team Liquid" ,"PSG Talon"]
pool2 = ["INTZ","Unicorns of love","V3 Esports","Rainbow7","Legacy Esports","SuperMassive"]
groupA = []
groupB = []
rodeios = 0

def embaralhar(vezes,lista):
    x = 0
    while x < vezes:
        random.shuffle(lista)
        x = x + 1
    return lista
def sorteioPote1(vezes,pool1,groupA,groupB):
    contador = 0
    manivela = 0
    while contador != len(pool1):
        if manivela % 2 == 0:
            embaralhar(10,pool1)
            sorteio = random.choice(pool1)
            print("TIME SORTEADO NO GRUPO A: " , sorteio)
            print("")
            groupA.append(sorteio)
            pool1.remove(sorteio)
            manivela = manivela + 1
        else:
            embaralhar(10,pool1)
            sorteio = random.choice(pool1)
            print("TIME SORTEADO NO GRUPO B: " , sorteio)
            print("")
            groupB.append(sorteio)
            pool1.remove(sorteio)
            manivela = manivela + 1

    print("GRUPOS DO POTE 1")
    resultado1 = print("Grupo A: " , groupA[0],"|",groupA[1])
    print("")
    resultado2 = print("Grupo B: " , groupB[0],"|",groupB[1])
    print("")


    return resultado1,resultado2

#Sorteio do pote 1 nos grupos
#               vezes do sorteio|pote|grupo a|grupo b
sortearPote1 = sorteioPote1(100,pool1,groupA,groupB)

def sorteioPote2(vezes,pool2,groupA,groupB):
    contador = 0
    manivela = 0
    while contador != len(pool2):
        if manivela % 2 == 0:
            embaralhar(10,pool2)
            sorteio = random.choice(pool2)
            print("TIME SORTEADO NO GRUPO A: " , sorteio)
            print("")
            groupA.append(sorteio)
            pool2.remove(sorteio)
            manivela = manivela + 1
        else:
            embaralhar(10,pool2)
            sorteio = random.choice(pool2)
            print("TIME SORTEADO NO GRUPO B: " , sorteio)
            print("")
            groupB.append(sorteio)
            pool2.remove(sorteio)
            manivela = manivela + 1
    print("-----------------------------------------------------------------------------------------------")
    print("SORTEIO COMPLETO")
    resultado1 = print("Grupo A: " , groupA[0]," | ",groupA[1]," | ",groupA[2]," | ",groupA[3]," | ",groupA[4],"|")
    print("")
    resultado2 = print("Grupo B: " , groupB[0]," | ",groupB[1]," | ",groupB[2]," | ",groupB[3]," | ",groupB[4]," | ")


    return resultado1,resultado2
sortearPote2 = sorteioPote2(100,pool2,groupA,groupB)


