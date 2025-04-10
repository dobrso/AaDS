import numpy as np
from numpy import ndarray

def nearestSmallElements(arr: ndarray) -> ndarray:
    n = len(arr)
    result = np.zeros(n)
    stack = []

    for i in range(n):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()

        result[i] = stack[-1] + 1 if stack else 0
        stack.append(i)

    return result

arr = np.random.randint(1, 10, 5)

print(arr)
print(nearestSmallElements(arr))