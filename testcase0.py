## Para el testcase0
pal = input("Palabra:")
letras = []
letras.append(input("Letra: "))
cont = 0
while (len(pal)) > 0:
    for x in letras:
        cont +=1
    if x in pal:
        pal = pal.replace(x, "") 
    continue        

print(letras)
print(cont)