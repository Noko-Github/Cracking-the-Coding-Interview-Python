def get_rank(node, x):
    if node.value == x:
        return node.left_size()
    if node.value > x:
        return get_rank(node.left, x)
