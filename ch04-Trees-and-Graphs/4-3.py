from queue import Queue
from bst import BST


def dfs(node, height, linked_list_arr):
    if node is None:
        return False

    if len(linked_list_arr) == height:
        new_linked_list = Queue()
        linked_list_arr.append(new_linked_list)

    linked_list_arr[height].enqueue(node.value)
    dfs(node.left, height+1, linked_list_arr)
    dfs(node.right, height+1, linked_list_arr)


def create_linked_list_from_bst(tree):
    linked_list_arr = []
    height = 0
    dfs(tree.root, height, linked_list_arr)
    return linked_list_arr


bst = BST()
bst.add_random_nodes(10, 1, 10)
print(len(create_linked_list_from_bst(bst)))
