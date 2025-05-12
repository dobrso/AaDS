from typing import List


def modSort(A: List[int]) -> List[int]:
    n = len(A)
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if A[mid] == 0:
            A[low], A[mid] = A[mid], A[low]
            low += 1
            mid += 1

        elif A[mid] == 1:
            mid += 1

        else:
            A[mid], A[high] = A[high], A[mid]
            high -= 1

    return A


a = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
print(modSort(a))
