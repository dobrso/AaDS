import numpy as np
import matplotlib.pyplot as plt
from solutionUtils import measureTime, generateSizes

"""
Выполнить обработку элементов матрицы А, имеющей N строк и М столбцов. 
Найти наибольшее значение среди средних значений для каждой строки матрицы. 
Сделать с помощью numpy (mean и max) и без него. 
Запустить с разной размерностью матрицы и замерить время выполнения программы (среднее, максимальное, минимальное). 
Построить графики.
"""

def calculateMeanNumpy(matrix):
    maxMean = np.max(np.mean(matrix, axis=1))
    return maxMean

def calculateMeanList(matrix):
    maxMean = 0
    for row in matrix:
        maxMean = max(maxMean, sum(row) / len(row))
    return maxMean

timesNumpyMean = []
timesNumpyMin = []
timesNumpyMax = []

timesListMean = []
timesListMin = []
timesListMax = []

sizes = generateSizes(10, 5)

for size in sizes:
    arr = np.random.randint(1, 1000, size=(size, size))
    arrList = arr.tolist()

    meanNumpyTime, minNumpyTime, maxNumpyTime = measureTime(calculateMeanNumpy, arr)
    timesNumpyMean.append(meanNumpyTime)
    timesNumpyMin.append(minNumpyTime)
    timesNumpyMax.append(maxNumpyTime)

    meanListTime, minListTime, maxListTime = measureTime(calculateMeanList, arrList)
    timesListMean.append(meanListTime)
    timesListMin.append(minListTime)
    timesListMax.append(maxListTime)

    print(f"Размер матрицы: {size}X{size}")
    print(f"Среднее время выполнения: {meanNumpyTime}")
    print(f"Минимальное время выполнения: {minNumpyTime}")
    print(f"Максимальное время выполнения: {maxNumpyTime}")
    print()

    print(f"Среднее время выполнения: {meanListTime}")
    print(f"Минимальное время выполнения: {minListTime}")
    print(f"Максимальное время выполнения: {maxListTime}")
    print()

plt.figure(figsize=(10, 6))

plt.plot(sizes, timesNumpyMean, label="Numpy массив", marker="o")
plt.plot(sizes, timesListMean, label="Список", marker="o")

plt.xlabel("Размер матрицы (NxN)")
plt.ylabel("Время выполнения (в секундах)")

plt.title("Зависимость времени выполнения от размера матрицы")
plt.legend()
plt.grid(True)

plt.xscale("log")
plt.yscale("log")

plt.show()