from typing import List


def countCommon(x: List[int], y: List[int]) -> int:
    i = 0
    j = 0
    count = 0
    k = len(x)
    l = len(y)

    while i < k and j < l:
        if x[i] < y[j]:
            i += 1
        elif x[i] > y[j]:
            j += 1
        else:
            count += 1
            i += 1
            j += 1

    return count


x = [0, 1, 2, 3, 4, 5]
y = [0, 3, 5, 10, 20]

print(countCommon(x, y)) # 3
