def correct_brackets(string: str) -> str:
    stack = []
    for item in string:
        if item in ['[', '(', "{"]:
            stack.append(item)
        elif item == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return 'no'
        elif item == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 'no'
        else:
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return 'no'
    if not stack:
        return 'yes'
    else:
        return 'no'


def input_correct_brackets() -> None:
    string = input()
    print(correct_brackets(string))


input_correct_brackets()
