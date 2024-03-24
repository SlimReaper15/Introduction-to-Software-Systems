import time
from matplotlib import pyplot as plt

currentTime = int(time.time())
seed = currentTime % 10000
k = 100
L = []

def pseudo_rand_gen(seed, k):
    while (k > 0):
        square = str(seed * seed)
        
        if len(square) < 8:
            square = square.zfill(8)

        square = square[3:7]
        L.append(int(square))
        seed = int(square)

        k -= 1

pseudo_rand_gen(seed, k)
print(L)

plt.style.use('fivethirtyeight')
plt.title('Random Number Generator')
plt.xlabel('Ranges')
plt.ylabel('Number Count')

plt.hist(L, edgecolor="black")

plt.tight_layout()

plt.show()