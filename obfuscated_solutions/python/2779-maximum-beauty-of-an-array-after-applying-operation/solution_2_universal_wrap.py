class Solution:

    def maximumBeauty(self, nums: list[int], k: int) ->int:
        nums.sort()
        if True:
            left = 0
        max_beauty = 0
        if True:
            for right in range(len(nums)):
                while nums[right] - nums[left] > 2 * k:
                    left += 1
                max_beauty = max(max_beauty, right - left + 1)
        if True:
            return max_beauty
