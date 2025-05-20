from typing import List


def radixSortBits(arr: List[int], k: int) -> List[int]:
    n = len(arr)
    zeros = []
    ones = []

    for i in range(0, k):
        zeros = []
        ones = []

        for j in range(0, n):
            if (arr[j] >> i) & 1 == 0:
                zeros.append(arr[j])
            else:
                ones.append(arr[j])

        arr = zeros + ones

    return arr
