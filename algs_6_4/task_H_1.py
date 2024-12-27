import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)


def pedigree(quantity: int, tree: defaultdict, prices: list) -> str:
    if quantity == 1:
        return f'{prices[0]} 1\n1'
    dp = [(0, 0) for _ in range(quantity)]
    colored = [False] * quantity

    def go_deep(node: int, parent: int) -> None:
        dp0 = 0
        dp1 = prices[node]
        for child in tree[node]:
            if child != parent:
                go_deep(child, node)
                dp0 += dp[child][1]
                dp1 += min(dp[child][0], dp[child][1])
        dp[node] = (dp0, dp1)

    def collect(node: int, parent: int, parent_included: bool) -> None:
        dp0_node, dp1_node = dp[node]
        if parent_included:
            if dp1_node <= dp0_node:
                colored[node] = True
                for child in tree[node]:
                    if child != parent:
                        collect(child, node, True)
            else:
                colored[node] = False
                for child in tree[node]:
                    if child != parent:
                        collect(child, node, False)
        else:
            colored[node] = True
            for child in tree[node]:
                if child != parent:
                    collect(child, node, True)

    go_deep(0, -1)
    root_dp0, root_dp1 = dp[0]
    if root_dp1 <= root_dp0:
        colored[0] = True
        total_cost = root_dp1
        for child in tree[0]:
            if child != -1:
                collect(child, 0, True)
    else:
        colored[0] = False
        total_cost = root_dp0
        for child in tree[0]:
            if child != -1:
                collect(child, 0, False)

    colored_nodes = [i + 1 for i, included in enumerate(colored) if included]
    return f'{total_cost} {len(colored_nodes)}\n' + " ".join(map(str, colored_nodes))


def input_pedigree() -> None:
    quantity = int(sys.stdin.readline())
    tree = defaultdict(list)
    for _ in range(quantity - 1):
        parent, child = map(int, sys.stdin.readline().split())
        tree[parent - 1].append(child - 1)
        tree[child - 1].append(parent - 1)
    prices = list(map(int, sys.stdin.readline().split()))
    print(pedigree(quantity, tree, prices))


input_pedigree()
