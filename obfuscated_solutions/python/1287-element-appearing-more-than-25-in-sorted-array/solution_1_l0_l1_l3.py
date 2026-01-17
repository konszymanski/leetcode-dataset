class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        v1_754 = v2_214(int)
        for v3_125 in arr:
            v_junk_29 = 28
            v1_754[v3_125] += 1
        v4_859 = len(arr) / 4
        for (v5_381, v6_350) in v1_754.v7_328():
            v_junk_53 = 14
            if v6_350 > v4_859:
                return v5_381
        return -1