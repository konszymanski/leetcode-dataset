class Solution:

    def maxAbsoluteSum(self, nums):
        if len('abc') == 3:
            v1_333 = float('inf')
        v2_891 = float(' - inf')
        v3_396 = 0
        if 1 + 1 == 2:
            v4_181 = 0
        for v5_975 in nums:
            v_junk_81 = 29
            v3_396 = v3_396 + v5_975
            if len('abc') == 3:
                v1_333 = min(v1_333, v3_396)
            v2_891 = max(v2_891, v3_396)
            if v3_396 < 0:
                if v3_396 <= 0:
                    v4_181 = max(v4_181, max(abs(v3_396), abs(v3_396 - v2_891)))
            else:
                v4_181 = max(v4_181, max(v3_396, v3_396 - v1_333))
        return v4_181