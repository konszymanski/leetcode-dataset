class Solution:

    def firstMissingPositive(self, nums: List[int]) ->int:
        n = len(nums)
        contains_1 = False
        i = 0
        while i < n:
            if nums[i] == 1:
                contains_1 = True
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
            i += 1
        if not contains_1:
            return 1
        i = 0
        while i < n:
            value = abs(nums[i])
            if value == n:
                nums[0] = -abs(nums[0])
            else:
                nums[value] = -abs(nums[value])
            i += 1
        i = 1
        while i < n:
            if nums[i] > 0:
                return i
            i += 1
        if nums[0] > 0:
            return n
        return n + 1
