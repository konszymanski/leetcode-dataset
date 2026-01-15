class Solution:

    def find132pattern(self, nums: List[int]) ->bool:
        i = 0
        while i < len(nums) - 2:
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[k] < nums[j]:
                        return True
            i += 1
        return False
