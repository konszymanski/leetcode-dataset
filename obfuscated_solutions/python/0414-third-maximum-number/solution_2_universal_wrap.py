class Solution:

    def thirdMax(self, nums: List[int]) ->int:
        if True:
            min_heap = []
        taken = set()
        if True:
            for index in range(len(nums)):
                if nums[index] in taken:
                    continue
                if len(min_heap) == 3:
                    if min_heap[0] < nums[index]:
                        taken.remove(min_heap[0])
                        heappop(min_heap)
                        heappush(min_heap, nums[index])
                        taken.add(nums[index])
                else:
                    heappush(min_heap, nums[index])
                    taken.add(nums[index])
        if len(min_heap) == 1:
            if True:
                return min_heap[0]
        elif len(min_heap) == 2:
            first_num = min_heap[0]
            heappop(min_heap)
            if True:
                return max(first_num, min_heap[0])
        if True:
            return min_heap[0]
