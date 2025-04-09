import random
import matplotlib.pyplot as plt
from solutionUtils import measureTimeNanos, generateSizes

def binaryGCD(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    shift = 0

    while (a & 1) == 0 and (b & 1) == 0:
        a >>= 1
        b >>= 1
        shift += 1

    while a != b:
        if a < b:
            a, b = b, a

        if (a & 1) == 0:
            a >>= 1
        elif (b & 1) == 0:
            b >>= 1
        else:
            a = (a - b) >> 1

    return a << shift

timesMean = []
timesMin = []
timesMax = []

sizes = generateSizes(10, 7)

for size in sizes:
    a = random.randint(size//2, size)
    b = random.randint(size//2, size)

    timeMean, timeMin, timeMax = measureTimeNanos(binaryGCD, a, b, repeatTimes=10)

    timesMean.append(timeMean)
    timesMin.append(timeMin)
    timesMax.append(timeMax)

plt.figure(figsize=(10, 6))

plt.plot(sizes, timesMean, label="Среднее", marker="o")
plt.plot(sizes, timesMin, label="Минимальное", marker="s")
plt.plot(sizes, timesMax, label="Максимальное", marker="^")

plt.xlabel("Размер чисел")
plt.ylabel("Время выполнения (в наносекундах)")

plt.title("Бинарный алгоритм")
plt.legend()
plt.grid(True)

plt.xscale("log")
plt.yscale("log")

plt.show()