def sum_quantity(cars: list[int], summa) -> list[int]:
    current_sum = cars[0]
    begin = end = 0
    quantity = 0

    while end < len(cars):
        if current_sum <= summa:
            if current_sum == summa:
                quantity += 1
            end += 1
            if end >= len(cars):
                break
            current_sum += cars[end]
        else:
            current_sum -= cars[begin]
            begin += 1

    return quantity


def input_sum_quantity() -> None:
    length, summa = map(int, input().split())
    cars = list(map(int, input().split()))
    print(sum_quantity(cars, summa))


input_sum_quantity()
