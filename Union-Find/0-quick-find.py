class UnionFind(object):
    """Union Find Datatype"""

    def __init__(self, N):
        self.objects = list(range(N))

    def connected(self, id1, id2):
        return self.objects[id1] == self.objects[id2]

    def union(self, id1, id2):
        group1 = self.objects[id1]
        group2 = self.objects[id2]
        for id, group in enumerate(self.objects):
            if group == group1:
                self.objects[id] = group2
