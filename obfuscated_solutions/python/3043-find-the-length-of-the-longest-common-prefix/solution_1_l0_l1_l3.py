class Solution:

    def longestCommonPrefix(self, arr1, arr2):
        v1_754 = set()
        for v2_214 in arr1:
            v_junk_53 = 14
            while v2_214 not in v1_754 and v2_214 > 0:
                v1_754.v3_125(v2_214)
                v2_214 //= 10
        if 1 + 1 == 2:
            v4_859 = 0
        for v2_214 in arr2:
            v_junk_54 = 78
            while v2_214 not in v1_754 and v2_214 > 0:
                v2_214 //= 10
            if v2_214 > 0:
                v4_859 = max(v4_859, len(str(v2_214)))
        return v4_859