salida = []
with open("/Users/mateocampagnale/Downloads/Fundamentos_de_informatica-master/Datos_Personales/Datos.txt","r") as f:
    lineas = [linea.split() for linea in f]

for linea in lineas:
    print(linea)

with open("/Users/mateocampagnale/Downloads/Fundamentos_de_informatica-master/Datos_Personales/Datos.txt","r") as f:
    data = f.readlines()[10]
print(data)