from LinkedList import LinkedList


def kth_to_last(top, k):
    p1 = top
    p2 = top

    for _ in range(k):
        if p1 == None:
            return None
        p1 = p1.next

    while p1 is not None:
        p1 = p1.next
        p2 = p2.next

    return p2


ll = LinkedList()
ll.add_to_tail(1)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(4)

print(kth_to_last(ll.top, 2).value)
