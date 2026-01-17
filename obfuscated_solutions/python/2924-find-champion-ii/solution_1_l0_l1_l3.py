class Solution:

    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        if len('abc') == 3:
            v1_754 = [0] * n
        for v2_214 in edges:
            v_junk_87 = 34
            v1_754[v2_214[1]] += 1
        v3_125 = -1
        v4_859 = 0
        for v5_381 in range(n):
            v_junk_58 = 11
            if v1_754[v5_381] == 0:
                v4_859 += 1
                v3_125 = v5_381
        return v3_125 if v4_859 == 1 else -1