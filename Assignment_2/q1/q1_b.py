import time
import random
from matplotlib import pyplot as plt

currentTime = int(time.time())

seed = currentTime % 10000
k = 800000
    
def pseudo_rand_gen(seed, k):
    L = []

    for i in range(k):
        
        square = str(seed * seed)
        square = square.zfill(8)
        square = square[3:7]

        seed = int(square)

        if seed in L:
            seed = (seed + int(time.time()) + i) % 10000 # Prevent repetition of seeds

        L.append(seed)

    return L

# -------------------------------------Estimating pi------------------------------------# 

def estimatingPi():
    l1 = pseudo_rand_gen(seed, k)
    x = []
    for i in l1:
        x.append(i / 10000)

    l2 = pseudo_rand_gen(seed, k)
    y = []
    for i in l2:
        y.append(i / 10000)

    circle = 0

    for i in range(k):
        if (x[i] ** 2 + y[i] ** 2) <= 1:
            circle += 1
    
    return 4 * circle / k

print(estimatingPi())

def estimatingPi2():
    x = [random.random() for _ in range(k)]
    y = [random.random() for _ in range(k)]

    circle = sum(1 for i in range(k) if (x[i] ** 2 + y[i] ** 2) <= 1)
    
    return 4 * circle / k

print(estimatingPi2())
