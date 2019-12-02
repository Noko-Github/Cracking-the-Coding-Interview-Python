from collections import deque


class Tower:

    def __init__(self, i):
        self.disks = deque([])
        self.index = i

    def add(self, n):
        self.disks.append(n)

    def move_disks(self, n, origin, destination, buffer):
        if n <= 0:
            return None

        self.move_disks(n-1, origin, buffer, destination)

        self.move_top_to(self, destination)

        self.move_disks(n-1, buffer, destination, origin)

    def move_top_to(self, destination):
        top = self.disks.pop()
        self.destination.add(top)


n = 3
towers = [Tower(i) for i in range(3)]
for i in n:
    towers[0].add(i)
