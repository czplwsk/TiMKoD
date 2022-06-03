import numpy as np
import matplotlib.pyplot as plt



def histogram(name):
    f = open(name, "r")
    dziedzina = set()
    array = []
    for line in f:
        for p in line:
            array.append(p)
            dziedzina.add(p)

    print(dziedzina)

    slownik = dict(zip(dziedzina,[0 for i in dziedzina]))

    for i in array:
        if i in dziedzina:
            slownik[i] = slownik[i]+1
    print(slownik)
    plt.bar(slownik.keys(), slownik.values(), 1.0, color='g')
    plt.show()

histogram("losowe.txt")
