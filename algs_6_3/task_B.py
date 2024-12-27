def lineland(quantity: int, cities: list[int]) -> list[int]:
    stack = []
    result = [None] * quantity
    num = 0
    while num <= quantity:
        if num == quantity:
            if not stack:
                return result
            else:
                result[stack[-1][1]] = -1
                stack.pop()
                continue
        if not stack or stack[-1][0] <= cities[num]:
            stack.append((cities[num], num))
            num += 1
        else:
            result[stack[-1][1]] = num
            stack.pop()

    return result


def input_lineland() -> None:
    quantity = int(input())
    cities = list(map(int, input().split()))
    print(*lineland(quantity, cities))


input_lineland()
