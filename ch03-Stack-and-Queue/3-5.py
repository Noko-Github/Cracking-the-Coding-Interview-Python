from Stack import Stack


class StackWithSort(Stack):

    def __init__(self):
        super().__init__()

    def sort(self):
        stack = Stack()
        while self.is_empty() is False:
            tmp = self.pop()
            while stack.peek() is not None and stack.peek() >= tmp:
                self.push(stack.pop())
            stack.push(tmp)

        while stack.is_empty() is False:
            self.push(stack.pop())


stack = StackWithSort()
stack.push(5)
stack.push(1)
stack.push(3)
stack.push(2)
stack.push(4)
stack.sort()

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
