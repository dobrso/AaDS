from typing import List


def findCommonElement(x: List[int],
                      y: List[int],
                      z: List[int]) -> int:
    i = 0
    j = 0
    k = 0

    p = len(x)
    q = len(y)
    r = len(z)

    while i < p and j < q and k < r:
        if x[i] == y[j] and y[j] == z[k]:
            return x[i]

        m = min(x[i], y[j], z[k])

        if x[i] == m:
            i += 1
        if y[j] == m:
            j += 1
        if z[k] == m:
            k += 1

    return None


x = [1, 2, 4, 5, 6, 7]
y = [5, 10, 11]
z = [3, 5, 20, 30]

print(findCommonElement(x, y, z)) # 5
