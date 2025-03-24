import numpy as np
import matplotlib.pyplot as plt
from solutionUtils import measureTimeMean, generateSizes

"""
Нахождение двух чисел, сумма которых равна целевому значению
-   С использованием множества: Преобразовать список в множество и для каждого элемента искать его дополнение.
    Сложность: O(n)
-   Без множества: Пройтись по всем возможным парам чисел.
    Сложность: O(n^2)
"""

targetSum = 100

def targetSumWithSet(lst, target):
    uniqueLst = set(lst)
    for element in uniqueLst:
        complement = target - element
        if complement in uniqueLst and element != complement:
            return (element, complement)

def targetSumWithoutSet(lst, target):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if (lst[i] + lst[j]) == target:
                return (lst[i], lst[j])

sizes = generateSizes(10, 5)
timesSet = []
timesNaive = []

for size in sizes:
    arr = list(np.random.randint(0, size, size))

    timeSet = measureTimeMean(targetSumWithSet, arr, targetSum)
    timesSet.append(timeSet)

    timeNaive = measureTimeMean(targetSumWithoutSet, arr, targetSum)
    timesNaive.append(timeNaive)

plt.figure(figsize=(12, 7))
plt.plot(sizes, timesSet, label="Множество (O(n))", marker="o", color="green")
plt.plot(sizes, timesNaive, label="Двойной цикл (O(n^2))", marker="s", color="red")

plt.title("Сравнение времени нахождения целевой суммы")
plt.xlabel("Размер списка")
plt.ylabel("Время выполнения (секунды)")
plt.xscale("linear")
plt.yscale("linear")
plt.grid(True, which="both", linestyle="--")
plt.legend()
plt.show()