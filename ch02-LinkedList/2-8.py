class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_beginning(node):
    fast = slow = node
    while fast is not None and slow is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            break

    slow = node
    while fast is not slow:
        slow = slow.next
        fast = fast.next

    return fast


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node4

node = find_beginning(node1)
print(node.value)
