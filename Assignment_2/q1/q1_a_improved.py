import time
import random
from matplotlib import pyplot as plt

currentTime = int(time.time())

seed = currentTime % 10000
k = 800000
L = []

def pseudo_rand_gen(seed, k):

    for i in range(k):
        
        square = str(seed * seed)
        square = square.zfill(8)
        square = square[3:7]

        seed = int(square)

        if seed in L:
            seed = (seed + int(time.time()) + i) % 10000 # Prevent repetition of seeds

        L.append(seed)

    return L

pseudo_rand_gen(seed, k)

plt.style.use('fivethirtyeight')
plt.title('Random Number Generator')
plt.xlabel('Ranges')
plt.ylabel('Number Count')

plt.hist(L, edgecolor="black")

plt.tight_layout()

plt.show()