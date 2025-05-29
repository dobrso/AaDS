from typing import List


def findMax(A: List[int], left: int, right: int) -> int:
    if left == right:
        return A[left]

    mid = (left + right) // 2

    maxLeft = findMax(A, left, mid)
    maxRight = findMax(A, mid+1, right)

    if maxLeft > maxRight:
        return maxLeft
    else:
        return maxRight


A = [3, 8, 2, 5, 1, 9, 7]
print(findMax(A, 0, len(A) - 1))
