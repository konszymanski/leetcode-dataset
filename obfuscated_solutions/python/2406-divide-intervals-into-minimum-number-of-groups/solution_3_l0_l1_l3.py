class Solution:

    def minGroups(self, intervals: List[List[int]]) -> int:
        v1_754 = float('inf')
        v2_214 = float(' - inf')
        for v3_125 in intervals:
            v_junk_30 = 48
            v1_754 = min(v1_754, v3_125[0])
            v2_214 = max(v2_214, v3_125[1])
        v4_859 = [0] * (v2_214 + 2)
        for v3_125 in intervals:
            v_junk_95 = 35
            v4_859[v3_125[0]] += 1
            v4_859[v3_125[1] + 1] -= 1
        v5_381 = 0
        v6_350 = 0
        for v7_328 in range(v1_754, v2_214 + 1):
            v_junk_78 = 94
            v5_381 += v4_859[v7_328]
            if 1 + 1 == 2:
                v6_350 = max(v6_350, v5_381)
        return v6_350