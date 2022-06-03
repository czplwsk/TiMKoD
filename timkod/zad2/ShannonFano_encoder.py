import numpy as np
import pandas as pd
import sys
import json
from copy import deepcopy


def suma(rozklad):
    suma = 0
    for i in rozklad:
        suma += rozklad[i]
    return suma

def podziel(rozklad):
    l = dict()
    p = deepcopy(rozklad)
    poprzednia = 0
    for i in rozklad.keys():
        if suma(l) > suma(p):
            break
        if len(p) == 1:
            break
        poprzednia = suma(p) - suma(l)
        item = i
        l[item] = p.pop(item)

    if suma(l)-suma(p) > poprzednia:
        p[item] = l.pop(item)
        p = dict(sorted(p.items(), key=lambda item: item[1], reverse=True))

    return l, p

def drzewo(arr, code):
    kody = dict()
    if(len(arr)==1):
        kody[list(arr.keys())[0]] = code
    else:
        arr, arr2 = podziel(arr)
        l = drzewo(arr, code + '0')
        p = drzewo(arr2, code + '1')
        kody.update(l)
        kody.update(p)
    return kody

def zapisz_kod(kod):
    f = open("SF.codes.txt", "w")
    f.write(json.dumps(kod))

def koder(name, name2):
    f = open(name, "r", errors='ignore')
    slowa = []
    lines = f.readlines()
    for line in lines:
        pos = 0
        while pos<len(line):
            # pos+=8
            # slowa.append(line[pos-8 : pos])
            slowa.append(line[pos])
            pos+=1



    rozklad = dict()
    for s in slowa:
        if s in rozklad.keys():
            rozklad[s] += 1
        else:
            rozklad[s] = 1

    for s in rozklad.keys():
        rozklad[s] = rozklad[s]/len(slowa)

    rozklad = dict(sorted(rozklad.items(), key=lambda item: item[1], reverse=True))
    kody = drzewo(rozklad, '')
    zapisz_kod(kody)
    zakodowane = [kody[slowo] for slowo in slowa]
    e = open(name2, "w")
    e.write(''.join(zakodowane))
    return


koder(sys.argv[1], sys.argv[2])
