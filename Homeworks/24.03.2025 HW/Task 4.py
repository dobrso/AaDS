import numpy as np
import matplotlib.pyplot as plt
from solutionUtils import measureTimeMean, generateSizes

def removeDuplicatesWithSet(lst):
    return list(set(lst))

def removeDuplicatesWithoutSet(lst):
    uniqueElements = []

    for element in lst:
        if element not in uniqueElements:
            uniqueElements.append(element)

    return uniqueElements

sizes = generateSizes(10, 5)
timesSet = []
timesNaive = []

for size in sizes:
    arr = list(np.random.randint(0, size, size))

    timeSet = measureTimeMean(removeDuplicatesWithSet, arr)
    timesSet.append(timeSet)

    timeNaive = measureTimeMean(removeDuplicatesWithoutSet, arr)
    timesNaive.append(timeNaive)

plt.figure(figsize=(12, 7))
plt.plot(sizes, timesSet, label="Множество (O(n))", marker="o", color="green")
plt.plot(sizes, timesNaive, label="Двойной цикл (O(n^2))", marker="s", color="red")

plt.title("Сравнение времени удаления дубликатов")
plt.xlabel("Размер списка")
plt.ylabel("Время выполнения (секунды)")
plt.xscale("linear")
plt.yscale("linear")
plt.grid(True, which="both", linestyle="--")
plt.legend()
plt.show()