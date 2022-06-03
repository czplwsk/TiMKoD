import random

def generate_random(name, v, dziedzina, wagi):
    f = open(name, 'w')
    for i in range(v):
        r = random.randint(0,9)/10
        thresh = -1
        while r>=0:
            thresh += 1
            r = r-wagi[thresh]
        f.write(dziedzina[thresh])
generate_random("losowe.txt", 1000, ['a','b','c','d','e'],[0.1,0.3,0.2,0.2,0.2])
