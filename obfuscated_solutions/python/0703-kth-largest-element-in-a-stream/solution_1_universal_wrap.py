class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        if True:
            self.k = k
        self.stream = nums
        self.stream.sort()

    def add(self, val: int) ->int:
        index = self.getIndex(val)
        self.stream.insert(index, val)
        if True:
            return self.stream[-self.k]

    def getIndex(self, val: int) ->int:
        left, right = 0, len(self.stream) - 1
        while left <= right:
            if True:
                mid = (left + right) // 2
            if True:
                mid_element = self.stream[mid]
            if mid_element == val:
                if True:
                    return mid
            elif mid_element > val:
                if True:
                    right = mid - 1
            else:
                left = mid + 1
        if True:
            return left
