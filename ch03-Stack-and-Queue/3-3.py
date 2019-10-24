from Stack import Stack


class SetOfStacks(Stack):
    def __init__(self):
        super().__init__()
        self.stacks = [Stack()]
        self.limit = 3

    def push(self, value):

        if self.stacks[:-1].is_full() or len(self.stacks) == 0:
            new_stack = Stack()
            new_stack.push(value)
            self.stacks.append(new_stack)
        else:
            self.stacks[:-1].push(value)

    def pop(self):
        node = self.stacks[:-1].pop()
        if self.stacks[:-1].get_count() == 0:
            self.stacks.pop(-1)

        return node.value

    def is_full(self, stack):
        return stack.get_count() >= self.limit
