import numpy as np
import sys
import json

'''
Niestety mój poprzedni kompresor miał ustawioną domyślną długość słowa w słowniku na
8 bitów. Zmieniłam to i teraz ta wielkość jest dopasowywana do długości tekstu.
'''

def decompress_LZW(inFile, outFile):
    f = open(inFile, "r")
    tekst = f.readline()
    slownik = json.loads(f.readline())
    nbits = slownik.get("nbits")
    tekst = [tekst[i:i+nbits] for i in range(0, len(tekst), nbits)]
    tekst = tekst[:-1]
    slownik = dict((y,x) for x,y in slownik.items())
    decompressed = [slownik.get(i) for i in tekst]
    e = open(outFile, "w")
    e.write(''.join(decompressed))

decompress_LZW(sys.argv[1],sys.argv[2])
