def algs_learning(quantity: int, interesting: list[int], usefull: list[int], mood: list[int]) -> list[int]:
    algs = []
    learned = set()

    algs_zip = [(index, interesting[index], usefull[index]) for index in range(quantity)]
    interesting_zip = sorted(algs_zip, key=lambda x: (-x[1], -x[2], x[0]))
    usefull_zip = sorted(algs_zip, key=lambda x: (-x[2], -x[1], x[0]))

    first = 0
    second = 0
    day = 0
    while day < len(mood):
        if mood[day]:
            algorithm = usefull_zip[first][0]
            if algorithm not in learned:
                algs.append(algorithm + 1)
                learned.add(algorithm)
                day += 1
            first += 1
        else:
            algorithm = interesting_zip[second][0]
            if not algorithm in learned:
                algs.append(algorithm + 1)
                learned.add(algorithm)
                day += 1
            second += 1

    return algs


def input_algs_learning() -> None:
    quantity = int(input())
    interesting = list(map(int, input().split()))
    usefull = list(map(int, input().split()))
    mood = list(map(int, input().split()))
    print(*algs_learning(quantity, interesting, usefull, mood))


input_algs_learning()


# length = 10 ** 5
# first = range(length)
# second = range(length - 1, -1, -1)
# third = [i // 2 for i in range(length)]
#
# print(*algs_learning(length, first, second, third))