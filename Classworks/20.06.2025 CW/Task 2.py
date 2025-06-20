k = 3

def generateSubset(current, subset, size):
    global k
    if len(subset) == size:
        print(subset)
        return
    if current > k:
        return

    subset.append(current)
    generateSubset(current+1, subset, size)
    subset.pop()
    generateSubset(current+1, subset, size)

for size in range(k+1):
    generateSubset(1, [], size)
