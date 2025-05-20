from typing import List


def findI(a: List[List[int]]) -> int | None:
    n = len(a)
    candidate = 0

    for i in range(n):
        if a[candidate][i] == 1 or a[i][candidate] == 0:
            candidate = i

    for j in range(0, n):
        if j != candidate and a[candidate][j] != 0:
            return None

    for i in range(0, n):
        if i != candidate and a[i][candidate] != 1:
            return None

    return candidate


a = [
    [0, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0]
]

print(findI(a)) # 1
