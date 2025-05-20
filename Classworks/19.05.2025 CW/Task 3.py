from typing import List
from math import ceil


def select(stones: List[int], k: int) -> int:
    n = len(stones)

    if n <= 5:
        stones.sort()
        return stones[k-1]

    groups = [stones[i:i+5] for i in range(0, n, 5)]

    medians = []

    for group in groups:
        group.sort()
        m = len(group)
        midIndex = m // 2
        medians.append(group[midIndex])

    pivot = select(medians, ceil(len(medians) / 2))

    less = []
    greater = []
    equal = []

    for stone in stones:
        if stone < pivot:
            less.append(stone)
        elif stone == pivot:
            equal.append(stone)
        else:
            greater.append(stone)

    sizeLess = len(less)
    sizeEqual = n - sizeLess - len(greater)

    if k <= sizeLess:
        return select(less, k)
    elif k <= sizeLess + sizeEqual:
        return pivot
    else:
        return select(greater, k - sizeLess - sizeEqual)

stones = [7, 2, 9, 4, 1, 5, 3, 6, 8]
k = 4
print(select(stones, k)) # 4
