import numpy as np
import pandas as pd
import sys
import json

# Wywołanie: python ShannonFano_decoder.py plik_wejsciowy.SF.01 plik_wyjsciowy.8bit.01

def dekoder(nazwa, nazwa2):
    with open("SF.codes.txt") as f:
        data = json.loads(f.read())
    f = open(nazwa, "r")
    tekst = ''
    kod = {y:x for x,y in data.items()}
    for line in f:
        tekst += line
    dlugosc = 0
    start = 0
    found = 0
    odkodowany = ''
    while start < len(tekst):
        dlugosc = 0
        found = 0
        while not found:
            dlugosc += 1
            koniec = start + dlugosc
            slowo = tekst[start:koniec]
            if slowo in kod.keys():
                odkodowany += kod[slowo]
                found = 1
        start += dlugosc
    #print(start)
    #print(odkodowany)
    e = open(nazwa2, "w")
    e.write(odkodowany)
dekoder(sys.argv[1], sys.argv[2])
