import matplotlib.pyplot as plt
import random
from solutionUtils import measureTimeNanosMean, generateSizes

def flooringSqrt(x: int) -> int:
    left = 0
    right = x
    while left <= right:
        mid = (left + right) // 2

        if mid **2 == x:
            return mid
        elif mid **2 < x:
            left = mid + 1
        else:
            right = mid - 1

    return right

times = []
sizes = generateSizes(10, 7)

for size in sizes:
    randomNumber = random.randint(size, size * 10)
    time = measureTimeNanosMean(flooringSqrt, randomNumber)
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