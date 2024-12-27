def pick_up_point(worktime: int, per_minute: int, clients: list[int]) -> int:
    result = 0
    minute = 0
    rest = 0
    for number in clients:
        if minute <= worktime:
            result += number + rest
            rest = max(0, number + rest - per_minute)
            minute += 1
        else:
            result += number + rest
            rest = 0
    result += rest
    return result


def input_pick_up_point() -> None:
    worktime, per_minute = map(int, input().split())
    clients = list(map(int, input().split()))
    print(pick_up_point(worktime, per_minute, clients))


input_pick_up_point()
