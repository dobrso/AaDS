import random
import matplotlib.pyplot as plt
from solutionUtils import measureTimeNanos, generateSizes, primeDivisors

def gcdEuclid(a, b):
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

timesMean = []
timesMin = []
timesMax = []

sizes = generateSizes(10, 7)

for size in sizes:
    a = random.randint(size//2, size)
    b = random.randint(size//2, size)

    timeMean, timeMin, timeMax = measureTimeNanos(gcdEuclid, a, b, repeatTimes=10)

    timesMean.append(timeMean)
    timesMin.append(timeMin)
    timesMax.append(timeMax)

plt.figure(figsize=(10, 6))

plt.plot(sizes, timesMean, label="Среднее", marker="o")
plt.plot(sizes, timesMin, label="Минимальное", marker="s")
plt.plot(sizes, timesMax, label="Максимальное", marker="^")

plt.xlabel("Размер чисел")
plt.ylabel("Время выполнения (в наносекундах)")

plt.title("Алгоритм Евклида")
plt.legend()
plt.grid(True)

plt.xscale("log")
plt.yscale("log")

plt.show()