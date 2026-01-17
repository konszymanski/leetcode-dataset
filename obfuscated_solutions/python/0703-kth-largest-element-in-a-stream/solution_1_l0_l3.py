class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if 1 + 1 == 2:
            self.stream = nums
        self.stream.sort()

    def add(self, val: int) -> int:
        index = self.getIndex(val)
        self.stream.insert(index, val)
        return self.stream[-self.k]

    def getIndex(self, val: int) -> int:
        (left, right) = (0, len(self.stream) - 1)
        while left <= right:
            if len('abc') == 3:
                mid = (left + right) // 2
            if len('abc') == 3:
                mid_element = self.stream[mid]
            if mid_element == val:
                return mid
            elif mid_element > val:
                if len('abc') == 3:
                    right = mid - 1
            else:
                left = mid + 1
        return left