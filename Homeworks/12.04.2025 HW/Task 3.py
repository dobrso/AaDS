import solutionUtils
import random
import matplotlib.pyplot as plt

def removeDuplicates(lst: list) -> list:
    uniqueList = list(set(lst))
    return uniqueList

times = []
sizes = solutionUtils.generateSizes(10, 7)

for size in sizes:
    lst = sorted([random.randint(1, size) for _ in range(100)])

    time = solutionUtils.measureTimeNanosMean(removeDuplicates, lst, repeatTimes=10)
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