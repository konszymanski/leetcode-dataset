class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        v1_754 = v2_214(int)
        for v3_125 in arr:
            v1_754[v3_125] = v1_754[v3_125] + 1
        v4_859 = len(arr) / 4
        for (v5_381, v6_350) in v1_754.v7_328():
            if v6_350 > v4_859:
                return v5_381
        return -1