def calculatePostfix(string: str) -> int:
    stack = []
    elements = string.strip().split()

    for element in elements:
        if element.isdigit():
            stack.append(int(element))
        else:
            a = stack.pop()
            b = stack.pop()

            if element == "+":
                stack.append(a + b)
            elif element == "-":
                stack.append(a - b)
            else:
                stack.append(a * b)

    result = stack.pop()
    return result

testString = "5 3 2 + 3 * +"
print(calculatePostfix(testString))