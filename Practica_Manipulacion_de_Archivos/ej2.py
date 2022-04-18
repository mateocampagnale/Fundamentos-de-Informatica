def imprimir(cantidad_de_filas, archivo):
    file = open(archivo, "r")
    for i in range(0, cantidad_de_filas):
        print(file.readline())


imprimir(3, '/Users/mateocampagnale/Downloads/Fundamentos_de_informatica-master/Datos_Personales/Datos.txt')
