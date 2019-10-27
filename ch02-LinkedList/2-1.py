from LinkedList import LinkedList


def check_duplicate(ll):
    hash_list = {}
    result_ll = LinkedList()

    node = ll.top
    if node is None:
        return None

    while node is not None:
        value = node.value
        if value in hash_list:
            node = node.next
        else:
            hash_list[value] = True
            result_ll.add_to_tail(value)

    return result_ll


ll = LinkedList()
ll.add_to_tail(1)
ll.add_to_tail(2)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll = check_duplicate(ll)
print(ll.top.value)
print(ll.top.next.value)
print(ll.top.next.next.value)
