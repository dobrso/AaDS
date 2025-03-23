import numpy as np
import matplotlib.pyplot as plt
from solutionUtils import measureTime, generateSizes

"""
Выполнить обработку элементов матрицы А, имеющей N строк и М столбцов.
Определить средние значения по всем строкам, столбцам матрицы и по всей матрицы. 
Запустить с разной размерностью матрицы и замерить время выполнения программы (среднее, максимальное, минимальное). 
Построить графики.
"""

def calculateMatrixMean(matrix):
    matrixMean = np.mean(matrix)
    rowMean = np.mean(matrix, axis=1)
    columnMean = np.mean(matrix, axis=0)
    return (matrixMean, rowMean, columnMean)

timesMean = []
timesMin = []
timesMax = []

sizes = generateSizes(10, 5)

for size in sizes:
    arr = np.random.randint(1, 1000, size=(size, size))

    meanTime, minTime, maxTime = measureTime(calculateMatrixMean, arr)
    timesMean.append(meanTime)
    timesMin.append(minTime)
    timesMax.append(maxTime)

    print(f"Размер матрицы: {size}X{size}")
    print(f"Среднее время выполнения: {meanTime}")
    print(f"Минимальное время выполнения: {minTime}")
    print(f"Максимальное время выполнения: {maxTime}")
    print()

plt.figure(figsize=(10, 6))

plt.plot(sizes, timesMean, label="Numpy массив", marker="o")

plt.xlabel("Размер матрицы (NxN)")
plt.ylabel("Время выполнения (в секундах)")

plt.title("Зависимость времени выполнения от размера матрицы")
plt.legend()
plt.grid(True)

plt.xscale("log")
plt.yscale("log")

plt.show()