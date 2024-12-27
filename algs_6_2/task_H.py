def move_on(quantity: int, spaces: list[int]) -> int:
    prefix_sum_left = [0] * quantity

    summa = 0
    for index in range(quantity):
        if index > 0:
            prefix_sum_left[index] = prefix_sum_left[index - 1] + summa
        summa += spaces[index]

    prefix_sum_right = [0] * quantity

    summa = 0
    for index in range(quantity - 1, -1, -1):
        if index < quantity - 1:
            prefix_sum_right[index] = prefix_sum_right[index + 1] + summa
        summa += spaces[index]

    min_sum = prefix_sum_left[-1] + prefix_sum_right[-1]
    for i in range(quantity):
        move_sum = prefix_sum_left[i] + prefix_sum_right[i]
        min_sum = min(move_sum, min_sum)

    return min_sum


def input_move_on() -> None:
    quantity = int(input())
    spaces = list(map(int, input().split()))
    print(move_on(quantity, spaces))


input_move_on()

# length = 2 * (10 ** 4)
# numbers = [10 ** 9] * length
# print(move_on(length, numbers))
