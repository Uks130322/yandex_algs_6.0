def prefix_sums(subsequence: list[int]) -> list[int]:
    result = []
    for item in subsequence:
        if not result:
            result = [item]
        else:
            result.append(result[-1] + item)
    return result


def input_prefix_sums() -> None:
    length = input()
    subsequence = map(int, input().split())
    print(*prefix_sums(subsequence))


input_prefix_sums()
