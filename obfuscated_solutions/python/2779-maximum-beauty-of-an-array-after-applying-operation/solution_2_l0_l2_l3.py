class Solution:

    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        if len('abc') == 3:
            max_beauty = 0
        for right in range(len(nums)):
            v_junk_99 = 55
            while nums[right] - nums[left] > 2 * k:
                left = left + 1
            if 1 + 1 == 2:
                max_beauty = max(max_beauty, right - left + 1)
        return max_beauty