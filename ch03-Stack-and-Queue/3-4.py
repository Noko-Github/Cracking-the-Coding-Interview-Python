from Stack import Stack


class MyQueue:
    def __init__(self):
        self.oldest_stack = Stack()
        self.newest_stack = Stack()

    def enqueue(self, value):
        self.newest_stack.push(value)

    def dequeue(self):
        if self.oldest_stack.is_empty():
            while self.newest_stack.is_empty() is False:
                value = self.newest_stack.pop()
                self.oldest_stack.push(value)

        return self.oldest_stack.pop()


queue = MyQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
