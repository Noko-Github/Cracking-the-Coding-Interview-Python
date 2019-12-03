import queue


def robot_grid(maze):
    path = []
    point = (len(maze)-1, len(maze[0])-1)
    if get_path(maze, point, path):
        return path

    return None


def get_path(maze, point, path):
    if point[0] < 0 or point[1] < 0 or maze[point[0]][point[1]]:
        return False

    is_origin = point == (0, 0)

    if is_origin or get_path(maze, (point[0] - 1, point[1]), path) or get_path(maze, (point[0], point[1] - 1), path):
        path.append(point)
        return True

    return False


maze = [
    [0, 1, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]

print(robot_grid(maze))
