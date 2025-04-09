import numpy as np
import matplotlib.pyplot as plt
from solutionUtils import measureTime, generateSizes

"""
Выполнить обработку элементов матрицы А, имеющей N строк и М столбцов.
Найти наименьший элемент строки матрицы А, для которого сумма абсолютных значений элементов максимальна (np.argmax и np.min). 
Сделать с помощью numpy (mean и max) и без него. 
Запустить с разной размерностью матрицы и замерить время выполнения программы (среднее, максимальное, минимальное). 
Построить графики.
"""

def calculateMinElementNumpy(matrix):
    absSums = np.sum(np.abs(matrix), axis=1)
    minElement = np.min(matrix[np.argmax(absSums)])
    return minElement

def calculateMinElementList(matrix):
    maxSum = -1
    maxSumRow = -1
    for i, row in enumerate(matrix):
        rowSum = sum(abs(x) for x in row)
        if rowSum > maxSum:
            maxSum = rowSum
            maxSumRow = i
    minElement = min(matrix[maxSumRow])
    return minElement

timesNumpyMean = []
timesNumpyMin = []
timesNumpyMax = []

timesListMean = []
timesListMin = []
timesListMax = []

sizes = generateSizes(10, 5)

for size in sizes:
    arr = np.random.randint(-100, 100, size=(size, size))
    arrList = arr.tolist()

    meanNumpyTime, minNumpyTime, maxNumpyTime = measureTime(calculateMinElementNumpy, arr)
    timesNumpyMean.append(meanNumpyTime)
    timesNumpyMin.append(minNumpyTime)
    timesNumpyMax.append(maxNumpyTime)

    meanListTime, minListTime, maxListTime = measureTime(calculateMinElementList, arr)
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
