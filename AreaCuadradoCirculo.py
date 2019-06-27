#Programa: que toma las medidas del cuadrado y circulo para sacar el area de cada uno.
#Hecho por: David Gabriel Rosario Sosa.
#Fecha: 16-06-2019, Hora: 2:54pm
#Nombre: AreaCuadradoCirculo    
print ("----Welcome----")
while True:
    
    print ("")
    print("(0) para salir. ")
    print ("(1) para continuar.")
    opc = int(input(""))
    if opc == 0:
        print("----Fin del programa----")
        break
    if opc == 1:
        print ("---Programa que toma medidas del cuadrado y el circulo para saber su area.---")
        print("")
        print ("--Determinar el area del cuadrado--")
        LC = float(input("Intruduzca la medida del lado del cuadrado: "))
        AreCua = (LC*LC)
        print("El area del cuadrado es: ", AreCua)
        print ("")
        print("--Determinar el area del circulo--")
        pi = 3.14
        r = float(input("indruzca el radio del circulo: "))
        AreCir = (pi *  r**2)
        print("el area del circulo es: ", AreCir)
        print("")
        Lb = float(input("intrduca el lado del bebedero: "))
        AreLb = (Lb*Lb)
        print("el area del bebedero es: ", AreLb)
        print ("")
        ArePod = AreCua-(AreCir + AreLb)
        print ("El area a podar en el solar es: ", ArePod)
        
