from typing import List


def removeDuplicates(A: List[int]) -> List[int]:
    if len(A) <= 1:
        return A

    A.sort()

    Result = []
    Result.append(A[0])

    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            Result.append(A[i])

    return Result


A = [4, 2, 7, 4, 2, 9]
print(removeDuplicates(A))
