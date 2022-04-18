def que_signo_tiene (numero) :
    if abs(numero) == numero:
        print ("es positivo")
    else:
        if numero == 0:
            print ("es cero")
        else:
            print ("es negativo")

print(que_signo_tiene (15))