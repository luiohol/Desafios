"""Ingresar una cadena y un valor entero que indique la cantidad de veces que 
se deberá repetir ésta. 
El programa deberá procesar 5 cadenas e ir informando los valores obtenidos. 
Al final, deberá mostrar cual es la cadena obtenida de mayor longitud."""
lista = []
for i in range(5):
	cadena = str(input("ingrese la cadena: "))
	lista.append(cadena)	
	for i in range(int(input("numero de veces que se repite : "))):
		print(cadena) #imprime la cantidad de veces indicada

print()

larga = sorted(lista, key=len, reverse=True) #ordena la lista de forma descendente segun longitud
print("La cadena mas larga: ",larga[0]) #imprime la primera de la lista

