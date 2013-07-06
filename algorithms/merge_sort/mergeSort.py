class MergeSort(object):
    """Merge sort algorithm"""

    def merge(self, a, b):
        merged = []
        while a and b:
            if a[0] < b[0]:
                merged.append(a.pop(0))
            else:
                merged.append(b.pop(0))

        if a:
            merged = merged + a
        if b:
            merged = merged + b

        return merged

    def divide(self, numbers):
        divider = len(numbers)//2
        return (numbers[0:divider], numbers[divider:])

    def sort(self, numbers):
        if len(numbers) is 2:
            return self.merge([numbers[0]], [numbers[1]])
        if len(numbers) is 3:
            odd_element = numbers.pop()
            first_merged = self.merge([numbers[0]], [numbers[1]])
            return self.merge(first_merged, [odd_element])

        divided = self.divide(numbers)
        sorted_divided = (self.sort(divided[0]), self.sort(divided[1]))
        merged = self.merge(sorted_divided[0], sorted_divided[1])

        return merged
