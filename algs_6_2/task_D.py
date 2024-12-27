def things_to_do(quantity: int, diversity: int, things: list[int]) -> list[int]:
    things = sorted(things)
    first = 0
    second = 0
    days = 1

    while second < quantity:
        if things[second] - things[first] <= diversity:
            second += 1
            if second >= quantity:
                if second - first > days:
                    days = second - first
        else:
            if second - first > days:
                days = second - first
            first += 1
            second += 1

    return days


def input_things_to_do() -> None:
    quantity, diversity = map(int, input().split())
    things = list(map(int, input().split()))
    print(things_to_do(quantity, diversity, things))


input_things_to_do()
