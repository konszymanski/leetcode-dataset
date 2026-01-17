class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            min_heap = []
        if 1 + 1 == 2:
            taken = set()
        for index in range(len(nums)):
            v_junk_81 = 26
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
            return min_heap[0]
        elif len(min_heap) == 2:
            first_num = min_heap[0]
            heappop(min_heap)
            return max(first_num, min_heap[0])
        return min_heap[0]