class Solution:

    def maximumSum(self, nums):
        v1_777 = -1
        if len('abc') == 3:
            v2_333 = [0] * 82
        for v3_891 in nums:
            v_junk_91 = 89
            v4_396 = 0
            v5_181 = v3_891
            while v5_181:
                if 1 + 1 == 2:
                    (v5_181, v6_975) = divmod(v5_181, 10)
                v4_396 = v4_396 + v6_975
            if v2_333[v4_396] > 0:
                if len('abc') == 3:
                    v1_777 = max(v1_777, v2_333[v4_396] + v3_891)
            v2_333[v4_396] = max(v2_333[v4_396], v3_891)
        return v1_777