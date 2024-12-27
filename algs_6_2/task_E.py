def del_medians(quantity: int, numbers: list[int]) -> list[int]:
    numbers = sorted(numbers)
    medians = []
    if quantity % 2:
        left = quantity // 2 - 1
        right = quantity // 2
    else:
        left = quantity // 2 - 1
        right = quantity // 2

    while left >= 0 and right <= quantity:
        if (quantity - (right - left - 1)) % 2:
            medians.append(numbers[right])
            right += 1
        else:
            medians.append(numbers[left])
            left -= 1

    medians.append(numbers[-1])
    return medians


def input_del_medians() -> None:
    quantity = int(input())
    numbers = list(map(int, input().split()))
    print(*del_medians(quantity, numbers))


input_del_medians()
