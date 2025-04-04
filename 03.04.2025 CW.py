def fastFactorial(N: int, P: int) -> int:
    e = 0
    n = N
    while n > 0:
        n //= P
        e += n

    if e > 0:
        return 0

    res = 1
    while N > 0:
        q = N // P
        r = N % P

        if q % 2 != 0:
            res = (P - res) % P

        for i in range(1, r+1):
            res = (res * i) % P

        N = q

    return res

print(fastFactorial(10, 7))
print(fastFactorial(14, 4))
print(fastFactorial(19, 404))