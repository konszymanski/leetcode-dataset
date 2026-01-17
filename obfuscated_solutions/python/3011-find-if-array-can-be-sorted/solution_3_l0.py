class Solution:
    def canSortArray(self, nums):
        n = len(nums)
        values = nums.copy()
        for i in range(n - 1):
            if values[i] <= values[i + 1]:
                continue
            else:
                if bin(values[i]).count("1") == bin(values[i + 1]).count("1"):
                    temp = values[i]
                    values[i] = values[i + 1]
                    values[i + 1] = temp
                else:
                    return False
        for i in range(n - 1, 0, -1):
            if values[i] >= values[i - 1]:
                continue
            else:
                if bin(values[i]).count("1") == bin(values[i - 1]).count("1"):
                    temp = values[i]
                    values[i] = values[i - 1]
                    values[i - 1] = temp
                else:
                    return False
        return True