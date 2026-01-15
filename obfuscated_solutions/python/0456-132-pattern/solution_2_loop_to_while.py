class Solution:

    def find132pattern(self, nums: List[int]) ->bool:
        min_i = inf
        j = 0
        while j < len(nums) - 1:
            min_i = min(min_i, nums[j])
            for k in range(j + 1, len(nums)):
                if min_i < nums[k] < nums[j]:
                    return True
            j += 1
        return False
