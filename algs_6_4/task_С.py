import sys

sys.setrecursionlimit(100000)

DEPTHS = dict()


def pedigree(quantity: int, lineage: dict[str: set[str]], children_pairs: list[tuple[str]]) -> list:
    result = []
    for pair in children_pairs:
        child1 = pair[0]
        child2 = pair[1]
        while child1 != child2:
            if DEPTHS[child1] > DEPTHS[child2]:
                child1 = lineage[child1]
                if not lineage.get(child1):
                    result.append(child1)
                    break
                continue
            elif DEPTHS[child1] < DEPTHS[child2]:
                child2 = lineage[child2]
                if not lineage.get(child2):
                    result.append(child2)
                    break
                continue
            child1 = lineage[child1]
            child2 = lineage[child2]
            if child1 == child2:
                result.append(child1)
                break
        else:
            result.append(child1)

    return result


def pedigree_depth(quantity: int, lineage: dict[str: set[str]], root: str) -> str:
    go_deep(lineage, root)


def go_deep(lineage: dict, key: str, depth: int = 0) -> None:
    DEPTHS[key] = depth
    for elem in lineage.get(key, []):
        go_deep(lineage, elem, depth + 1)


def input_pedigree() -> None:
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    quantity = int(data[0])
    lineage = dict()
    lineage_depth = dict()
    parents = set()
    children = set()
    children_pairs = []
    for i in range(1, quantity):
        child, parent = data[i].split()
        lineage[child] = parent
        lineage_depth[parent] = lineage_depth.get(parent, []) + [child]
        parents.add(parent)
        children.add(child)
    for i in range(quantity, len(data)):
        if data[i] != '':
            children_pairs.append(data[i].split())
    root = parents.difference(children).pop()
    pedigree_depth(quantity, lineage_depth, root)
    result = pedigree(quantity, lineage, children_pairs)
    print(*result, sep='\n')


input_pedigree()

