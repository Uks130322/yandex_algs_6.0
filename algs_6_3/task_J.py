def chairbed(quantity: int, height: int, chairs_height: list[int], chairs_width: list[int]) -> int:
    from collections import deque
    if quantity == 1:
        return 0
    chairs = sorted(list(zip(chairs_height, chairs_width)), key=lambda x: x[0])
    begin, end = 0, 0
    max_discomforts = deque()
    min_discomfort = None
    length = chairs[0][1]

    while begin < quantity:
        if not max_discomforts:
            max_discomforts.append(chairs[end][0] - chairs[begin][0])
        if length < height:
            if end >= quantity - 1:
                break
            end += 1
            length += chairs[end][1]
            diff = chairs[end][0] - chairs[end - 1][0]
            while max_discomforts and max_discomforts[-1] < diff:
                max_discomforts.pop()
            max_discomforts.append(diff)
        else:
            if min_discomfort is None or min_discomfort > max_discomforts[0]:
                min_discomfort = max_discomforts[0]
            length -= chairs[begin][1]
            begin += 1
            if begin < quantity:
                diff = chairs[begin][0] - chairs[begin - 1][0]
                if max_discomforts[0] == diff:
                    max_discomforts.popleft()

    return min_discomfort


def input_chairbed() -> None:
    quantity, height = map(int, input().split())
    chairs_height = list(map(int, input().split()))
    chairs_width = list(map(int, input().split()))
    print(chairbed(quantity, height, chairs_height, chairs_width))


input_chairbed()
