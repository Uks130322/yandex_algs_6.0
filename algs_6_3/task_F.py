def min_CBC(length: int, powers: str, string: str) -> str:
    powers = {powers[index]: index + 1 for index in range(len(powers))}
    stack = []
    for item in string:
        if item in ['[', '(']:
            stack.append(item)
        elif item == ']':
            stack.pop()
        elif item == ')':
            stack.pop()

    prefix = ''
    while stack:
        if stack[-1] == '(':
            prefix += ')'
            stack.pop()
        else:
            prefix += ']'
            stack.pop()
    if len(string) + len(prefix) == length:
        return string + prefix

    half_difference = (length - len(string) - len(prefix)) // 2
    min_bracket = '(' if powers['('] < powers['['] else '['
    if min_bracket == '(':
        if powers['('] > powers[')']:
            middle = '()' * half_difference
        else:
            middle = '(' * half_difference + ')' * half_difference
    else:
        if powers['['] > powers[']']:
            middle = '[]' * half_difference
        else:
            middle = '[' * half_difference + ']' * half_difference
    if not prefix:
        return string + middle
    for i, char in enumerate(prefix):
        if powers[char] <= powers[min_bracket]:
            if i == len(prefix) - 1:
                result = string + prefix + middle
            else:
                continue
        else:
            result = string + prefix[:i] + middle + prefix[i:]
            break

    return result


def input_min_CBC() -> None:
    length = int(input())
    powers = input()
    string = input()
    print(min_CBC(length, powers, string))


input_min_CBC()
