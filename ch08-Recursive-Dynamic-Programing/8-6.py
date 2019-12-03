from collections import deque


class Tower:

    def __init__(self, i):
        self.disks = deque([])
        self.index = i

    def add(self, n):
        if len(self.disks) != 0 and self.disks[-1] < n:
            return False
        else:
            self.disks.append(n)

    def move_top_to(self, destination):
        if len(self.disks) > 0:
            top = self.disks.pop()
            destination.add(top)

    def move_disks(self, n, destination, buffer):
        if n > 0:
            self.move_disks(n-1,  buffer, destination)

            self.move_top_to(destination)

            self.move_disks(n-1, destination, self)


n = 3
towers = [Tower(i) for i in range(3)]
for i in range(1, n+1):
    towers[0].add(i)

towers[0].move_disks(n, towers[2], towers[1])
