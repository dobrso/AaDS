import matplotlib.pyplot as plt
import random
import solutionUtils

def modCount(a: int, b: int, p: int) -> int:
    count = 0
    for c in range(1, p):
        if a == (b * c) % p:
            count += 1

    return count

times = []
sizes = solutionUtils.generateSizes(10, 7)

for size in sizes:
    a = random.randint(1, size)
    b = random.randint(1, size)
    p = size

    time = solutionUtils.measureTimeNanosMean(modCount, a, b, p)
    times.append(time)

plt.figure(figsize=(12, 6))

plt.plot(sizes, times, marker="o")

plt.xlabel("Размер чисел")
plt.ylabel("Время выполнения (в наносекундах)")

plt.title("Зависимость времени выполнения от входных данных")
plt.grid(True)

plt.xscale("log")
plt.yscale("log")

plt.show()