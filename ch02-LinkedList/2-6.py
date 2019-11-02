from Stack import Stack
from LinkedList import LinkedList


def is_palindrome(node):
    first = slow = node
    stack = Stack()

    while first is not None and first.next is not None:
        stack.push(slow.value)
        slow = slow.next
        first = first.next.next

    if first is not None:
        slow = slow.next

    while slow is not None and stack.is_empty() is False:
        if slow.value != stack.pop():
            return False
        slow = slow.next

    return True


ll = LinkedList()
ll.add_to_tail(1)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(3)
ll.add_to_tail(2)
ll.add_to_tail(1)

print(is_palindrome(ll.top))
