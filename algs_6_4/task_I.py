import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10000000)


def path_pair(quantity: int, tree: defaultdict) -> list:
    max_node, max_length, result, parent = bfs(0, tree)
    end_node, diameter, distance, parent = bfs(max_node, tree)

    path = []
    cur_node = end_node
    while cur_node != -1:
        path.append(cur_node)
        cur_node = parent[cur_node]

    def find_max_branches(tree, diameter_path):
        diameter_set = set(diameter_path)

        max_branches = dict()

        def dfs_no_diameter(node, parent):
            nonlocal max_branches
            branch_length = 0

            for child in tree[node]:
                if child == parent or child in diameter_set:
                    continue
                cur_length = dfs_no_diameter(child, node) + 1
                branch_length = max(branch_length, cur_length)

            max_branches[node] = branch_length

            return branch_length

        for path_node in diameter_path:
            dfs_no_diameter(path_node, -1)

        return max_branches

    max_branches = find_max_branches(tree, path)

    def find_max_branch_outside_diameter(tree, diameter_path):
        diameter_set = set(diameter_path)

        def dfs_outside(node, parent):
            max_branch = 0
            for child in tree[node]:
                if child == parent or child in diameter_set:
                    continue

                child_branch = dfs_outside(child, node) + 1
                max_branch = max(max_branch, child_branch)

            return max_branch

        max_outside_branch = 0
        max_outside_node = None

        for node in range(len(tree)):
            if node in diameter_set:
                continue

            branch_length = dfs_outside(node, -1)
            if branch_length > max_outside_branch:
                max_outside_branch = branch_length
                max_outside_node = node

        return max_outside_branch, max_outside_node

    branch_outside, branch_outside_node = find_max_branch_outside_diameter(tree, path)

    max_mult_by_diam = max([i * (diameter - i - 1) for i in range(len(path))])

    max_with_branch_and_diam = 0
    for i in range(len(path) - 1):
        max_left = 0
        max_right = 0
        for j in range(i + 1):
            left = max_branches[path[j]] + j
            max_left = max(max_left, left)
        for j in range(i + 1, diameter):
            right = max_branches[path[j]] + (diameter - j)
            max_right = max(max_right, right)
        max_with_branch_and_diam = max(max_with_branch_and_diam, max_left * max_right)
    max_with_outside_and_diam = diameter * branch_outside

    return max(max_mult_by_diam, max_with_branch_and_diam, max_with_outside_and_diam)


def bfs(node: int, tree: defaultdict) -> list:
    result = [-1] * len(tree)
    result[node] = 0
    queue = deque([node])
    max_length = 0
    max_node = node
    parent = [-1] * len(tree)

    while queue:
        cur_node = queue.popleft()
        for child in tree[cur_node]:
            if result[child] == -1:
                result[child] = result[cur_node] + 1
                parent[child] = cur_node
                queue.append(child)
                if result[child] > max_length:
                    max_length = result[child]
                    max_node = child

    return max_node, max_length, result, parent


def input_path_pair() -> None:
    quantity = int(input())
    tree = defaultdict(list)
    for _ in range(quantity - 1):
        parent, child = map(int, input().split())
        tree[parent - 1].append(child - 1)
        tree[child - 1].append(parent - 1)
    print(path_pair(quantity, tree))


input_path_pair()
