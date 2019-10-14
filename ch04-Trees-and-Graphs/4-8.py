def common_ancestor(node_1, node_2):
    delta = get_depth(node_1) - get_depth(node_2)
    first = node_2 if delta > 0 else node_1
    second = node_1 if delta > 0 else node2_

    second = go_up_by(second, delta)

    while(first != second and first is not None and second is not None):
        first = first.parent
        second = second.parent

    return first if first is None or second is None else first


def go_up_by(node, delta):
    while delta > 0 and node is not None:
        node = node.parent
        delta -= 1

    return node


def get_depth(node):
    depth = 0
    while node is not None:
        node = node.parent
        depth += 1

    return depth
