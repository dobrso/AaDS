from typing import List

def findIndex(arr: List[int]) -> int:
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

        if left == right:
            j = left
            return j

testOne = [9, 7, 5, 3, 4, 6, 8]
testTwo = [100, 50, 10, 20, 40, 60]

print(findIndex(testOne))
print(findIndex(testTwo))