import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)


def pedigree(quantity: int, tree: defaultdict, prices: list) -> list:
    if quantity == 1:
        return f'{prices[0]} 1\n1'
    colored = [False] * quantity

    def go_deep(node: int, parent: int) -> int:
        print(colored)
        sum_price = sum([prices[child] for child in tree[node] if child != parent and not colored[child]])
        if parent == 0 and len(tree[parent]) == 1:
            sum_price += prices[parent]
        if prices[node] < sum_price:
            colored[node] = True
        if parent > -1 and not colored[parent]:
            colored[node] = True
        for child in tree[node]:
            if child != parent:
                go_deep(child, node)

    go_deep(0, -1)
    if all(colored[item] for item in tree[0]):
        colored[0] = False
    colored_nodes = [i + 1 for i, item in enumerate(colored) if item]
    sum_price = sum([prices[node - 1] for node in colored_nodes])
    return f'{sum_price} {len(colored_nodes)}\n' + " ".join(map(str, colored_nodes))


def input_pedigree() -> None:
    quantity = int(input())
    tree = defaultdict(list)
    for _ in range(quantity - 1):
        parent, child = map(int, input().split())
        tree[parent - 1].append(child - 1)
        tree[child - 1].append(parent - 1)
    prices = list(map(int, input().split()))
    print(pedigree(quantity, tree, prices))


input_pedigree()
