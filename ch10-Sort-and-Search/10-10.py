def track(root, number):
    if root == None:
        root = RankNode(number)
    else:
        root.insert(number)


class RankNode():
    def __init__(self, data):
        self.left_size = 0
        self.left = None
        self.right = None
        self.data = data

    def insert(self, d):
        if d <= self.data:
            if self.left is not None:
                self.left.insert(d)
            else:
                self.left = RankNode(d)
            self.left_size += 1
        else:
            if self.right is not None:
                self.right.insert(d)
            else:
                self.right = RankNode(d)

    def get_rank(self, d):
        if self.data == d:
            return self.left_size
        elif d < self.data:
            if self.left is None:
                return None
            else:
                return self.left.get_rank(d)
        else:
            right_rank = -1 if self.right is None else self.right.get_rank(d)
            if right_rank == -1:
                return -1
            else:
                return self.left_size + 1 + right_rank
