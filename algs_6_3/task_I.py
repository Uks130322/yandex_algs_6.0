def get_rovers(quantity: int, mains: tuple[int]) -> list[int]:
    from collections import deque
    result = [None] * quantity
    deques = {1: [], 2: [], 3: [], 4: []}
    for i in range(quantity):
        rover = list(map(int, input().split())) + [i]
        deques[rover[0]].append(rover[1:])

    for num in (1, 2, 3, 4):
        deques[num] = deque(sorted(deques[num], key=lambda x: x[0]))
    for time in range(400):
        first = deques[1][0][1] + 1 if deques[1] and deques[1][0][0] <= time else 0
        second = deques[2][0][1] + 1 if deques[2] and deques[2][0][0] <= time else 0
        third = deques[3][0][1] + 1 if deques[3] and deques[3][0][0] <= time else 0
        fourth = deques[4][0][1] + 1 if deques[4] and deques[4][0][0] <= time else 0
        if first:
            if 1 in mains:
                if 4 in mains:
                    if fourth:
                        deques[1][0][0] = time + 1
                    else:
                        result[first - 1] = time
                        deques[1].popleft()
                else:
                    result[first - 1] = time
                    deques[1].popleft()
            else:
                if 2 in mains and second or 3 in mains and third or fourth:
                    deques[1][0][0] = time + 1
                else:
                    result[first - 1] = time
                    deques[1].popleft()
        if second:
            if 2 in mains:
                if 1 in mains:
                    if first:
                        deques[2][0][0] = time + 1
                    else:
                        result[second - 1] = time
                        deques[2].popleft()
                else:
                    result[second - 1] = time
                    deques[2].popleft()
            else:
                if 3 in mains and third or 4 in mains and fourth or first:
                    deques[2][0][0] = time + 1
                else:
                    result[second - 1] = time
                    deques[2].popleft()
        if third:
            if 3 in mains:
                if 2 in mains:
                    if second:
                        deques[3][0][0] = time + 1
                    else:
                        result[third - 1] = time
                        deques[3].popleft()
                else:
                    result[third - 1] = time
                    deques[3].popleft()
            else:
                if 4 in mains and fourth or 1 in mains and first or second:
                    deques[3][0][0] = time + 1
                else:
                    result[third - 1] = time
                    deques[3].popleft()
        if fourth:
            if 4 in mains:
                if 3 in mains:
                    if third:
                        deques[4][0][0] = time + 1
                    else:
                        result[fourth - 1] = time
                        deques[4].popleft()
                else:
                    result[fourth - 1] = time
                    deques[4].popleft()
            else:
                if 2 in mains and second or 1 in mains and first or third:
                    deques[4][0][0] = time + 1
                else:
                    result[fourth - 1] = time
                    deques[4].popleft()

    return result


def input_get_rovers() -> None:
    quantity = int(input())
    mains = tuple(map(int, input().split()))
    print(*get_rovers(quantity, mains), sep='\n')


input_get_rovers()
