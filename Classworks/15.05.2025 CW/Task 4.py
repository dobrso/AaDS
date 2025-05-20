from typing import List


def computePrefixSums(a: List[List[int]], n: int) -> List[List[int]]:
    P = [[0] * (n+1)] * (n+1)

    for i in range(n+1):
        for j in range(n+1):
            P[i][j] = a[i-1][j-1] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]

    return P


def sumSquares(a: List[List[int]], n: int, m: int) -> List[int]:
    P = computePrefixSums(a, n)
    result = []

    for i in range(0, n-m+1):
        for j in range(0, n-m+1):
            sum = P[i+m][j+m] - P[i][j+m] - P[i+m][j] + P[i][j]
            result.append(sum)

    return result
