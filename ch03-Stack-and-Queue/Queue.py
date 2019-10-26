class Node:
    def __init__(self, value, order=None):
        self.value = value
        self.order = order

    def set_order(self, order):
        self.order = order


class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def enqueue(self, value):
        self.size += 1
        node = Node(value, self.size)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def dequeue(self):
        self.size -= 1
        if self.head is None:
            return None
        else:
            node = self.head
            self.head = self.head.next
            return node.value

    def get_size(self):
        return self.size
