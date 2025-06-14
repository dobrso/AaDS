def countMinCoins(n: int):
    coins = [25, 10, 5, 1]
    count = 0
    used = {coin: 0 for coin in coins}

    for coin in coins:
        while n >= coin:
            n -= coin
            count += 1
            used[coin] += 1

    return count, used


n = 63
print(countMinCoins(n))
