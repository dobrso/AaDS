import random
import solutionUtils
import numpy as np
from typing import List, Union, Tuple

LIST_SIZE = 100

def findLeftBound(arr: List[int], a: int) -> int:
    left = 0
    right = len(arr) - 1

    low = 0

    while left <= right:
        mid = (left + right) // 2
        element = arr[mid]

        if element < a:
            left = mid + 1
        elif element > a:
            right = mid - 1
        else:
            low = mid
            right = mid - 1

    return low

def findRightBound(arr: List[int], a: int) -> int:
    left = 0
    right = len(arr) - 1

    high = 0

    while left <= right:
        mid = (left + right) // 2
        element = arr[mid]

        if element < a:
            left = mid + 1
        elif element > a:
            right = mid - 1
        else:
            high = mid
            left = mid + 1

    return high

def findBounds(arr: List[int], a: int) -> Union[int, Tuple[int, int]]:
    low = findLeftBound(arr, a)
    high = findRightBound(arr, a)

    return 0 if (low, high) == (0, 0) else (low, high)

times = []
sizes = solutionUtils.generateSizes(10, 7)

for size in sizes:
    arr = sorted([random.randint(size, size * 10) for _ in range(LIST_SIZE)])
    a = random.randint(size, size * 10)

    time = solutionUtils.measureTimeNanosMean(findBounds, arr, a)
    times.append(time)

meanTime = np.mean(times)
print(meanTime)