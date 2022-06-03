
__author__      = "Eliza Czaplewska"

import numpy as np
import pandas as pd
import sys
import random

def losuj(dlugosc, litery):
    str = ''
    for i in range(dlugosc):
        str += random.choice(litery)
    return str

def prawdopodobienstwa(f):
    raw_data = []
    licznik = dict()
    litery = list(f)
    for i in range(len(litery)-2):
        raw_data.append(''.join(litery[i:i+3]))
    dziedzina = np.array([[word[0:2], word[2]] for word in raw_data])
    for inst in dziedzina[:,0]:
        licznik[inst] = dict()

    for pref, lit in dziedzina:
        if lit in licznik[pref].keys():
            licznik[pref][lit] += 1
        else:
            licznik[pref][lit] = 1
    licznik = dict(sorted(licznik.items()))

    return licznik, litery

def generator(dlugosc, rozklad2D, litery):
    str = losuj(2, litery)
    dlugosc -= 2
    while(dlugosc):
        ostatnie_litery = str[-2:]
        if ostatnie_litery in rozklad2D.keys():
            litera = random.choices(list(rozklad2D[ostatnie_litery].keys()), weights = list(rozklad2D[ostatnie_litery].values()))[0]
        else :
            litera = losuj(1, litery)
        str += litera
        dlugosc -= 1
    return str

f1 = open(sys.argv[1], "r").read()
f2 = open(sys.argv[3], "w")
rozklad, litery = prawdopodobienstwa(f1)
str = generator(int(sys.argv[2]), rozklad, litery)
f2.write(str)
f2.close()
