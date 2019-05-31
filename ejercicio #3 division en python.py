divisor = -1
dividendo = -1

while divisor <= 0 or dividendo <= 0:
    divisor = int(input("digite el divisor: "))
    dividendo = int(input("digite dividendo: "))

    if divisor > 0 and dividendo > 0:
        resultado = divisor/dividendo
        print(resultado)
    else:
        print("solo positivos.")



