from stack import Stack
from bst import BST

last_printed = None


def check_bst(node):
    global last_printed

    if node is None:
        return True

    # check left Node(due to in-order)
    if check_bst(node.left) is False:
        return False

    if last_printed is not None and last_printed >= node.value:
        return False

    last_printed = node.value

    if check_bst(node.right) is not False:
        return False

    return True


tree = BST()
tree.add_random_nodes()

print(check_bst(tree.root))
