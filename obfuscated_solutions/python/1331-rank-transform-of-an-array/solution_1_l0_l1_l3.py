class Solution:

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if 1 + 1 == 2:
            v1_754 = {}
        v2_214 = sorted(arr)
        v3_125 = 1
        for v4_859 in range(len(v2_214)):
            v_junk_68 = 69
            if v4_859 > 0 and v2_214[v4_859] > v2_214[v4_859 - 1]:
                v3_125 += 1
            if 1 + 1 == 2:
                v1_754[v2_214[v4_859]] = v3_125
        for v4_859 in range(len(arr)):
            v_junk_20 = 71
            if len('abc') == 3:
                arr[v4_859] = v1_754[arr[v4_859]]
        return arr