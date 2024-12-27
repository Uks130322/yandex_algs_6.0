# import sys
#
# sys.setrecursionlimit(100000)
#
#
# def pedigree(quantity: int, tree: list) -> str:
#     posterity = [1] * quantity
#
#     def go_deep(tree: list, key: str, parents: set) -> None:
#         if key in parents:
#             return
#         parents.add(key)
#         result = 0
#         for child in tree[key]:
#             if child not in parents:
#                 result += go_deep(tree, child, parents) + 1
#         posterity[key - 1] += result
#         return result
#
#     go_deep(tree, 1, set())
#     return posterity
#
#
# def input_pedigree() -> None:
#     quantity = int(input())
#     tree = [[]] * (quantity + 1)
#     for _ in range(quantity - 1):
#         parent, child = map(int, input().split())
#         tree[parent] = tree[parent] + [child]
#         tree[child] = tree[child] + [parent]
#     print(*pedigree(quantity, tree))
#
#
# input_pedigree()

import sys
from collections import defaultdict

sys.setrecursionlimit(100000)


def pedigree(quantity: int, tree: defaultdict) -> list:
    posterity = [0] * quantity

    def go_deep(node: int, parent: int) -> int:
        count = 1
        for child in tree[node]:
            if child != parent:
                count += go_deep(child, node)
        posterity[node] = count
        return count

    go_deep(0, -1)
    return posterity


def input_pedigree() -> None:
    quantity = int(input())
    tree = defaultdict(list)
    for _ in range(quantity - 1):
        parent, child = map(int, input().split())
        tree[parent - 1].append(child - 1)
        tree[child - 1].append(parent - 1)
    print(*pedigree(quantity, tree))


input_pedigree()
