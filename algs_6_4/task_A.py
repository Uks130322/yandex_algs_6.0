
DEPTHS = dict()


def pedigree(quantity: int, lineage: dict[str: set[str]], root: str) -> str:
    go_deep(lineage, root)
    return sorted([(key, value) for key, value in DEPTHS.items()], key=lambda x: x[0])


def go_deep(lineage: dict, key: str, depth: int = 0) -> None:
    DEPTHS[key] = depth
    for elem in lineage.get(key, []):
        go_deep(lineage, elem, depth + 1)


def input_pedigree() -> None:
    quantity = int(input())
    lineage = dict()
    parents = set()
    children = set()
    for _ in range(quantity - 1):
        child, parent = input().split()
        lineage[parent] = lineage.get(parent, []) + [child]
        parents.add(parent)
        children.add(child)
    root = parents.difference(children).pop()
    result = pedigree(quantity, lineage, root)
    print(*[f'{item[0]} {item[1]}' for item in result], sep='\n')


input_pedigree()
