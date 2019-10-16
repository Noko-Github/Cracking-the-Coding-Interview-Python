"""
Problem:
Solution:
"""


def get_left_most_progeny(node):
    while node is not None:
        if node.left is None:
            return node
        node = node.left

    return None


def get_successor(node):
    successor = get_left_most_progeny(node.right_node)
    if successor is None:
        parent = node.parent
        while parent is None or parent.left != node:
            parent = node.parent
        successor = parent

    return successor
