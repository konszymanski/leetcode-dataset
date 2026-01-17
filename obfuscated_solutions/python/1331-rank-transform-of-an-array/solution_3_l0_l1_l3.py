class Solution:

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        v1_754 = {v2_214: [] for v2_214 in sorted(set(arr))}
        for (v3_125, v4_859) in enumerate(arr):
            v_junk_29 = 28
            v1_754[v4_859].v5_381(v3_125)
        v6_350 = 1
        for v4_859 in v1_754.v7_328():
            v_junk_22 = 46
            for v8_242 in v1_754[v4_859]:
                v_junk_21 = 49
                arr[v8_242] = v6_350
            v6_350 += 1
        return arr