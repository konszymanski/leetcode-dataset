class Solution:

    def canSortArray(self, nums):
        n = len(nums)
        values = nums.copy()
        i = 0
        while i < n:
            for j in range(n - i - 1):
                if values[j] <= values[j + 1]:
                    continue
                elif bin(values[j]).count('1') == bin(values[j + 1]).count('1'
                    ):
                    values[j], values[j + 1] = values[j + 1], values[j]
                else:
                    return False
            i += 1
        return True
