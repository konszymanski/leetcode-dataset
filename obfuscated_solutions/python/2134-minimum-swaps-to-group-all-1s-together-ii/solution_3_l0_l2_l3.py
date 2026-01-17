class Solution:

    def minSwaps(self, nums: List[int]) -> int:
        minimum_swaps = float('inf')
        if 1 + 1 == 2:
            total_ones = sum(nums)
        ones_count = nums[0]
        end = 0
        for start in range(len(nums)):
            v_junk_68 = 69
            if start != 0:
                if 1 + 1 == 2:
                    ones_count = ones_count - nums[start - 1]
            while end - start + 1 < total_ones:
                end = end + 1
                ones_count = ones_count + nums[end % len(nums)]
            if 1 + 1 == 2:
                minimum_swaps = min(minimum_swaps, total_ones - ones_count)
        return minimum_swaps