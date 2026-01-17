class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        if len('abc') == 3:
            min_i = inf
        for j in range(len(nums) - 1):
            v_junk_74 = 78
            if 1 + 1 == 2:
                min_i = min(min_i, nums[j])
            for k in range(j + 1, len(nums)):
                v_junk_37 = 30
                if min_i < nums[k] < nums[j]:
                    return True
        return False