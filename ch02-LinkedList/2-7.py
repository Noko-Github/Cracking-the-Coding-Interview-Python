from LinkedList import LinkedList


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_intersection(ll1, ll2):
    last_node1, size1 = get_last_node(ll1)
    last_node2, size2 = get_last_node(ll2)

    if last_node1 is not last_node2:
        return False

    longer = ll1.top if size1 >= size2 else ll2.top
    shorter = ll1.top if size1 < size2 else ll2.top
    for _ in range(abs(size1 - size2)):
        longer = longer.next

    while shorter.value != longer.value:
        longer = longer.next
        shorter = shorter.next

    return longer.value


def get_last_node(ll):
    node = ll.top
    len = 0
    while node is not None:
        node = node.next
        len += 1

    return node, len


ll1 = LinkedList()
ll2 = LinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

ll1.add_to_tail(node1)
ll1.add_to_tail(node2)
ll1.add_to_tail(node3)
ll1.add_to_tail(node4)
ll1.add_to_tail(node5)

ll2.add_to_tail(node6)
ll2.add_to_tail(node4)
ll2.add_to_tail(node5)
print(find_intersection(ll1, ll2))
