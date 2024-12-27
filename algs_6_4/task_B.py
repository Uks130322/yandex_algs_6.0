
POSTERITY = dict()


def pedigree(quantity: int, lineage: dict[str: set[str]], root: str) -> str:
    go_deep(lineage, root)
    return sorted([(key, value) for key, value in POSTERITY.items()], key=lambda x: x[0])


def go_deep(lineage: dict, key: str) -> None:
    if key not in lineage:
        POSTERITY[key] = 0
        return 0
    else:
        result = len(lineage.get(key, [])) + sum([go_deep(lineage, elem) for elem in lineage.get(key, [])])
        POSTERITY[key] = (POSTERITY.get(key, 0) + result)
        return result


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
