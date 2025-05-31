from typing import List


def maxEqualSequence(A: List[int]) -> int:
    N = len(A)
    if N == 0:
        return 0

    currentLen = 1
    maxLen = 1

    for i in range(1, N):
        if A[i] == A[i-1]:
            currentLen += 1
        else:
            currentLen = 1

        if currentLen > maxLen:
            maxLen = currentLen

    return maxLen


A = [1, 1, 2, 2, 2, 3, 3]
print(maxEqualSequence(A))
