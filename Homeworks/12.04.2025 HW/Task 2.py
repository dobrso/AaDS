def isCorrectSequence(bracketSequence: str) -> bool:
    stack = []

    for bracket in bracketSequence:
        if bracket == "(":
            stack.append(bracket)
        else:
            if not(stack):
                return False
            else:
                stack.pop()

    result = True if not(stack) else False
    return result

testSequences = ["()", "(())()", "()()", "((()))", ")(", "())(()", "(", "))))", "((())"]

for sequence in testSequences:
    print(isCorrectSequence(sequence))