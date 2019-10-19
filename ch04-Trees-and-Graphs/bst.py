from random import randint


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, value_list=[]):
        self.root = None
        for value in value_list:
            node = Node(value)
            self.insert(node)

    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            self._insert(node, self.root)

    def _insert(self, new_node, current_node):
        if new_node.value == current_node.value:
            print("Value: {} is alread added in tree.".format(new_node.value))
            return True

        if new_node.value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert(new_node, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert(new_node, current_node.right)

    def add_random_nodes(self, num_nodes=100, min_value=1, max_value=1000):
        for _ in range(num_nodes):
            current_node = Node(randint(min_value, max_value))
            self.insert(current_node)
