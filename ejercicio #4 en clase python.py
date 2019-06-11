def DecimalABase(valorOrigen, baseDestino):
    resultado = 0
    potencia10 = 1

    while valorOrigen != 0:
        nuevoResiduo = valorOrigen % baseDestino

        resultado += potencia10 * nuevoResiduo
        potencia10 *= 10

        valorOrigen //= baseDestino

    return resultado

def BaseADecimal(valorOrigen, baseOrigen):
    contadoraPotencia = 0
    resultado = 0

    while valorOrigen != 0:
        resultado += baseOrigen ** contadoraPotencia * (valorOrigen % 10)
        valorOrigen //= 10
        contadoraPotencia += 1

    return resultado

valor = int(input("Digite el valor: "))
baseOrigen = int(input("Digite la base origen: "))
baseDestino = int(input("Digite la base destino: "))

if baseOrigen == 10:
    print(DecimalABase(valor, baseDestino))
elif (baseDestino == 10):
    print(BaseADecimal(valor, baseOrigen))
else:
    print("No puedo convertir eso.")
