archivo = open("/Users/mateocampagnale/Downloads/Fundamentos_de_informatica-master/Datos_Personales/Datos.txt","r")
lineas = archivo.readlines(70)
print('el archivo tiene', len(lineas), 'lineas')
print('el contenido del archivo')
for linea in lineas:
    print(linea, end='')
archivo.close()