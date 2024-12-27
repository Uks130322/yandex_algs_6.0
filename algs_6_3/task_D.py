def postfix_notation(string: list[str]) -> int:
    result = 0
    stack = []
    for char in string:
        if char.isdigit():
            stack.append(int(char))
        else:
            second = stack.pop()
            first = stack.pop()
            if char == "+":
                result = first + second
            elif char == "-":
                result = first - second
            elif char == "*":
                result = first * second
            stack.append(result)

    return stack[0]


def input_postfix_notation() -> None:
    string = input().split()
    print(postfix_notation(string))


input_postfix_notation()
