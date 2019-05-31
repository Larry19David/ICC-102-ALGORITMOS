Algoritmo moduloIterativo
	Escribir 'digite el divisor: '
	Leer divisor
	Escribir 'digite el dividendo: '
	Leer dividendo
	Si dividendo>0 y divisor>0 Entonces
		resultado <- CalcularResiduo(divisor,dividendo)
	SiNo
		Escribir 'solo positivos'
	FinSi
	Escribir resultado
FinAlgoritmo

Funcion divisor <- CalcularResiduo(divisor,dividendo)
	Repetir
	Hasta Que divisor>dividendo
	divisor <- divisor-dividendo
FinFuncion

