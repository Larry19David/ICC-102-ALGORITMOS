def MostrarMenu():
    opcion = -1

    while opcion < 0 or opcion > 7:
        print("Seleccione una opcion del menu: \n\n")
        print("\t1: Capturar una lista.")
        print("\t2: Sacar los ultimos J valores.")
        print("\t3: Invertir lista.")
        print("\t4: Mostrar sub-conjunto.")
        print("\t5: Mostrar  elemento dada una posicion. ")
        print("\t6: Buscar un elemeto.")
        print("\t7: Modificar  la lista.")
        print("\n\n\t0: salir.")

        opcion = int(input("opcion: "))

    return opcion

def CapturarLista():
    nuevaLista = []

    #for valorActual in input().split():
    #    nuevaLista.append(int(valorActual))

    #nuevaLista =(list(map(int, input().split())))

    nuevaLista = [int(valor) for valor in input().split()]
    
    return nuevaLista

def SacarValores(lista, j):
    while j>0:
        print(lista.pop())
        j-=1
        
    return lista

def InvertirLista(lista):
    return lista[::-1]

def SubConjunto(lista, d, h, s):
    return lista[d:h:s]

def  ObtenerElemento(lista, posicion):
     return lista[posicion]

def BusquedaSecuencial(lista, valor):
    return lista.index(valor)
    #for (indice, valorActual) in enumerate(lista):
    #    if valorActual == valor:
    #        return indice
    #return -1
            

listado = []
seleccion = -1


while seleccion !=0:
      print("La lista es: {0}, y su longitud {1}".format(listado, len(listado)))
      seleccion = MostrarMenu()

      if seleccion ==1:
          listado = CapturarLista()
      elif seleccion == 2:
          nuevaEntrada = int(input("Digite la cantidad de valores a sacar: "))
          listado = SacarValores(listado, nuevaEntrada)
      elif seleccion == 3:
          print(InvertirLista(listado))
      elif seleccion == 4:
          desde = int(input("Desde: "))
          hasta = int(input("hasta: "))
          step = int(input("strep: "))
          subConjunto(listado, desde, hasta, step)
      elif seleccion == 5:
          pos = int(input("Digite la posicion: "))
          print(ObtenerElemento(listado, pos))
      elif seleccion == 6:
          val = int(input("Digite el valor: "))
          print(BusquedaSecuencial(listado, val))

                             
