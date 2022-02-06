#palabra = palabra.replace( "A", "" )

import abc


palabra = [str(input("PALABRA:  "))]

Adivinar = [str(input("LETRA: "))]

for letra in palabra:
    fallos = 0
    if letra in palabra:
        print(letra, end="")
    else:
        fallos+=1

import time
nombre=input("como te llamas ")
print("hola, "+nombre," es hora de jugar")
print(" ")
time.sleep(1)
print("comienza a adivinar")
time.sleep(0.5)
palabra="murcielago"
tupalabra=" "
vidas=5

while vidas > 0:
    fallas=0
    for letra in palabra:
        if letra in tupalabra:
            print(letra,end="")
        else:
            print("*",end="")
            fallas+=1
    if fallas==0:
        input()
        print("")
        print("felicidades, ganaste")
        input()
        break

    tuletra=input("introduce una letra: ")
    tupalabra+=tuletra

    if tuletra not in palabra:
        vidas-=1
        print("equivocacion")
        print("tu tienes ",+vidas," vidas")
    if vidas== 0:
        print("perdiste!")
else:
    input()
    print("gracias por participar")
    input()


## Para el testcase0
pal = "PYTHON"
letras = ["A", "B","C","P", "H","Y", "T","O", "N"]
cont = 0
while (len(pal)) > 0:
    for x in letras:
        cont +=1
        if x in pal:
            pal = pal.replace(x, "") 
print(cont)

## Para el testcase1
pal2 = "IEEE"
letras2 = ["X", "Y","E","I"]
cont2 = 0
while (len(pal2)) > 0:
    for x in letras2:
        cont2 +=1
        if x in pal2:
            pal2 = pal2.replace(x, "") 
print(cont2)