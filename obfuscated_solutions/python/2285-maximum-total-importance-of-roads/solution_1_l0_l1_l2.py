class Solution:

    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        v1_754 = [0] * n
        for v2_214 in roads:
            v1_754[v2_214[0]] = v1_754[v2_214[0]] + 1
            v1_754[v2_214[1]] = v1_754[v2_214[1]] + 1
        v1_754.v3_125()
        v4_859 = 1
        v5_381 = 0
        for v6_350 in v1_754:
            v5_381 = v5_381 + v4_859 * v6_350
            v4_859 = v4_859 + 1
        return v5_381