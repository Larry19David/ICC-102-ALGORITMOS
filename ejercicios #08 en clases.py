from random import randint
from time import time

lista = []

for i in range(0,100):
    lista.append(randint(0,1000000))

print(lista)

temp = 0
tiempo_inicial = time()
for j in range(1,len(lista)):
    for i in range(0,len(lista)-j):
        if lista[i]>lista[i+1]:
            temp = lista[1]
            lista[i] = lista[i+1]
            lista[i+1] = temp
tiempo_final = time()
print(lista)
print("tiempo de ejecucion: "+str(tiempo_final-tiempo_inicial))

