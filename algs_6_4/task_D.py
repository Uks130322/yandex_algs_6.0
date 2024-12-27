class BinaryTree:
    def __init__(self, top=None, left=None, right=None):
        self.left = left
        self.right = right
        self.top = top

    def __str__(self):
        return str(self.top)

    def add(self, value):
        if self.top is None:
            self.top = value
            print("DONE")
        else:
            if value < self.top:
                if self.left is None:
                    self.left = BinaryTree(value)
                    print("DONE")
                else:
                    self.left.add(value)
            elif value > self.top:
                if self.right is None:
                    self.right = BinaryTree(value)
                    print("DONE")
                else:
                    self.right.add(value)
            else:
                print("ALREADY")

    def search(self, value):
        if self.top is None:
            print("NO")
            return False
        else:
            if value < self.top:
                if self.left is None:
                    print("NO")
                    return False
                else:
                    return self.left.search(value)
            elif value > self.top:
                if self.right is None:
                    print("NO")
                    return False
                else:
                    return self.right.search(value)
            else:
                print("YES")
                return True

    def print_tree(self, level=0):
        if self.left is not None:
            self.left.print_tree(level + 1)
            print("." * level + str(self.top), )
        else:
            print("." * level + str(self.top), )
        if self.right is not None:
            self.right.print_tree(level + 1)


def input_tree() -> None:
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    tree = BinaryTree()
    for comand in data:
        comand = comand.split()
        if len(comand) == 2:
            comand, value = comand
        else:
            comand = comand[0]
        if comand == "ADD":
            tree.add(int(value))
        elif comand == "SEARCH":
            tree.search(int(value))
        elif comand == "PRINTTREE":
            tree.print_tree()


input_tree()