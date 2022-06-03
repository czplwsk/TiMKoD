import numpy as np
import pandas as pd
import random


def losuj(dlugosc, litery):
    str = ''
    for i in range(dlugosc):
        str += random.choice(litery)
    return str

def hist():
    return


def prawdopodobienstwa(f):
    raw_data = []
    licznik = dict()

    for line in f:
        for i in range(len(line)-2):
            raw_data.append(line[i:i+3])

    dziedzina = np.array([[word[0:2], word[2]] for word in raw_data])

    for inst in dziedzina[:,0]:
        licznik[inst] = dict()

    for pref, lit in dziedzina:
        if lit in licznik[pref].keys():
            licznik[pref][lit] += 1
        else:
            licznik[pref][lit] = 1

    licznik = dict(sorted(licznik.items()))

    for pref in licznik:
        suma = sum(licznik[pref].values())
        licznik[pref].update((x, y/suma) for x, y in licznik[pref].items())

    return licznik

def generator(dlugosc, rozklad2D, litery):
    str = losuj(2, litery)
    dlugosc -= 2
    while(dlugosc):
        ostatnie_litery = str[-2:]
        if ostatnie_litery in rozklad2D.keys():
            litera = random.choice(rozklad2D[ostatnie_litery].keys(), rozklad2D[ostatnie_litery].values())
        else :
            return



        dlugosc -= 1

    return 0

f = open("norm_wiki_sample.txt", "r")
litery = list(f.read())
rozklad2D = prawdopodobienstwa(f)
print(losuj(2, litery))
print(rozklad2D)
