from Stack import Stack
from LinkedList import LinkedList


def is_palindrome(node):
    first = slow = node
    stack = Stack()

    while first.next is not None:
        slow = slow.next
        first = first.next.next
        stack.push(slow.value)

    if first is not None:
        slow = slow.next
        stack.pop()

    while slow is not None and stack.is_empty() is False:
        if slow.value != stack.pop():
            return False
        slow = slow.next

    return True


ll = LinkedList()
ll.add_to_tail(1)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(2)
ll.add_to_tail(1)

print(is_palindrome(ll.top))
