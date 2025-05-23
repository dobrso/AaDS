from typing import List, Tuple


def generateSegments(n: int) -> List[Tuple[Tuple[float, int], Tuple[float, int]]]:
    k = n // 2
    segments = []

    for i in range(k):
        x = i / k
        start = (x, 0)
        end = (x, 1)
        segments.append((start, end))

    for j in range(k):
        y = j / k
        start = (0, y)
        end = (1, y)
        segments.append((start, end))

    return segments


n = 4
print(generateSegments(n))
