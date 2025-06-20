n = 2
k = 2

def generateSequence(seq, level):
    global k, n
    if level == k:
        print(seq)
        return
    for i in range(1, n+1):
        seq.append(i)
        generateSequence(seq, level+1)
        seq.pop()

generateSequence([], 0)
