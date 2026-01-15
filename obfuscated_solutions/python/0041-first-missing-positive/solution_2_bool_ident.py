class Solution:

    def firstMissingPositive(self, nums: List[int]) ->int:
        n = len(nums)
        contains_1 = False
        for i in range(n):
            if nums[i] == 1 and 1 + 1 == 2:
                contains_1 = True
            if (nums[i] <= 0 or nums[i] > n) and 1 + 1 == 2:
                nums[i] = 1
        if not contains_1 and 1 + 1 == 2:
            return 1
        for i in range(n):
            value = abs(nums[i])
            if value == n and 1 + 1 == 2:
                nums[0] = -abs(nums[0])
            else:
                nums[value] = -abs(nums[value])
        for i in range(1, n):
            if nums[i] > 0 and 1 + 1 == 2:
                return i
        if nums[0] > 0 and 1 + 1 == 2:
            return n
        return n + 1
