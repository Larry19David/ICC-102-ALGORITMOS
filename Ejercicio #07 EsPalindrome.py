a = int(input("digite la palabra   "))
lista=[]

lista.append(a)
listaInvertida = lista[::-1]
if lista == listaInvertida:
        print ("es palindroma")
else:
        print ("no es palindroma")
          
