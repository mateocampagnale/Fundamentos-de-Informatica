nombreApellidos = input('Ingrese nombre y dos apellidos: ')
datos = nombreApellidos.split()
for palabra in datos:
    palabra = palabra.capitalize()
    print(palabra,end=' ')
print()