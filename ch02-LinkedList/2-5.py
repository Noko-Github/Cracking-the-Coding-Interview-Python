from LinkedList import LinkedList


def add_lists(node1, node2):
    result = LinkedList()
    carry = 0
    while node1 is not None or node2 is not None:
        value1 = node1.value if node1 is not None else 0
        value2 = node2.value if node2 is not None else 0

        value = value1 + value2 + carry
        result.add_to_tail(value % 10)
        carry = 1 if value/10 >= 1 else 0

        if node1 is not None:
            node1 = node1.next
        if node2 is not None:
            node2 = node2.next

    return result


ll1 = LinkedList()
ll2 = LinkedList()

ll1.add_to_tail(1)
ll1.add_to_tail(2)
ll1.add_to_tail(3)

ll2.add_to_tail(8)
ll2.add_to_tail(9)

result = add_lists(ll1.top, ll2.top)
print(result.top.value)
print(result.top.next.value)
print(result.top.next.next.value)
