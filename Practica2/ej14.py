def calcularTemperaturaMedia(temp1,temp2):
	return (temp1 + temp2)/2

cantidad=int(input("¿Cuántas temperaturas vas a calcular?:"))
for indice in range(cantidad):
	tmin = float(input("Introduce temperatura mínima:"))
	tmax = float(input("Introduce temperatura máxima:"))
	print("Temperatura media:",calcularTemperaturaMedia(tmin,tmax))
