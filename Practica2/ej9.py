lista_nombres = []
lista_edades = []
nombres = input("ingrese nombre:")
if nombres != "*":
    lista_nombres.append(nombres)
    edad = int(input("ingrese edad:"))
    lista_edades.append(edades)
else:
    print("no hay alumnos")
while nombres != "*":
    nombres = input("ingrese nombre:")
if nombres != "*":
    lista_nombres.append(nombres)
edad = int(input("ingrese edad:"))
lista_edades.append(edades)
else:
    edad_maxima = max(lista_edades)
    ubicacion = list.findex(lista_edades, edad_maxima)
    nombre_maximo = lista_nombres[ubicacion]

    print("la edad maxima es: " + str(edad_maxima) + "y corresponde a la de" + str(nombre_maximo))