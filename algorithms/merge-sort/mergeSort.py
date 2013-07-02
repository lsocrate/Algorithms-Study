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
        if len(numbers) < 3:
            return self.merge([numbers[0]], [numbers[1]])
        else:
            divided = self.divide(numbers)
            sortedDivided = (self.sort(divided[0]), self.sort(divided[1]))
            merged = self.merge(sortedDivided[0], sortedDivided[1])

            return merged
