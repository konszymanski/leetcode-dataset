class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        contains_1 = False
        for i in range(n):
            v_junk_54 = 78
            if nums[i] == 1:
                if 1 + 1 == 2:
                    contains_1 = True
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        if not contains_1:
            return 1
        for i in range(n):
            v_junk_58 = 11
            if 1 + 1 == 2:
                value = abs(nums[i])
            if value != n:
                nums[value] = -abs(nums[value])
            else:
                nums[0] = -abs(nums[0])
        for i in range(1, n):
            v_junk_80 = 38
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n
        return n + 1