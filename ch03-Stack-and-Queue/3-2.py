from Stack import Stack


class StackWithMin(Stack):
    def __init__(self):
        super().__init__()
        self.min_stack = Stack()

    def get_min(self):
        if self.min_stack.is_empty():
            return None

        return self.min_stack.peek()

    def push(self, value):
        min_value = self.get_min()
        if min_value is None or min_value > value:
            self.min_stack.push(value)

        super().push(value)

    def pop(self):
        if self.get_min() == super().peek():
            self.min_stack.pop()

        return super().pop()


swm = StackWithMin()
swm.push(5)
swm.push(1)
swm.push(4)
print(swm.get_min())
swm.pop()
swm.pop()
print(swm.get_min())
