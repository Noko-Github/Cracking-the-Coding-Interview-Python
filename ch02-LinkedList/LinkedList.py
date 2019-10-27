class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.top = self.tail = None

    def add_to_tail(self, value):
        node = Node(value)
        if self.top is None:
            self.top = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
