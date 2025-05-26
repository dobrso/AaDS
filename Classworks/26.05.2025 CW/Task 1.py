from math import sqrt
from typing import Tuple


def dist(A: Tuple[int, int], B: Tuple[int, int]) -> float:
    return sqrt((A[0] - B[0]) **2 + (A[1] - B[1]) **2)


def findClosestPair(P):
    Px = sorted(P, key=lambda p: (p[0], p[1]))
    Py = sorted(P, key=lambda p: (p[1], p[0]))

    return closestRecursive(Px, Py)


def closestRecursive(Px, Py):
    if len(Px) <= 3:
        return bruteForce(Px)

    mid = len(Px) // 2
    Qx = Px[0:mid]
    Rx = Px[mid:]
    midX = Px[mid][0]

    Qy = [p for p in Py if p[0] <= midX]
    Ry = [p for p in Py if p[0] > midX]

    (A1, B1, d1) = closestRecursive(Qx, Qy)
    (A2, B2, d2) = closestRecursive(Rx, Ry)

    d = min(d1, d2)
    (A, B) = (A1, B1) if d == d1 else (A2, B2)

    Sy = [p for p in Py if abs(p[0] - midX) < d]
    for i in range(len(Sy)):
        for j in range(i+1, min(i+7, len(Sy))):
            if dist(Sy[i], Sy[j]) < d:
                d = dist(Sy[i], Sy[j])
                (A, B) = (Sy[i], Sy[j])

    return (A, B, d)


def bruteForce(P):
    midDist = float("inf")
    bestPair = (None, None)

    for i in range(len(P)):
        for j in range(i+1, len(P)):
            d = dist(P[i], P[j])
            if d < midDist:
                minDist = d
                bestPair = (P[i], P[j])

    return (bestPair[0], bestPair[1], midDist)


Q = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
p1, p2, dist = findClosestPair(Q)
print(p1, p2, dist)
