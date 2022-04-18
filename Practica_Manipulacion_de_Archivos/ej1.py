def start_with(letra, archivo):
    count = 0
    with open(archivo, "r") as file:
        for line in file:
            if (line[0] != letra.lower() or line[0] != letra.upper()):
                count += 1
    print("El numero de lineas que empiezan con", letra, "es", count)


start_with("M", "/Users/mateocampagnale/Downloads/Fundamentos_de_informatica-master/Datos_Personales/Datos.txt")