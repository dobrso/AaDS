import numpy as np
import matplotlib.pyplot as plt
from solutionUtils import measureTimeMeanTwoArgs, generateSizes

"""
Нахождение пересечения двух списков
-   С использованием множества: Преобразовать оба списка в множества и найти пересечение.
    Сложность: O(n + m), где n и m — размеры списков.
-   Без множества: Для каждого элемента из первого списка проверять, есть ли он во втором списке.
    Сложность: O(n * m)
"""

def intersectionWithSets(listFirst, listSecond):
    setFirst = set(listFirst)
    setSecond = set(listSecond)
    return setFirst.intersection(setSecond)

def intersectionWithoutSets(listFirst, listSecond):
    return [element for element in listFirst if element in listSecond]

sizes = generateSizes(10, 5)
timesSet = []
timesNaive = []

for size in sizes:
    arrFirst = list(np.random.randint(0, size, size))
    arrSecond = list(np.random.randint(0, size, size))

    timeSet = measureTimeMeanTwoArgs(intersectionWithSets, arrFirst, arrSecond)
    timesSet.append(timeSet)

    timeNaive = measureTimeMeanTwoArgs(intersectionWithoutSets, arrFirst, arrSecond)
    timesNaive.append(timeNaive)

plt.figure(figsize=(12, 7))
plt.plot(sizes, timesSet, label="Множество (O(n + m))", marker="o", color="green")
plt.plot(sizes, timesNaive, label="Двойной цикл (O(n * m))", marker="s", color="red")

plt.title("Сравнение времени нахождения пересечения")
plt.xlabel("Размер списка")
plt.ylabel("Время выполнения (секунды)")
plt.xscale("linear")
plt.yscale("linear")
plt.grid(True, which="both", linestyle="--")
plt.legend()
plt.show()