import solutionUtils
import random
import numpy as np
from typing import List

def missingElement(a: List[int]) -> int:
    n = a[-1]
    S = n * (n + 1) // 2
    actualSum = sum(a)
    element = S - actualSum

    return element

times = []
sizes = solutionUtils.generateSizes(10, 7)

for size in sizes:
    a = [number for number in range(size)]
    a.pop(random.randint(0, size))

    time = solutionUtils.measureTimeNanosMean(missingElement, a)
    times.append(time)

meanTime = np.mean(times)
print(meanTime)