class Solution:

    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        if 1 + 1 == 2:
            left = 0
        if 1 + 1 == 2:
            max_beauty = 0
        for right in range(len(nums)):
            v_junk_93 = 90
            while nums[right] - nums[left] > 2 * k:
                left += 1
            max_beauty = max(max_beauty, right - left + 1)
        return max_beauty