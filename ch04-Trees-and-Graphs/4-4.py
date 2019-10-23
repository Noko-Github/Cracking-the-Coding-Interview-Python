from bst import BST


def check_height(node):
    if node is None:
        return -1

    left_height = check_height(node.left)
    right_height = check_height(node.left)

    height_diff = left_height - right_height
    if abs(height_diff) > 1:
        return False
    else:
        return max(left_height, right_height) + 1


def is_balanced(root_node):
    if root_node is None:
        return False

    return check_height(root_node) is not False


tree = BST()
tree.add_random_nodes()
print(is_balanced(tree.root))
