from typing import List


def findMedianOfSortedArrays(A: List[int], B: List[int]) -> int:
    if len(A) > len(B):
        A, B = B, A

    n = len(A)
    m = len(B)
    low = 0
    high = n
    totalLeft = (n + m + 1) // 2

    while low <= high:
        i = (low + high) // 2
        j = totalLeft - i

        leftA = float("-inf") if i == 0 else A[i-1]
        rightA = float("inf") if i == n else A[i]

        leftB = float("-inf") if j == 0 else B[j-1]
        rightB = float("inf") if j == m else B[j]

        if leftA <= rightB and leftB <= rightA:
            if (n + m) % 2 == 1:
                return max(leftA, leftB)
            else:
                return (max(leftA, leftB) + min(rightA, rightB)) // 2
        elif leftA > rightB:
            high = i - 1
        else:
            low = i + 1
