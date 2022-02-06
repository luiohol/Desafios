palabra = input("Palabra:  ")
ahorcado = list(palabra)
largo = (len(ahorcado))
fallos=0
while (largo)  != 0:

  letra = input("Letra: ")
  fallos+=1
  while letra in ahorcado:
    ahorcado.remove(letra)
    largo = (len(ahorcado))
 
print ("Tuviste :",fallos,"  Fallos!")
