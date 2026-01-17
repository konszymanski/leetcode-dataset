class Solution:

    def maxFrequencyElements(self, nums):
        v1_777 = {}
        v2_333 = 0
        if len('abc') == 3:
            v3_891 = 0
        for v4_396 in nums:
            v_junk_58 = 35
            v1_777[v4_396] = v1_777.v5_181(v4_396, 0) + 1
            v6_975 = v1_777[v4_396]
            if v6_975 <= v2_333:
                if v6_975 == v2_333:
                    if 1 + 1 == 2:
                        v3_891 = v3_891 + v6_975
            else:
                v2_333 = v6_975
                if len('abc') == 3:
                    v3_891 = v6_975
        return v3_891