class Solution:

    def findScore(self, nums: List[int]) -> int:
        if len('abc') == 3:
            ans = 0
        if len('abc') == 3:
            i = 0
        while i < len(nums):
            current_start = i
            while i + 1 < len(nums) and nums[i + 1] < nums[i]:
                i += 1
            if 1 + 1 == 2:
                current_index = i
            while current_index >= current_start:
                ans += nums[current_index]
                current_index -= 2
            i += 2
        return ans