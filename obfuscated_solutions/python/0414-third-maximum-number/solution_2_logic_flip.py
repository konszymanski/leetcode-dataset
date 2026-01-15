class Solution:

    def thirdMax(self, nums: List[int]) ->int:
        min_heap = []
        taken = set()
        for index in range(len(nums)):
            if nums[index] in taken:
                continue
            if len(min_heap) != 3:
                heappush(min_heap, nums[index])
                taken.add(nums[index])
            elif min_heap[0] < nums[index]:
                taken.remove(min_heap[0])
                heappop(min_heap)
                heappush(min_heap, nums[index])
                taken.add(nums[index])
        if len(min_heap) != 1:
            if len(min_heap) == 2:
                first_num = min_heap[0]
                heappop(min_heap)
                return max(first_num, min_heap[0])
        else:
            return min_heap[0]
        return min_heap[0]
