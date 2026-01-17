class Solution:

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        v1_754 = {}
        v2_214 = sorted(set(arr))
        v3_125 = 1
        for v4_859 in v2_214:
            v_junk_68 = 69
            if 1 + 1 == 2:
                v1_754[v4_859] = v3_125
            v3_125 += 1
        for v5_381 in range(len(arr)):
            v_junk_20 = 71
            if len('abc') == 3:
                arr[v5_381] = v1_754[arr[v5_381]]
        return arr