import math


def logFactorial(N: int) -> float:
    if N == 0 or N == 1:
        return 0
    return math.log2(N) + logFactorial(N-1)
