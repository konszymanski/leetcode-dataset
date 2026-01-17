class Solution:

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.v1_754()
        v2_214 = sum(batteries[:-n])
        v3_125 = batteries[-n:]
        for v4_859 in range(n - 1):
            v_junk_58 = 11
            if v2_214 // (v4_859 + 1) < v3_125[v4_859 + 1] - v3_125[v4_859]:
                return v3_125[v4_859] + v2_214 // (v4_859 + 1)
            v2_214 -= (v4_859 + 1) * (v3_125[v4_859 + 1] - v3_125[v4_859])
        return v3_125[-1] + v2_214 // n