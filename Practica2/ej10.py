contadores = {}
cadena = input("escribi una cadena:")
for caracter in cadena:
    if caracter in contadores:
        contadores[caracter]+=1
	else: 
	    contadores[caracter]=1
for campo,valor in contadores.items():
    print(campo,valor)