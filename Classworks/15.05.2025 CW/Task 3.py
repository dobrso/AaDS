from typing import List
from functools import cmp_to_key


def compare(a: str, b: str) -> int:
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0


def maxNumber(arr: List[int]) -> str:
    strArr = []
    for num in arr:
        strArr.append(str(num))

    strArr = sorted(strArr, key=cmp_to_key(compare))

    result = ""
    for s in strArr:
        result += s

    if result[0] == "0":
        return "0"
    else:
        return result


arr = [3, 30, 34, 5, 9]
print(maxNumber(arr)) # 9534330
