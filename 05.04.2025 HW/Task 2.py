import matplotlib.pyplot as plt
import solutionUtils

def grayCode(n: int) -> list:
    return [(x ^ (x >> 1)) for x in range(2 **n)]

times = []
sizes = list(range(1, 21))

for size in sizes:
    time = solutionUtils.measureTimeMean(grayCode, size)
    times.append(time)

plt.figure(figsize=(12, 6))

plt.plot(sizes, times, marker="o")

plt.xlabel("Размер чисел")
plt.ylabel("Время выполнения (в секундах)")

plt.title("Зависимость времени выполнения от входных данных")
plt.grid(True)

plt.xscale("linear")
plt.yscale("linear")

plt.show()