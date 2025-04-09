import numpy as np
import random
import time

class Solution:
    @staticmethod
    def task1(arr):
        timeStartNumpy = time.time()

        maxMeanNumpy = np.max(np.mean(arr, axis=1))

        timeEndNumpy = time.time()

        print(f"Numpy: {maxMeanNumpy}")
        print(timeEndNumpy - timeStartNumpy)

        timeStartList = time.time()

        listArr = arr.tolist()

        maxMeanList = 0
        for row in listArr:
            maxMeanList = max(maxMeanList, sum(row) / len(row))

        timeEndList = time.time()

        print(f"List: {maxMeanList}")
        print(timeEndList - timeStartList)

    @staticmethod
    def task2(arr):
        timeStart = time.time()

        absSums = np.sum(np.abs(arr), axis=1)
        maxElem = np.max(arr[:, np.argmax(absSums)])

        timeEnd = time.time()

        print(maxElem)
        print(timeEnd - timeStart)

    @staticmethod
    def task3(arr):
        timeStart = time.time()

        minMean = np.min(np.mean(arr, axis=0))

        timeEnd = time.time()

        print(minMean)
        print(timeEnd - timeStart)

    @staticmethod
    def task4(arr):
        timeStart = time.time()

        meanRow = np.mean(arr, axis=1)
        meanColumn = np.mean(arr, axis=0)
        meanMatrix = np.mean(arr)

        timeEnd = time.time()

        print(meanRow, meanColumn, meanMatrix)
        print(timeEnd - timeStart)

    @staticmethod
    def task5(arr, subRows, subColumns, mult):
        timeStart = time.time()

        multSubMatrix = arr[:subRows, :subColumns] *= mult

        timeEnd = time.time()

        print(multSubMatrix)
        print(timeEnd - timeStart)

N = random.randint(1, 10000)
M = random.randint(1, 10000)
subRows = N - (10000 - N)
subColumns = M - (10000 - M)
multiplier = random.randint(1, 1000)
arr = np.random.randint(1, 1000, size=(N, M))
arrWithNeg = np.random.randint(-1000, 1000, size=(N, M))