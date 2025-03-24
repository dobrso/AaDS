import time
import numpy as np

def measureTime(func, *args, repeatTimes=5):
    times = []

    for i in range(repeatTimes):
        timeStart = time.time()
        result = func(*args)
        timeEnd = time.time()
        times.append(timeEnd - timeStart)

    return np.mean(times), np.min(times), np.max(times)

def measureTimeMean(func, *args, repeatTimes=5):
    times = []

    for i in range(repeatTimes):
        timeStart = time.time()
        func(*args)
        timeEnd = time.time()

        times.append(timeEnd - timeStart)

    return np.mean(times)

def generateSizes(base, lenOfSizes):
    return [base **i for i in range(1, lenOfSizes)]

def bubbleSort(arg):
    for i in range(0, len(arg)):
        for j in range(0, len(arg) - 1 - i):
            if arg[j] > arg[j+1]:
                arg[j], arg[j+1] = arg[j+1], arg[j]
    return arg

def isPrime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n **0.5) + 1))

def primeDivisors(n):
    divs = []

    for i in range(2, int(n **0.5) + 1):
        if n % i == 0:
            if isPrime(i):
                divs.append(i)
            if isPrime(n // i):
                divs.append(n // i)

    return sorted(divs)