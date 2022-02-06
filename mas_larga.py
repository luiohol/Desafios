def lenLista():
	lista = []
	cadena = str(input("ingrese la cadena: "))
	lista.append(cadena)
	mayor = None
	for valor in lista:
		if mayor is None or valor > mayor :
			mayor = valor
		print ("mas larga es:", mayor) #imprime la palabra mas larga


for ejecucion in range(5): #procesa 5 veces la función
	lenLista()