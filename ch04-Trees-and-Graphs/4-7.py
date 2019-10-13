class State:
    UNCOMPLETED = 0
    PROCESSING = 1
    COMPLETED = 2


class Node:
    def __init__(self, id):
        self.id = id
        self.childen = []
        self.state = State.UNCOMPLETED


def build_order(project_list, dependency_list):
    build_list = []
    graph = {}

    # create graph
    for id in project_list:
        graph[id] = Node(id)

    for dependency in dependency_list:
        dep_from = dependency[0]
        dep_to = dependency[1]

        graph[dep_from].childen.append(graph[dep_to])

    # start topological sorting
    for id in project_list:
        node = graph[id]
        if not dfs(build_list, node):
            return None

    return build_list


def dfs(build_list, node):
    if node.state == State.PROCESSING:
        print(node.id)
        return False

    if node.state == State.UNCOMPLETED:
        node.state = State.PROCESSING
        for child in node.childen:
            if not dfs(build_list, child):
                return False
        build_list.append(node.id)
        node.state = State.COMPLETED

    return True


if __name__ == '__main__':
    project_list = ['a', 'b', 'c', 'd', 'e', 'f']
    dependency_list = [('d', 'a'), ('b', 'f'), ('d', 'b'), ('a', 'f'), ('c', 'd')]

    print(build_order(project_list, dependency_list))
