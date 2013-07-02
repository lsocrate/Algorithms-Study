import unittest
from mergeSort import *

class MergeSortTest(unittest.TestCase):
    """docstring for Example """

    def test_merge_sort_simple(self):
        mergeSort = MergeSort()
        result = mergeSort.sort([2,1])
        self.assertEqual([1,2], result)
        result2 = mergeSort.sort([1,2])
        self.assertEqual([1,2], result2)

    def test_merge_sort_complex(self):
        mergeSort = MergeSort()
        result = mergeSort.sort([5,4,1,8,7,2,6,3])
        self.assertEqual([1,2,3,4,5,6,7,8], result)


if __name__ == '__main__':
    unittest.main()
