class UnionFind(object):
    """Union Find Datatype"""

    def __init__(self, N):
        self.objects = list(range(N))
        self.size = [1] * N

    def connected(self, id1, id2):
        return self._root(id1) == self._root(id2)

    def union(self, id1, id2):
        rootId1 = self._root(id1)
        rootId2 = self._root(id2)

        if self.size[rootId1] < self.size[rootId2] :
            self.objects[rootId1] = rootId2
            self.size[rootId2] = self.size[rootId1] + self.size[rootId2]
        else :
            self.objects[rootId2] = rootId1
            self.size[rootId1] = self.size[rootId1] + self.size[rootId2]

    def _root(self, id):
        while id is not self.objects[id]:
            id = self.objects[id]

        return id
