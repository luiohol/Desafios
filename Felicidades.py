from random import randint
from time import sleep

def fold(list):
    string = ''
    for item in list:
        string +=  item
    return string
def randtxt(count):
    tempstr = ''
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(1, count + 1):
        tempstr += abc[randint(0, len(abc) - 1)]
    return tempstr

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
h1 = a1 = p1 = p2 = y1 = b = i1 = r = t = h2 = d = a2 = y2 = s1 = p3 = e = y3 = k = i2 = o = u = s2 = abc[randint(0,23)]
strtotal = f'{h1}{a1}{p1}{p2}{y1} {b}{i1}{r}{t}{h2}{d}{a2}{y2}, {s1}{p3}{e}{y3}{k}{i2}{o}{u}{s2}'
string = "happy birthday, speykious"
strlist = list(string)
total = list(strtotal)
for i in range(len(strtotal) - 2):
    if i == 5 or i == 15:
        tempstr = randtxt(i - 1) + ' '
        continue
    if i == 14:
        tempstr = randtxt(i - 1) + ','
        continue
    else:
        tempstr = randtxt(i)
        if i > 5:
            templist = list(tempstr)
            templist.insert(5, ' ')
            tempstr = fold(templist)
        if i > 15:
            templist = list(tempstr)
            templist.insert(14, ',')
            tempstr = fold(templist)
        if i > 15:
            templist = list(tempstr)
            templist.insert(15, ' ')
            tempstr = fold(templist)
    print(tempstr, end = '\r')
    sleep(0.1)

while total !=  strlist:
    print(fold(total), end = "\r")
    sleep(0.1)
    for i in range(0,len(strtotal)):
        if total[i]  ==  strlist[i] or not total[i].isalpha():
            continue
        else:
            total[i] = abc[randint(0,25)]
else:
    print(fold(total))