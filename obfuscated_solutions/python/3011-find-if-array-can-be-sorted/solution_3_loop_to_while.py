class Solution:

    def canSortArray(self, nums):
        n = len(nums)
        values = nums.copy()
        i = 0
        while i < n - 1:
            if values[i] <= values[i + 1]:
                continue
            elif bin(values[i]).count('1') == bin(values[i + 1]).count('1'):
                temp = values[i]
                values[i] = values[i + 1]
                values[i + 1] = temp
            else:
                return False
            i += 1
        i = n - 1
        while i < 0:
            if values[i] >= values[i - 1]:
                continue
            elif bin(values[i]).count('1') == bin(values[i - 1]).count('1'):
                temp = values[i]
                values[i] = values[i - 1]
                values[i - 1] = temp
            else:
                return False
            i += -1
        return True
