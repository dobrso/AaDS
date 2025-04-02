import matplotlib.pyplot as plt
from solutionUtils import measureTimeNanosMean
import random

def binarySqrt(n):
    left = 0
    right = n

    while left <= right:
        mid = (left + right) // 2
        if mid **2 < n:
            left = mid + 1
        elif mid **2 > n:
            right = mid - 1
        else:
            return True

    return False

start = 1
end = 10_000
repeatTimes = 10

times = []
randomNumbers = sorted([random.randint(start, end) for _ in range(repeatTimes)])

for number in randomNumbers:
    time = measureTimeNanosMean(binarySqrt, number)
    times.append(time)

plt.figure(figsize=(12, 6))

plt.plot(randomNumbers, times, marker="o")

plt.xlabel("Числа")
plt.ylabel("Время выполнения (в наносекундах)")

plt.title("Зависимость времени выполнения от входных данных")
plt.grid(True)

plt.xscale("log")
plt.yscale("log")

plt.show()