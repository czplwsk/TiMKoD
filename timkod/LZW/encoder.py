import numpy as np
import sys
import json
import math

def encoder_LZW(inFile, outFile):
    f = open(inFile, "r")
    i = 0
    tekst = []
    slownik = dict()
    # for line in f:
    #     pos = 0
    #     while pos<len(line):
    #         pos+=8
    #         znak = line[pos-8 : pos]
    #         tekst.append(znak)
    #         if znak not in slownik.keys():
    #             #slownik.update({znak:format(len(slownik), "0" + str(n) +"b")})
    #             slownik.update({znak:""})
    for line in f:
        pos = 0
        while pos<len(line):
            znak = line[pos]
            tekst.append(znak)
            if znak not in slownik.keys():
                #slownik.update({znak:format(len(slownik), "0" + str(n) +"b")})
                slownik.update({znak:""})
            pos+=1

    dlugosc = len(tekst)
    out=[]
    temp = ''
    while True:
        if(i>=dlugosc):
            if temp != '':
                out.append(temp)
            break
        temp += tekst[i]
        if temp in slownik:
            i+=1
        else:
            out.append(temp[:-1])
#            slownik.update({temp:format(len(slownik), "0" + str(n) +"b")})
            slownik.update({znak:""})
            temp = ''
    nbits = math.ceil(math.log(len(slownik),2))
    print(nbits)
    indices=range(len(slownik))
    print(indices)
    indices = [format(x,"0" + str(nbits) +"b") for x in indices]
    slownik2 = dict(zip(slownik.keys(),indices))
    slownik.update(slownik2)
    slownik.update({'nbits':nbits})
    out = [slownik.get(x) for x in out]
    e = open(outFile, "w")
    e.write(''.join(out)+'\n')
    e.write(json.dumps(slownik))

encoder_LZW(sys.argv[1],sys.argv[2])
