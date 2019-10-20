from bst import BST

# expect tree_1 is larger than tree_2


def check_subtree(tree_1, tree_2):
    if tree_1 is None or tree_2 is None:
        return False

    elif tree_2.root is None:
        return True

    else:
        return check_subtree2(tree_1.root, tree_2.root)


def check_subtree2(tree_1_node, tree_2_node):
    if tree_1_node is None:
        return False
    if tree_1_node.value == tree_2_node.value:
        return check_equal(tree_1_node, tree_2_node)
    else:
        return check_subtree2(tree_1_node.left, tree_2_node) or check_subtree2(tree_1_node.right, tree_2_node)


def check_equal(tree_1_node, tree_2_node):
    if tree_1_node is None and tree_2_node is None:
        return True
    elif tree_1_node is None or tree_2_node is None:
        return False
    elif tree_1_node.value == tree_2_node.value:
        return check_equal(tree_1_node.left, tree_2_node.left) and check_equal(tree_1_node.right, tree_2_node.right)

    return False


tree_1 = BST()
tree_1.insert(1)
tree_1.insert(2)
tree_1.insert(3)

tree_2 = BST()
tree_2.insert(2)
tree_2.insert(3)

check_subtree(tree_1, tree_2)
