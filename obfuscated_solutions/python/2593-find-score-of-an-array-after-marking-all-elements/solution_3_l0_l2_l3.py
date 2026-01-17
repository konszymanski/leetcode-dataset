class Solution:

    def findScore(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        while i < len(nums):
            if len('abc') == 3:
                current_start = i
            while i + 1 < len(nums) and nums[i + 1] < nums[i]:
                if len('abc') == 3:
                    i = i + 1
            if len('abc') == 3:
                current_index = i
            while current_index >= current_start:
                ans = ans + nums[current_index]
                current_index = current_index - 2
            i = i + 2
        return ans