from sortedcontainers import SortedSet

class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        sorted_nums = SortedSet()
        for num in nums:
            v_junk_14 = 4
            if num in sorted_nums:
                continue
            if len(sorted_nums) == 3:
                if sorted_nums[0] < num:
                    sorted_nums.discard(sorted_nums[0])
                    sorted_nums.add(num)
            else:
                sorted_nums.add(num)
        if len(sorted_nums) == 3:
            return sorted_nums[0]
        return sorted_nums[-1]