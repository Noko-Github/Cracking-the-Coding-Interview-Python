class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.last = node
        else:
            self.last.next = node
            self.last = self.last.next

    def dequeue(self):
        if self.is_empty:
            return None

        node = self.head
        self.head = self.head.next

        return node

    def is_empty(self):
        return self.head is None
