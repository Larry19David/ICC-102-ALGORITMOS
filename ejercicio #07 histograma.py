valores = [int(x) for x in input().split()]
suma = sum (valores)
proporciones = []
for indiceActual in range(len(valores)):
     proporciones.append(valores[indiceActual] / suma * 100)
     
     print("{0}:".format(valores[indiceActual]), end = '')
     proporcionActual = proporciones[indiceActual]
     while (proporciones[indiceActual] > 0):
          print ("*", end = '')
          proporciones[indiceActual]-=1
     print("{0}%" . format(proporcionActual))

    
