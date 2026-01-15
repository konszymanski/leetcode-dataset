class Solution:

    def canSortArray(self, nums):
        n = len(nums)
        values = nums.copy()
        for i in range(n):
            for j in range(n - i - 1):
                if values[j] > values[j + 1]:
                    if bin(values[j]).count('1') != bin(values[j + 1]).count(
                        '1'):
                        return False
                    else:
                        values[j], values[j + 1] = values[j + 1], values[j]
                else:
                    continue
        return True
