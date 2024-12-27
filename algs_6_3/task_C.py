def window_min(quantity: int, length: int, section: list[int]) -> list[int]:
    from collections import deque
    mins = deque(maxlen=quantity)
    result = []
    index = 0
    while index < quantity:
        print(mins, result, index)
        if not mins:
            mins.append((section[index], index))
            index += 1
        else:
            if index < length:
                if mins[-1][0] > section[index]:
                    mins.pop()
                else:
                    mins.append((section[index], index))
                    index += 1
            else:
                result.append(mins[0][0])
                if mins[0][1] == index - length:
                    mins.popleft()

                while mins and mins[-1][0] >= section[index]:
                    mins.pop()
                mins.append((section[index], index))
                index += 1
    if mins:
        result.append(mins[0][0])
    return result


def input_window_min() -> None:
    quantity, length = map(int, input().split())
    section = list(map(int, input().split()))
    print(*window_min(quantity, length, section))


input_window_min()
