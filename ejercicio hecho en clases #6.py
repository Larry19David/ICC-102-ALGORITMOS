valores =[int(x) for x in input().split()]
suma = sum(valores)

for indiceActual in range(len(valores)):
    print("{0}: ".format(valores[indiceActual]), end = '')  
    proporcionActual = valores[indiceActual]/suma * 100
    proporcionCopia = proporcionActual
    while(proporcionActual > 0):
        print("*", end = '')
        proporcionActual-=1
    print("{0}%".format(proporcionCopia))
    


      
