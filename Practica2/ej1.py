def es_mayuscula (cadena):
    if (cadena[0]).isupper() == True:
        print ("la primer letra esmayuscula")
    else:
        print("la primer letra es minuscula")
print(es_mayuscula("computadora"))

cadena = str(input("dame una palabra:"))
def es_mayuscula(una_palabra):
    if una_palabra[0] >= "a" and una_palabra[0] <= "z":
        print("es minuscula")
    else:
        print("es mayuscula")

print(es_mayuscula(cadena))

