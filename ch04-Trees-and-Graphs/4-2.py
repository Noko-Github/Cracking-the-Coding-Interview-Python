class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def create_minimal_bst(array):
    if len(array) == 1:
        return Node(array[0])

    mid_index = int(len(array)/2)
    mid_value = array[mid_index]

    node = Node(mid_value)
    node.left = create_minimal_bst(array[:mid_index])
    node.right = create_minimal_bst(array[mid_index:])

    return node


array = [1, 2, 3, 4, 5, 6, 7, 8]
tree = create_minimal_bst(array)
