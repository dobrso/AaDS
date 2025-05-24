from math import atan2, sqrt
from typing import List, Tuple


def findFarthestPoints(Q: List[Tuple[int, int]]) -> Tuple[int, int]:
    CH = grahamScan(Q)

    maxDist = 0
    bestPair = (None, None)
    j = 1

    for i in range(len(CH)):
        while dist(CH[i], CH[(j+1) % len(CH)]) > dist(CH[i], CH[j]):
            j = (j + 1) % len(CH)

        d = dist(CH[i], CH[j])
        if d > maxDist:
            maxDist = d
            bestPair = (CH[i], CH[j])

    return bestPair


def grahamScan(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    start = min(points, key=lambda p: (p[1], p[0]))

    def polarAngle(p: Tuple[int, int]) -> float:
        return atan2(p[1] - start[1], p[0] - start[0])

    sortedPoints = sorted(points, key=lambda p: (polarAngle(p), (p[0] - start[0]) **2 + (p[1] - start[1]) **2))
    stack = []

    for p in sortedPoints:
        while len(stack) >= 2 and cross(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)

    return stack


def cross(o: Tuple[int, int], a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def dist(a: Tuple[int, int], b: Tuple[int, int]) -> float:
    return sqrt((a[0] - b[0]) **2 + (a[1] - b[1]) **2)


Q = [(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)]
print(findFarthestPoints(Q))

points = [(0, 0), (1, 1), (2, 2), (2, 0), (0, 2), (1, 0.5)]
hull = grahamScan(points)
print(hull)
