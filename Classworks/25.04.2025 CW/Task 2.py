import random
import solutionUtils
import numpy as np
from typing import List, Tuple

LIST_SIZE = 100

def closestSum(x: List[int], y: List[int], q: int) -> Tuple[int, int, int]:
    k = len(x)
    l = len(y)

    i = 0
    j = l - 1

    minDiff = float("inf")
    closeSum = 0
    bestI, bestJ = -1, -1

    while i < k and j >= 0:
        s = x[i] + y[j]
        diff = abs(s - q)

        if diff < minDiff:
            minDiff = diff
            closeSum = s
            bestI, bestJ = i, j

        if s < q:
            i += 1
        else:
            j -= 1

    return x[bestI], y[bestJ], closeSum

times = []
sizes = solutionUtils.generateSizes(10, 7)

for size in sizes:
    x = [random.randint(size, size * 10) for _ in range(LIST_SIZE)]
    y = [random.randint(size, size * 10) for _ in range(LIST_SIZE)]
    q = random.randint(size, size * 10)

    time = solutionUtils.measureTimeNanosMean(closestSum, x, y, q)
    times.append(time)

meanTime = np.mean(times)
print(meanTime)