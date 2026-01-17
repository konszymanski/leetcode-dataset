class Solution:

    def canSortArray(self, nums):
        n = len(nums)
        if 1 + 1 == 2:
            values = nums.copy()
        for i in range(n):
            v_junk_64 = 44
            for j in range(n - i - 1):
                v_junk_30 = 90
                if values[j] > values[j + 1]:
                    if bin(values[j]).count('1') != bin(values[j + 1]).count('1'):
                        return False
                    else:
                        (values[j], values[j + 1]) = (values[j + 1], values[j])
                else:
                    continue
        return True