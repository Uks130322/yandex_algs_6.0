import sys
from collections import defaultdict

sys.setrecursionlimit(100000)


def pedigree(quantity: int, tree: defaultdict) -> list:
    posterity_depth = [[0, 1] for _ in range(quantity)]
    result = [1] * quantity

    def count_depth(node: int) -> int:
        for child in tree[node]:
            posterity_depth[child][1] = posterity_depth[node][1] + 1
            count_depth(child)

    def count_posterity(node: int, parent: int) -> int:

        count = 1
        for child in tree[node]:
            if child != parent:
                count += count_posterity(child, node)
                if posterity_depth[child][0] == 1:
                    result[child] = 1
        posterity_depth[node][0] = count
        result[node] = posterity_depth[node][0] + sum(result[child] for child in tree[node])
        return count

    count_depth(0)
    count_posterity(0, -1)
    return result


def input_pedigree() -> None:
    quantity = int(input())
    tree = defaultdict(list)
    nodes = map(int, input().split())
    for i, node in enumerate(nodes):
        tree[node - 1].append(i + 1)
    print(*pedigree(quantity, tree))


input_pedigree()
