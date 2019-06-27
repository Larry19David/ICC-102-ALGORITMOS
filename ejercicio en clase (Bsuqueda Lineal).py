def BusquedaLineal (lista, valor):
    for posActual in range(len(lista)):
        if lista [posActual] == valor:
            return posActual
    return -1

def BusquedaBinaria(lista, valor):
      limI = 0
      limS = len(lista) -1
      while limI<limS:
           posCentral = int(limI/2 + limS/2)
           if lista[posCentral] == valor:
                return posCentral
           elif lista[posCentral] > valor:
                  limS = posCentral - 1
           else:
                limI = posCentral + 1
      return -1 
      
      

valores = [float(x) for x in input().split()]
destino = float(input())
#resultado = BusquedaLineal(valores, destino)
#print("No encontro el valor" if resultado < 0 else "El valor esta en {0}".format(resultado))
resultado = BusquedaBinaria(valores, destino)
print("No encontro el valor" if resultado < 0 else "El valor esta en {0}".format(resultado))
      

