def calculate(string: str) -> str:
    num_stack = []
    sign_stack = []
    brackets = 0
    signs = ["-", "+", "*"]
    previous = None
    for char in string:
        # print(num_stack, sign_stack)
        if char.isalpha():
            return "WRONG"
        if char == " ":
            if previous == 'number':
                previous = 'finished_number'
            continue
        if char.isdigit():
            if previous == "negative":
                num_stack.append("-" + char)
                previous = 'number'
            elif previous == 'number':
                num_stack[-1] += char
                previous = 'number'
            elif previous is None or previous != 'finished_number':
                num_stack.append(char)
                previous = 'number'
            elif previous == 'finished_number':
                return "WRONG"
        elif char in signs:
            if previous not in signs:
                if char == "*":
                    if previous == '(':
                        return 'WRONG'
                    sign_stack.append(char)
                    previous = char
                elif char == "-" or char == "+":
                    if char == '+' and previous == '(':
                        return 'WRONG'
                    if char == "-" and previous is None or previous == "(":
                        previous = "negative"
                        continue
                    while sign_stack and sign_stack[-1] != '(':
                        num_stack.append(sign_stack.pop())
                    sign_stack.append(char)
                    previous = char
            else:
                return "WRONG"
        elif char == "(":
            brackets -= 1
            sign_stack.append(char)
            previous = char
        elif char == ")":
            if brackets == 0 or previous in signs:
                return "WRONG"
            else:
                brackets += 1
                while sign_stack[-1] != "(":
                    num_stack.append(sign_stack.pop())
                sign_stack.pop()
    while sign_stack:
        num_stack.append(sign_stack.pop())
    if brackets != 0:
        return "WRONG"
    return num_stack


def postfix_notation(string: list[str, int]) -> int:
    if string == "WRONG":
        return "WRONG"
    result = 0
    stack = []
    for char in string:
        if char.isdigit() or char[0] == '-' and char[1:].isdigit():
            stack.append(int(char))
        else:
            if not stack:
                return "WRONG"
            second = stack.pop()
            if not stack:
                return "WRONG"
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
    string = input()
    print(postfix_notation(calculate(string)))


input_postfix_notation()

