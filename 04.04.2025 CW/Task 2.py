import random
import matplotlib.pyplot as plt
from solutionUtils import measureTimeNanosMean, generateSizes, primeDivisors

def gcdEuclid(a: int, b: int) -> int:
    aDivs = primeDivisors(a)
    bDivs = primeDivisors(b)

    commonDivs = set(aDivs).intersection(set(bDivs))

    gcd = 1
    for div in commonDivs:
        aPower = 0
        while a % div == 0:
            a = a // div
            aPower += 1
        bPower = 0
        while b % div == 0:
            b = b // div
            bPower += 1
        minPower = min(aPower, bPower)
        gcd *= div ** minPower

    return gcd

def damagedTiles(N: int, M:int) -> int:
    return N + M - gcdEuclid(N, M)

times = []
sizes = generateSizes(10, 7)

for size in sizes:
    randomN = random.randint(size, size * 10)
    randomM = random.randint(size, size * 10)
    time = measureTimeNanosMean(damagedTiles, randomN, randomM)

    times.append(time)

plt.figure(figsize=(12, 6))

plt.plot(sizes, times, marker="o")

plt.xlabel("Числа")
plt.ylabel("Время выполнения (в наносекундах)")

plt.title("Зависимость времени выполнения от входных данных")
plt.grid(True)

plt.xscale("log")
plt.yscale("log")

plt.show()