import random

def findPi(n) :
    count = 0
    for i in range (n) :
        x,y = random.uniform(0,1), random.uniform(0,1)
        if (x**2 + y**2)**0.5 <= 1 :
            count += 1
    return 4 * count/n

print (findPi(100000))