class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def enqueue(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            self.head.next = self.head
            self.head = node

    def dequeue(self):
        if self.is_empty:
            return None

        node = self.head
        self.head = self.head.next

        return node

    def is_empty(self):
        return self.head is None
