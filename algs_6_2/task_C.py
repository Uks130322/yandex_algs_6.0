def monument_quantity(quantity: int, safe_distance: int, monuments: list[int]) -> list[int]:
    first = 0
    second = 1
    result = 0

    while second < quantity:
        distance = monuments[second] - monuments[first]
        if distance > safe_distance:
            result += quantity - second
            first += 1
        else:
            second += 1
    return result


def input_monument_quantity() -> None:
    quantity, safe_distance = map(int, input().split())
    monuments = list(map(int, input().split()))
    print(monument_quantity(quantity, safe_distance, monuments))


input_monument_quantity()
