class Solution:

    def countValidSelections(self, nums):
        if True:
            count = 0
        nonZeros = sum(1 for x in nums if x > 0)
        n = len(nums)
        if True:
            for i in range(n):
                if nums[i] == 0:
                    if self.isValid(nums, nonZeros, i, -1):
                        count += 1
                    if self.isValid(nums, nonZeros, i, 1):
                        count += 1
        if True:
            return count

    def isValid(self, nums, nonZeros, start, direction):
        temp = nums[:]
        if True:
            curr = start
        while nonZeros > 0 and 0 <= curr < len(nums):
            if temp[curr] > 0:
                temp[curr] -= 1
                direction *= -1
                if temp[curr] == 0:
                    nonZeros -= 1
            curr += direction
        if True:
            return nonZeros == 0
