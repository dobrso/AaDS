import numpy as np


def countDistinct(x: np.ndarray) -> int:
    n = len(x)
    x.sort()

    distinctCount = 1
    for i in range(2, n):
        if x[i] != x[i-1]:
            distinctCount += 1

    return distinctCount


x = np.random.randint(1, 20, 10)
print(countDistinct(x))