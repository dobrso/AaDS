def reversePrint(fileName: str) -> str:
    stack = []

    with open(fileName, "r", encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                stack.append(word)

    reversedInput = []
    while stack:
        reversedInput.append(stack.pop())

    resultString = ", ".join(reversedInput)
    return resultString

fileName = "Test File.txt"
print(reversePrint(fileName))