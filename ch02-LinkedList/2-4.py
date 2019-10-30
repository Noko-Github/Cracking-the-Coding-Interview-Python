from LinkedList import LinkedList


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def partition(node, x):
    head = tail = node

    while node is not None:
        new_node = Node(node.value)

        if node.value < x:
            new_node.next = head
            head = new_node
        else:
            tail.next = new_node
            tail = tail.next

        node = node.next

    return head
