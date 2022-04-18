import re
lista = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
def verificar_palabras(lista):
    for elemento in lista:
        resultado = re.match("P\w*)\W(P\w*)", elemento)
        if resultado is not None:
            print(resultado.group())
verificar_palabras(lista)