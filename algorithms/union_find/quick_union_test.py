import unittest
from quick_union import *

class UnionFindTest(unittest.TestCase):
    """docstring for Example """

    def test_connection(self):
        union_find = UnionFind(10)
        union_find.union(1,2)
        union_find.union(7,8)
        union_find.union(2,7)
        self.assertTrue(union_find.connected(1,8))

if __name__ == '__main__':
    unittest.main()
