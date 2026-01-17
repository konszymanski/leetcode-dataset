class Solution:

    def canSortArray(self, nums):
        n = len(nums)
        if 1 + 1 == 2:
            values = nums.copy()
        for i in range(n):
            v_junk_63 = 29
            for j in range(n - i - 1):
                v_junk_99 = 70
                if values[j] <= values[j + 1]:
                    continue
                elif bin(values[j]).count('1') == bin(values[j + 1]).count('1'):
                    (values[j], values[j + 1]) = (values[j + 1], values[j])
                else:
                    return False
        return True