def endpointZeros(n: int) -> int:
    if n == 0:
        raise ValueError("Число должно быть положительным")

    if (n & 1) == 1:
        return 0
    else:
        return 1 + endpointZeros(n // 2)


n = 11
print(endpointZeros(n))
