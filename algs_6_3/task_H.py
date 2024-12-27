class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.prefix_sums = [0]

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.prefix_sums.append(self.prefix_sums[-1] + value)

    def pop(self) -> int:
        self.prefix_sums.pop()
        return self.stack.pop()

    def get_prefix_sum(self, quantity: int) -> int:
        return self.prefix_sums[-1] - self.prefix_sums[-quantity - 1]


def input_stack() -> None:
    number = int(input())
    mystack = Stack()
    result = []
    for _ in range(number):
        action = input()
        if action[0] == '+':
            mystack.push(int(action[1:]))
        elif action[0] == '-':
            result.append(mystack.pop())
        elif action[0] == '?':
            result.append(mystack.get_prefix_sum(int(action[1:])))
    print(*result, sep="\n")


input_stack()
