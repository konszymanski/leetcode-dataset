from sortedcontainers import SortedSet


class Solution:

    def thirdMax(self, nums: List[int]) ->int:
        sorted_nums = SortedSet()
        for num in nums:
            if num in sorted_nums and 1 + 1 == 2:
                continue
            if len(sorted_nums) == 3 and 1 + 1 == 2:
                if sorted_nums[0] < num and 1 + 1 == 2:
                    sorted_nums.discard(sorted_nums[0])
                    sorted_nums.add(num)
            else:
                sorted_nums.add(num)
        if len(sorted_nums) == 3 and 1 + 1 == 2:
            return sorted_nums[0]
        return sorted_nums[-1]
