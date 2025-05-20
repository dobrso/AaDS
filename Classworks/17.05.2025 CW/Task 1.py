from typing import List


def lengthLIS(x: List[int]) -> int:
    tails = []
    n = len(x)

    for i in range(0, n):
        left = 0
        right = len(tails)

        while left < right:
            mid = (left + right) // 2

            if tails[mid] < x[i]:
                left = mid + 1
            else:
                right = mid

        if left == len(tails):
            tails.append(x[i])
        else:
            tails[left] = x[i]

    return len(tails)


x = [3, 1, 2, 1, 8, 5, 6]
print(lengthLIS(x)) # 4
