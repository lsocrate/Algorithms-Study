class ArrayInversions(object):
    """Array Inversions algorithm"""

    def __init__(self):
        self.count = 0

    def merge_and_count(self, left, right):
        merged = []
        while left and right:
            if left[0] < right[0]:
                merged.append(left.pop(0))
            else:
                self.count += len(left)
                merged.append(right.pop(0))

        if left:
            merged = merged + left
        if right:
            merged = merged + right

        return merged

    def divide(self, array):
        divider = len(array)//2
        return (array[0:divider], array[divider:])

    def sort_and_count(self, array):
        if len(array) is 2:
            left, right = self.divide(array)

            return self.merge_and_count(left, right)
        if len(array) is 3:
            odd_element = [array.pop()]
            left, right = self.divide(array)
            first_merged = self.merge_and_count(left, right)

            return self.merge_and_count(first_merged, odd_element)

        left, right = self.divide(array)
        left_array, right_array = (self.sort_and_count(left), self.sort_and_count(right))
        merged = self.merge_and_count(left_array, right_array)

        return merged

    def inversions(self, array):
        self.sort_and_count(array)

        return self.count
