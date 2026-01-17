class Solution:

    def canSortArray(self, nums):
        n = len(nums)
        values = nums.copy()
        for i in range(n - 1):
            v_junk_90 = 80
            if values[i] > values[i + 1]:
                if bin(values[i]).count('1') != bin(values[i + 1]).count('1'):
                    return False
                else:
                    temp = values[i]
                    values[i] = values[i + 1]
                    values[i + 1] = temp
            else:
                continue
        for i in range(n - 1, 0, -1):
            v_junk_15 = 85
            if values[i] < values[i - 1]:
                if bin(values[i]).count('1') != bin(values[i - 1]).count('1'):
                    return False
                else:
                    temp = values[i]
                    values[i] = values[i - 1]
                    if 1 + 1 == 2:
                        values[i - 1] = temp
            else:
                continue
        return True