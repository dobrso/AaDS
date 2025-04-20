from collections import deque
import random
import solutionUtils
import numpy as np

def mergeQueues(Q1: deque, Q2: deque) -> deque:
    Q = deque()

    while Q1 and Q2:
        if Q1[0] <= Q2[0]:
            Q.append(Q1.popleft())
        else:
            Q.append(Q2.popleft())

    while Q1:
        Q.append(Q1.popleft())
    while Q2:
        Q.append(Q2.popleft())

    return Q

times = []
sizes = solutionUtils.generateSizes(10, 7)

for size in sizes:
    Q1 = deque([random.randint(size, size * 10) for _ in range(10)])
    Q2 = deque([random.randint(size, size * 10) for _ in range(10)])

    time = solutionUtils.measureTimeNanosMean(mergeQueues, Q1, Q2, repeatTimes=10)
    times.append(time)

print(np.mean(times))