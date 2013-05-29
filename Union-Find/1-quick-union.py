class UnionFind(object):
    """Union Find Datatype"""

    def __init__(self, N):
        self.objects = list(range(N))

    def connected(self, id1, id2):
        return self._root(id1) == self._root(id2)

    def union(self, id1, id2):
        self.objects[self._root(id1)] = self._root(id2)

    def _root(self, id):
        while id is not self.objects[id]:
            id = self.objects[id]

        return id
