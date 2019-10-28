from LinkedList import LinkedList


def delete(n):
    if n is None:
        return None

    next = n.next
    n.value = next.value
    n.next = next.next
    return True


ll = LinkedList()
ll.add_to_tail(1)
ll.add_to_tail(2)
ll.add_to_tail(3)
delete(ll.top.next)
print(ll.top.value)
print(ll.top.next.value)
print(ll.top.next.next)
