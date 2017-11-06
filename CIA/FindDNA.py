# -*- coding: utf-8 -*-
dna= open("dna.txt", "r")
F=dna.read()
dna.close()
seznam=[]
print("Hair color: ")
dnalas=["CCAGCAATCGC", "GCCAGTGCCG", "TTAGCTATCGC"]
barvalas =["Črna", "Rjava", "Svetlolasa"]
x=0
for i in dnalas:
    if i in F:
        print(barvalas[x])
        seznam.append(barvalas[x])
    x += 1


print("Oblika obraza: ")
oblika=["GCCACGG", "ACCACAA", "AGGCCTCA"]
obraz =["Kvadratna", "Okrogla" , "Ovalna"]
x=0
for i in oblika:
    if i in F:
        print(obraz[x])
        seznam.append(obraz[x])
    x += 1


print("Barva oči: ")
barva=["TTGTGGTGGC", "GGGAGGTGGC", "AAGTAGTGAC"]
oci =["Modra", "Zelena" , "Rjava"]
x=0
for i in barva:
    if i in F:
        print(oci[x])
        seznam.append(oci[x])
    x += 1



print("Spol: ")
spol=["TGAAGGACCTTC", "TGCAGGAACTTC"]
spol1 =["Ženska", "Moški"]
x=0
for i in spol:
    if i in F:
        print(spol1[x])
        seznam.append(spol1[x])
    x += 1


print("Rasa: ")
rasa=["AAAACCTCA", "CGACTACAG", "CGCGGGCCG"]
rasa1 =["Bela", "Črna", "Azijska"]
x=0
for i in rasa:
    if i in F:
        print(rasa1[x])
        seznam.append(rasa1[x])
    x += 1


print(seznam)

Eva=["Svetlolasa", "Ovalna", "Modra", "Ženska", "Bela"]
Larisa=["Rjava", "Ovalna", "Rjava", "Ženska", "Bela"]
Matej=["Črna", "Ovalna", "Modra", "Moški", "Bela"]
Miha=["Rjava", "Kvadratna", "Zelena", "Moški", "Bela"]

x=0
for i in Eva:
    if i == seznam[x]:

        x += 1
    else:
        break
    if x==5:
       print("Eva")

x=0
for i in Larisa:
    if i == seznam[x]:

        x += 1
    else:
       break
    if x==5:
       print("Larisa")

x=0
for i in Matej:
    if i == seznam[x]:

        x += 1
    else:
        break
    if x==5:
       print("Matej")


x=0
for i in Miha:
    if i == seznam[x]:

        x += 1
    else:
       break
    if x == 5:
       print("Miha")



