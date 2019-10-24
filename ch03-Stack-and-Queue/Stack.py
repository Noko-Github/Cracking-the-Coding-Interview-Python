class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.count += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            node = self.head
            self.head = self.head.next
            self.count -= 1

        return node.value

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.value

    def is_empty(self):
        return self.head is None

    def get_count(self):
        return self.count
