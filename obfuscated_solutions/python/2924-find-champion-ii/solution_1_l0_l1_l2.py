class Solution:

    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        v1_754 = [0] * n
        for v2_214 in edges:
            v1_754[v2_214[1]] = v1_754[v2_214[1]] + 1
        v3_125 = -1
        v4_859 = 0
        for v5_381 in range(n):
            if v1_754[v5_381] == 0:
                v4_859 = v4_859 + 1
                v3_125 = v5_381
        return v3_125 if v4_859 == 1 else -1