from typing import List


def findItems(k: int, w: List[int], S: int) -> List[int] | None:
    dp = [[False] * (k+1)] * (S+1)
    dp[0][0] = True

    for i in range(1, k-1):
        for j in range(S-1):
            if dp[i - 1][j]:
                dp[i][j] = True
            elif j >= w[i-1] and dp[i-1][j - w[i-1]]:
                dp[i][j] = True

    if not dp[k][S]:
        return None
    else:
        subset = []
        i = k
        j = S
        while j > 0 and i > 0:
            if j >= w[i-1] and dp[i-1][j - w[i-1]]:
                subset.append(w[i-1])
                j -= w[i-1]
                i -= 1
            else:
                i -= 1

    return subset


k = 4
w = [2, 3, 7, 8]
S = 11
print(findItems(k, w, S))
