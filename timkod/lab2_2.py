import numpy as np
import matplotlib.pyplot as plt



def rozklad_warunkowy(name):
    f = open(name, "r")
    dziedzina = set()
    array = []
    for line in f:
        for i in range(len(line)-1):
            array.append(line[i]+line[i+1])
            dziedzina.add(line[i]+line[i+1])

    slownik = dict(zip(dziedzina,[0 for i in dziedzina]))
    slownik = dict( sorted(slownik.items(), key=lambda x: x[0].lower()) )
    dziedzina = sorted(dziedzina, key=lambda x: x[0].lower())
    for i in array:
        if i in dziedzina:
            slownik[i] = slownik[i]+1
    print(slownik)
    #plt.bar(slownik.keys(), slownik.values(), 1.0, color='g')
    #plt.show()
    #plt.hist(array, len(dziedzina))
    plt.bar(slownik.keys(), slownik.values())
    plt.show()

    for l in slownik.keys():
        l[0]
rozklad_warunkowy("norm_romeo.txt")
