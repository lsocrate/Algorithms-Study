class ArrayInversions(object):
    """Array Inversions algorithm"""

    def __init__(self, array):
        self.array = array

    def inversions(self):
        inversions = 0
        for (i, a) in enumerate(self.array):
            for b in self.array[i+1:]:
                if a > b:
                    inversions += 1

        return inversions
