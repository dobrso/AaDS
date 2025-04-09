import numpy as np
import matplotlib.pyplot as plt
from solutionUtils import measureTimeMean, generateSizes

"""
Нахождение первого повторяющегося элемента в списке
-   С использованием множества: Пройтись по списку и использовать множество для отслеживания встречающихся элементов. 
    Сложность: O(n)
-   Без множества: Пройтись по всем парам элементов и найти повторяющийся элемент.
    Сложность: O(n^2)
"""

def firstDuplicateWithSet(lst):
    uniqueElements = set()
    for element in lst:
        if element in uniqueElements:
            return element
        uniqueElements.add(element)

def firstDuplicateWithoutSet(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                return lst[i]

sizes = generateSizes(10, 5)
timesSet = []
timesNaive = []

for size in sizes:
    arr = list(np.random.randint(0, size, size))

    timeSet = measureTimeMean(firstDuplicateWithSet, arr)
    timesSet.append(timeSet)

    timeNaive = measureTimeMean(firstDuplicateWithoutSet, arr)
    timesNaive.append(timeNaive)

plt.figure(figsize=(12, 7))
plt.plot(sizes, timesSet, label="Множество (O(n))", marker="o", color="green")
plt.plot(sizes, timesNaive, label="Двойной цикл (O(n^2))", marker="s", color="red")

plt.title("Сравнение времени нахождения первого повторяющегося элемента")
plt.xlabel("Размер списка")
plt.ylabel("Время выполнения (секунды)")
plt.xscale("linear")
plt.yscale("linear")
plt.grid(True, which="both", linestyle="--")
plt.legend()
plt.show()