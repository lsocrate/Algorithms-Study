import unittest
from array_inversions import *

class ArrayInversionsTest(unittest.TestCase):
    """Tests for ArrayInversions"""

    def test_array_inversion(self):
        array_inversions = ArrayInversions([1,3,5,2,4,6])
        result = array_inversions.inversions()
        self.assertEqual(3, result)

if __name__ == '__main__':
    unittest.main()
