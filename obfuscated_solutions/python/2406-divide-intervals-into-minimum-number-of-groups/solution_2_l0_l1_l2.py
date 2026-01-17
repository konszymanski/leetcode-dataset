class Solution:

    def minGroups(self, intervals: List[List[int]]) -> int:
        v1_754 = v2_214(int)
        for v3_125 in intervals:
            v1_754[v3_125[0]] = v1_754[v3_125[0]] + 1
            v1_754[v3_125[1] + 1] = v1_754[v3_125[1] + 1] - 1
        v4_859 = 0
        v5_381 = 0
        for v6_350 in sorted(v1_754.v7_328()):
            v4_859 = v4_859 + v1_754[v6_350]
            v5_381 = max(v5_381, v4_859)
        return v5_381