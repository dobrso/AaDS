import numpy as np
import matplotlib.pyplot as plt
from solutionUtils import measureTimeMeanOneArg, generateSizes

"""
Удаление всех дубликатов из списка
-   С использованием множества: Преобразовать список в множество и обратно в список.
    Сложность: O(n)
-   Без множества: Пройтись по списку и добавлять в новый список только уникальные элементы.
    Сложность: O(n^2)
"""

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

    timeSet = measureTimeMeanOneArg(removeDuplicatesWithSet, arr)
    timesSet.append(timeSet)

    timeNaive = measureTimeMeanOneArg(removeDuplicatesWithoutSet, arr)
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