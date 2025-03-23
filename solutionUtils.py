import time
import numpy as np

def measureTime(func, arg, repeatTimes=5):
    times = []

    for i in range(repeatTimes):
        timeStart = time.time()
        result = func(arg)
        timeEnd = time.time()
        times.append(timeEnd - timeStart)

    return np.mean(times), np.min(times), np.max(times)

def measureTimeMeanOneArg(func, arg, repeatTimes=5):
    times = []

    for i in range(repeatTimes):
        timeStart = time.time()
        func(arg)
        timeEnd = time.time()

        times.append(timeEnd - timeStart)

    return np.mean(times)

def measureTimeMeanTwoArgs(func, argFirst, argSecond, repeatTimes=5):
    times = []

    for i in range(repeatTimes):
        timeStart = time.time()
        func(argFirst, argSecond)
        timeEnd = time.time()

        times.append(timeEnd - timeStart)

    return np.mean(times)

def measureTimeMeanTargetSumArg(func, arg, argTarget, repeatTimes=5):
    times = []

    for i in range(repeatTimes):
        timeStart = time.time()
        func(arg, argTarget)
        timeEnd = time.time()

        times.append(timeEnd - timeStart)

    return np.mean(times)

def generateSizes(base, lenOfSizes):
    return [base **i for i in range(1, lenOfSizes)]