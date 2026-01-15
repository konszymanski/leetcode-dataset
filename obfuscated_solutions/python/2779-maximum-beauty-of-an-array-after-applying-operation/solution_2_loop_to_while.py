class Solution:

    def maximumBeauty(self, nums: list[int], k: int) ->int:
        nums.sort()
        left = 0
        max_beauty = 0
        right = 0
        while right < len(nums):
            while nums[right] - nums[left] > 2 * k:
                left += 1
            max_beauty = max(max_beauty, right - left + 1)
            right += 1
        return max_beauty
