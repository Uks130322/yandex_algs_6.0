def trial_product(quantity: int, numbers: list[int]) -> list[int]:
    summa = 0
    prefix_sum = []

    for index in range(quantity-1, -1, -1):
        if not prefix_sum:
            prefix_sum = [numbers[index]]
        else:
            prefix_sum.append(prefix_sum[-1] + numbers[index])

    index = 0
    while index < quantity - 2:
        summa += (prefix_sum[index]
                  * numbers[quantity - index - 2]
                  * (prefix_sum[-1] - prefix_sum[index + 1])
                  % 1_000_000_007)
        summa %= 1_000_000_007
        index += 1

    return summa


def input_trial_product() -> None:
    quantity = int(input())
    numbers = list(map(int, input().split()))
    print(trial_product(quantity, numbers))


input_trial_product()

num = 10**6
lst = [10**6 - 1] * num

print(trial_product(num, lst))
