totalPreguntas = int(input('Ingrese el total de preguntas: '))
totalCorrectas = int(input('Ingrese cantidad respuestas correctas: '))
totalIncorrectas = int(input('Ingrese cantidad respuestas incorrectas: '))
notaFinal = 4*totalCorrectas - totalIncorrectas
print('La calificacion final es: {0} ({1:.2f}%)'.format(notaFinal,((totalCorrectas/totalPreguntas)*100)))

