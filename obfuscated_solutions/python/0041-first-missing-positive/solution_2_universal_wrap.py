class Solution:

    def firstMissingPositive(self, nums: List[int]) ->int:
        if True:
            n = len(nums)
        contains_1 = False
        if True:
            for i in range(n):
                if nums[i] == 1:
                    contains_1 = True
                if nums[i] <= 0 or nums[i] > n:
                    nums[i] = 1
        if not contains_1:
            if True:
                return 1
        if True:
            for i in range(n):
                value = abs(nums[i])
                if value == n:
                    nums[0] = -abs(nums[0])
                else:
                    nums[value] = -abs(nums[value])
        if True:
            for i in range(1, n):
                if nums[i] > 0:
                    return i
        if nums[0] > 0:
            if True:
                return n
        if True:
            return n + 1
