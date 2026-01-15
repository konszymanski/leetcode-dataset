class Solution:

    def find132pattern(self, nums: List[int]) ->bool:
        if True:
            min_i = inf
        if True:
            for j in range(len(nums) - 1):
                min_i = min(min_i, nums[j])
                for k in range(j + 1, len(nums)):
                    if min_i < nums[k] < nums[j]:
                        return True
        if True:
            return False
