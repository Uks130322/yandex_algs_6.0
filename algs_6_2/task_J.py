def evidence(quantity: int, weights: list[int], experiments: int, boring: int, start_numbers: list[int]) -> list[int]:
    result = []
    prefix_sum = [0] * quantity

    for i in range(quantity - 1, -1, -1):
        if i == quantity - 1:
            prefix_sum[i] = 0
        else:
            prefix_sum[i] = prefix_sum[i + 1] + int(weights[i + 1] == weights[i])

    finish_for_evidence = [0] * quantity

    end = quantity - 1
    start = quantity - 1
    while start >= 0 and end > 0:
        if prefix_sum[start] - prefix_sum[end] <= boring:
            finish_for_evidence[end] = start
            if start == 0:
                end -= 1
            else:
                start -= 1
        else:
            start += 1
            end -= 1

    finish_for_not_risen = [0] * quantity
    stop = 0
    for i in range(quantity):
        if i > 0 and weights[i - 1] > weights[i]:
            stop = i
        finish_for_not_risen[i] = max(finish_for_evidence[i], stop)

    for part in start_numbers:
        result.append(finish_for_not_risen[part - 1] + 1)

    return result


def input_evidence() -> None:
    quantity = int(input())
    weights = list(map(int, input().split()))
    experiments, boring = map(int, input().split())
    start_numbers = list(map(int, input().split()))
    print(*evidence(quantity, weights, experiments, boring, start_numbers))


input_evidence()


# length = 10 ** 5
# first = range(length)
# second = range(length - 1, -1, -1)
# third = [i // 2 for i in range(length)]
#
# print(*algs_learning(length, first, second, third))