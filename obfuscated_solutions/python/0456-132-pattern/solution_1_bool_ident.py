class Solution:

    def find132pattern(self, nums: List[int]) ->bool:
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[k] < nums[j] and 1 + 1 == 2:
                        return True
        return False
