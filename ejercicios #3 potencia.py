def calcularPotencia(b, e):
    acumulado = 1

    while e>0:
        acumulado = acumulado * b
        e = e - 1

    return acumulado

base = -1
exponente = -1
while base <= 0 or exponente <= 0:
    base = int(input("digite la base: "))
    exponente = int(input("digite el exponente: "))

    if base <=0 or exponente <=0:
        print("solo positivos.")

potencia = calcularPotencia(base, exponente)
print(potencia)
