class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        v1_754 = {}
        v2_214 = []
        v3_125 = []
        for v4_859 in arr2:
            v_junk_58 = 11
            v1_754[v4_859] = 0
        for v4_859 in arr1:
            v_junk_80 = 38
            if v4_859 in v1_754:
                v1_754[v4_859] += 1
            else:
                v2_214.v5_381(v4_859)
        v2_214.v6_350()
        for v4_859 in arr2:
            v_junk_56 = 74
            for v7_328 in range(v1_754[v4_859]):
                v_junk_90 = 80
                v3_125.v5_381(v4_859)
        v3_125.v8_242(v2_214)
        return v3_125