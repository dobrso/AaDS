n = 5
k = 2

def generateIncreasing(seq, level, start):
    global n, k
    if level == k:
        print(seq)
        return

    for i in range(start, n+1):
        seq.append(i)
        generateIncreasing(seq, level+1, i+1)
        seq.pop()

generateIncreasing([], 0, 1)
