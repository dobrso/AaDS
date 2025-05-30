def findWays(N: int, K: int) -> int:
    if N <= 0:
        return None
    if N == 1:
        return 1

    window = []
    window.append(1)
    currentSum = 1
    result = 0

    for i in range(1, N):
        dpI = currentSum
        result = dpI

        window.append(dpI)
        currentSum += dpI

        if len(window) > K:
            deletedValue = window.pop(0)
            currentSum -= deletedValue

    return result


N = 5
K = 2
print(findWays(N, K))
