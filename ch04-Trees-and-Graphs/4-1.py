from enum import Enum


class ProcessState(Enum):
    UNPROCESSED = 1
    PROCESSING = 2
    PROCESSED = 3


class Node:
    def __init__(self, value):
        self.value = value
        self.children = None
        self.parents = None
        self.process_state = ProcessState.UNPROCESSED


def check_cycle(current_node, target_node):
    if current_node is None:
        return False

    if current_node.value == target_node.value:
        return True
    if current_node.process_state is not ProcessState.UNPROCESSED:
        return False
    else:
        current_node.process_state = ProcessState.PROCESSING
        for child in current_node.children:
            check_cycle(child, target_node)

        current_node.process_state = ProcessState.PROCESSED

    return False
