import random

# CBS - correct bracket sequence
def countCBS(string: str) -> int:
    openCount = 0
    removals = 0

    for i in string:
        if i == "(":
            openCount += 1
        else:
            if openCount > 0:
                openCount -= 1
            else:
                removals += 1

    needToRemove = removals + openCount
    return needToRemove

firstTestString = "((()))"
print(countCBS(firstTestString)) # 0

secondTestString = "(()))"
print(countCBS(secondTestString)) # 1

randomString = "(" * random.randint(1, 10) + ")" * random.randint(1, 10)
print(countCBS(randomString)) # random number