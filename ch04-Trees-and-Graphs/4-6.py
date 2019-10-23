
class Node:
    def __init__(self, value):
        self.parent = None
        self.value = value
        self.left = None
        self.right = None


def get_left_most_progeny(node):
    while node is not None:
        if node.left is None:
            return node
        node = node.left

    return None


def get_successor(node):
    successor = get_left_most_progeny(node.right)
    if successor is None:
        parent = node.parent
        while parent is not None and parent.right == node:
            node = parent
            parent = parent.parent
        successor = parent

    return successor


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.left = node2
node2.parent = node1
node1.right = node3
node3.parent = node1

print(get_successor(node1).value)
